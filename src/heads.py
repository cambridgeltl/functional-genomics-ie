import numpy as np

import torch
from torch import nn

from allennlp.modules.conditional_random_field import ConditionalRandomField, allowed_transitions

from src.misc import get_prf1a, check_tag_list, pad_sequences, copy_type

from util.core import pairs
from util.core import list_of_dicts_to_dict_of_lists as ld2dl
from util.core import dict_of_lists_to_list_of_dicts as dl2ld


# Schmea funcs convert to other schema, assumed BIOES schema
# Single_Label and other appropriate heads will convert Nones into 'O'
def bioes_schema(x):
    if x in ["B", "I", "E", "S"]:
        return x
    return None

def bio_schema(x):
    if x in ["B", "S"]:
        return "B"
    if x in ["I", "E"]:
        return "I"
    return None

def iob1_schema(_):
    raise Exception("Not currently supported")

def io_schema(x):
    if x in ["B", "I", "E", "S"]:
        return "I"
    return None

schema_funcs = {
    "BIOES": bioes_schema,
    "IOB1": iob1_schema,
    "IOB2": bio_schema,
    "BIO": bio_schema,
    "IO": io_schema,
}


# BASE CLASSES

# Base for all heads
class _Head_Base:
    htype = NotImplemented
    _classifier_base = nn.Linear
    _full_pad_tag = NotImplemented
    predic_func = NotImplemented
    _none_tag = NotImplemented
    _extra_non_predicting_tags = []
    _extra_predicting_tags = []
    _ignored_tags = []

    def __init__(self, name, num_labels, input_size, schema=None):
        self._classifier = self._classifier_base(input_size, num_labels)
        self.name = name
        self._tag_list = None
        self._num_predictable_labels = num_labels
        self._num_total_labels = num_labels + len(self._extra_non_predicting_tags)
        self.cuda_device = None

        self.schema = schema
        if schema is not None:
            self.schema_func = schema_funcs[schema]
        else:
            self.schema_func = None

    @property
    def tag_list(self):
        return self._tag_list

    @tag_list.setter
    def tag_list(self, new_list):
        if new_list is not None:

            # Add extra predicting tags
            for tg in self._extra_predicting_tags:
                if tg not in new_list:
                    new_list.append(tg)

            # Remove non predicting tags and ignored tags
            new_list = [x for x in new_list
                        if x not in (self._extra_non_predicting_tags + self._ignored_tags)]

            # Sort and re-add non predicting tags
            new_list = sorted(new_list)
            new_list.extend(sorted(self._extra_non_predicting_tags))

            if self._tag_list is None:
                self._tag_list = new_list
            else:
                check_tag_list(self._tag_list, new_list, exception_on_missing_tags=False,
                               print_full_lists_on_error=True)

            if len(self._tag_list) != self._num_total_labels:
                tag_list_str = '\n'.join(self.tag_list)
                raise Exception(f"Tag list size and num_total_labels mismatch: \
{len(self._tag_list)} vs {self._num_total_labels}, \
tag list:\n{tag_list_str}")

        else:
            self._tag_list = None

    def get_named_params(self):
        return [(n, p) for n, p in self._classifier.named_parameters()]

    def cuda(self):
        self._classifier.cuda()

    def train(self, *args, **kwargs):
        self._classifier.train(*args, **kwargs)

    def eval(self, *args, **kwargs):
        self._classifier.eval(*args, **kwargs)

    def extend_data(self, b_tkns_per_tag, b_tags, maxlen=None):
        new_tags = [[tg for tag, n in zip(tags, tkns_per_tag) for tg in [tag]*n]
                    for tags, tkns_per_tag in zip(b_tags, b_tkns_per_tag)]
        new_tags = pad_sequences(new_tags, maxlen=maxlen, dtype=object, value=self._full_pad_tag)
        return new_tags, {}

    def get_tagged_word_idxs(self, tags):
        return [i for i, t in enumerate(tags) if t != self._none_tag]

    # This will be overwritten by multi tfm input style heads
    @staticmethod
    def form_head_data_dict(labels, extra_inputs, masks):
        return {"labels": labels, "extra_inputs": extra_inputs, "masks": masks}

    # This will be overwritten by mutlit tfm input style heads
    @staticmethod
    def get_labels(head_data):
        return head_data["labels"].to('cpu').numpy()

    def __call__(self, tfm_output, head_data):
        raise NotImplementedError

    def b_tags2b_labels(self, b_tags):
        raise NotImplementedError

    def b_labels2b_tags(self, b_labels):
        raise NotImplementedError

    def b_predictions2b_labels(self, b_predictions):
        raise NotImplementedError

    def filtered_labels2tags(self, b_true_labels, b_pred_labels):
        raise NotImplementedError

    def tags2processed_labels(self, b_tags, b_tokens):
        raise NotImplementedError

    def loss_calc(self, logits, head_data, tfm_data, class_loss_weights=None):
        raise NotImplementedError

    # Helper function to get data out of head_data and tfm_data for easy use
    @staticmethod
    def single_input_loss_vars(head_data, tfm_data):
        return head_data["labels"], head_data["masks"], tfm_data["ntpw"]

    def tag_list_from_b_tags(self, b_tags):
        raise NotImplementedError

    def get_label_weights(self, labels, n):
        raise NotImplementedError

    def accuracy(self, b_predicted_tags, b_actual_tags):
        raise NotImplementedError

    def get_loss_masks(self, b_labels):
        raise NotImplementedError

    @staticmethod
    def b_condense(b_xs, b_n_tkns_per_word, method="first"):
        raise NotImplementedError

    @staticmethod
    def bblabels2blabels(b_b_labels):
        raise NotImplementedError

    @staticmethod
    def b_tags2lists_of_tags(b_tags):
        raise NotImplementedError

    def tag2str(self, tag):
        raise NotImplementedError

    @staticmethod
    def apply_schema_to_tag_list(tag_list, schema):
        raise NotImplementedError


# Base for heads which have labels on a token by token basis i.e. NER, Sequence classification
class _Tkn_Base(_Head_Base):
    _pad_tag = "PAD"
    _extra_non_predicting_tags = [_pad_tag]
    _i_tkn_blacklist = None  # Overrides whitelist
    _i_tkn_whitelist = None  # Leave None if not using specific input tokens for task

    def __call__(self, tfm_output, _):
        return self._classifier(tfm_output)

    @property
    def _none_label(self):
        return self._tag2label(self._none_tag)

    @property
    def _full_pad_label(self):
        return self._tag2label(self._full_pad_tag)

    def force_predictions2labels(self, predictions):
        return [self._force_prediction2label(p) for p in predictions]

    def b_tags2b_labels(self, b_tags):
        return [[self._tag2label(t) for t in tags] for tags in b_tags]

    def b_labels2b_tags(self, b_labels):
       return [[self._label2tag(l) for l in labels] for labels in b_labels]

    def b_predictions2b_labels(self, b_predictions):
       return [[self._prediction2label(p) for p in predictions] for predictions in b_predictions]

    def _process_tag(self, tag, token):
        whitelisted = self._i_tkn_whitelist is None or token in self._i_tkn_whitelist
        blacklisted = self._i_tkn_blacklist is not None and token in self._i_tkn_blacklist
        if blacklisted or not whitelisted:
            return self._full_pad_tag
        else:
            return self._none_tag if tag is None else tag

    def tags2processed_labels(self, b_tags, b_tokens):
        b_tokens = [pad_sequences([x], value="PAD", maxlen=len(y))[0]
                    for x, y in zip(b_tokens, b_tags)]
        processed_tags = [[self._process_tag(tag, token) for tag, token in zip(tags, tokens)]
                          for tags, tokens in zip(b_tags, b_tokens)]
        b_labels = self.b_tags2b_labels(processed_tags)
        return np.array(b_labels, dtype=np.int_)


    @staticmethod
    def b_condense(b_xs, b_n_tkns_per_word, method="first", pad_value=None):
        def f_func(xs, i, _):
            return xs[i]

        def a_func(xs, i, n):
            assert isinstance(xs, (np.ndarray, torch.Tensor))
            return xs[i:i+n].mean(axis=0)

        def m_func(xs, i, n):
            if isinstance(xs, np.ndarray):
                return xs[i:i+n].max(axis=0)
            elif isinstance(xs, torch.Tensor):
                return xs[i:i+n].amax(axis=0)
            else:
                raise Exception

        method_funcs = {
            "first": f_func,
            "average": a_func,
            "maximum": m_func
        }

        new_b_xs = []
        func = method_funcs[method]

        for xs, n_tkns_per_word in zip(b_xs, b_n_tkns_per_word):
            assert sum(n_tkns_per_word) <= len(xs)
            new_xs = []
            i = 0

            for n in n_tkns_per_word:
                if n != 0:
                    new_xs.append(func(xs, i, n))
                    i += n

            if pad_value is not None:
                new_xs.extend([copy_type(xs[0], pad_value) for _ in range(len(xs) - len(new_xs))])
                assert len(new_xs) == len(xs)

            new_b_xs.append(copy_type(xs, new_xs))
        return new_b_xs


    @staticmethod
    def bblabels2blabels(b_b_labels):
        return [x for xs in b_b_labels for x in xs]

    @staticmethod
    def b_tags2lists_of_tags(b_tags):
        return b_tags

    @staticmethod
    def apply_schema_to_tag_list(tag_list, schema):
        if schema is not None:
            return [f"{s}-{tag}" for tag in tag_list for s in schema]
        else:
            return tag_list

    def _tag2label(self, tag):
        raise NotImplementedError

    def _label2tag(self, label):
        raise NotImplementedError

    def _prediction2label(self, prediction):
        raise NotImplementedError

    def _force_prediction2label(self, prediction):
        raise NotImplementedError


# MIXINS

class NonLinMixin:
    @staticmethod
    def _classifier_base(i_size, o_size):
        h_size = int((i_size * o_size) ** 0.5)
        return nn.Sequential(
            nn.Linear(i_size, h_size),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(h_size, o_size)
        )


# MAIN CLASSES

class Single_Label(_Tkn_Base):
    htype = "single_label"
    predic_func = nn.Softmax(dim=-1)
    _full_pad_tag = "PAD"
    _none_tag = "O"
    _extra_predicting_tags = [_none_tag]
    _ignored_tags = [None]
    _i_tkn_blacklist = ["[CLS]", "[SEP]"]

    @property
    def _extra_non_predicting_labels(self):
        return self.b_tags2b_labels([self._extra_non_predicting_tags])[0]

    def loss_calc(self, logits, head_data, tfm_data, class_loss_weights=None):
        labels, loss_mask, b_n_tkns_per_word = self.single_input_loss_vars(head_data, tfm_data)

        _logits = logits.view(-1, self._num_predictable_labels)
        _labels = labels.view(-1)
        loss_func = nn.CrossEntropyLoss(weight=class_loss_weights)

        if loss_mask is not None:
            active_loss = torch.tensor([m == 1 and l not in self._extra_non_predicting_labels
                                        for m, l in zip(loss_mask.view(-1), _labels)],
                                       device=self.cuda_device)
            active_labels = torch.where(
                active_loss, _labels, torch.tensor(loss_func.ignore_index).type_as(labels)
            )
            return loss_func(_logits, active_labels)
        else:
            return loss_func(_logits, _labels)

    def _tag2label(self, tag):
        return self.tag_list.index(tag)

    def _label2tag(self, label):
        return self.tag_list[label]

    @staticmethod
    def _prediction2label(prediction):
        return np.argmax(prediction)

    def _force_prediction2label(self, prediction):
        prediction[self._none_label] = -1
        return self._prediction2label(prediction)

    @staticmethod
    def tag_list_from_b_tags(b_tags):
        return list(set([tag for tags in b_tags for tag in tags]))

    def get_label_weights(self, labels, n):
        counts = torch.tensor(labels).view(-1).bincount(minlength=self._num_predictable_labels)
        w = (1 / (1 + counts)) ** n
        w = w[:self._num_predictable_labels]
        return w / sum(w)

    def accuracy(self, b_true_labels, b_pred_labels):
        tp, fp, fn, total_Neg = 0, 0, 0, 0
        for true_labels, pred_labels in zip(b_true_labels, b_pred_labels):
            for t, p in zip(true_labels, pred_labels):
                if (t != self._none_label or p != self._none_label) and t != self._full_pad_label:
                    tp += t == p
                    fp += t != p and p != self._none_label
                    fn += t != p and t != self._none_label
                    total_Neg += t != p
        return get_prf1a(tp, fp, fn, (fp + fn))

    def get_loss_masks(self, b_labels):
        return [[float(label != self._full_pad_label) for label in labels]
                for labels in b_labels]

    def tag2str(self, tag):
        return '' if tag == self._none_tag else str(tag)


class CRF(Single_Label):
    htype = "CRF"
    predic_func = nn.Identity()  # Viterbi tags algorithm expects logits

    def __init__(self, schema, **kwargs):
        assert schema == "BIO"  # Only supported at the moment
        super().__init__(schema=schema, **kwargs)
        self._crf = None

    def cuda(self):
        super().cuda()
        self._crf.cuda()

    @Single_Label.tag_list.setter
    def tag_list(self, new_list):
        Single_Label.tag_list.fset(self, new_list)
        if self._crf is None:
            labels = {k: v for k, v in enumerate(
                self.tag_list[:self._num_predictable_labels])}
            constraints = allowed_transitions(self.schema, labels)
            self._crf = ConditionalRandomField(self._num_predictable_labels, constraints)

    def get_named_params(self):
        return super().get_named_params() + [(n, p) for n, p in self._crf.named_parameters()]

    def loss_calc(self, logits, head_data, tfm_data, class_loss_weights=None):
        labels, loss_mask, b_n_tkns_per_word = self.single_input_loss_vars(head_data, tfm_data)

        # Need to condense as inter-tag relationships are important
        # Pad so we can turn these back into tensors
        _logits = torch.stack(self.b_condense(
            logits, b_n_tkns_per_word, method="average",
            pad_value=torch.zeros(self._num_predictable_labels, device=self.cuda_device)
        ))
        _labels = torch.stack(self.b_condense(labels, b_n_tkns_per_word, method="first",
                                              pad_value=self._full_pad_label))
        _loss_mask = torch.stack(self.b_condense(loss_mask, b_n_tkns_per_word, method="first",
                                                 pad_value=0))

        # This will increase loss related with rare tags and decrease it for common ones
        # Works by pushing low weighted (less than one) logits towards their labels and
        # higly weighted ones away from their labels
        # Below is correct logic but destroys gradients and is extremely slow
#       bool_labels = torch.tensor([[[x==i for i in range(_logits.shape[-1])] for x in xs]
#                                      for xs in _labels], device=self.cuda_device)
#       _logits = torch.tensor([[[x/z if y else x*z for x, y, z in zip(xs, ys, class_loss_weights)]
#                                for xs, ys in zip(xss, yss)]
#                               for xss, yss in zip(_logits, bool_labels)], device=self.cuda_device)

        # Can't put pad label into crf as it's out of range so we set it to none label
        # Loss mask ensures these false nones aren't actually used
        active_labels = torch.tensor([[x not in self._extra_non_predicting_labels for x in l]
                                      for l in _labels], device=self.cuda_device)
        dummy_labels = torch.tensor([[self._none_label for _ in l] for l in _labels],
                                    device=self.cuda_device)
        __labels = torch.where(active_labels, _labels, dummy_labels)
        return -self._crf(_logits, __labels, mask=_loss_mask)

    def b_predictions2b_labels(self, b_predictions):
        # No need to condense here as model will have already called that method
        b_predictions = [torch.tensor(ps, device=self.cuda_device) for ps in b_predictions]
        return [x for x, y in [self._crf.viterbi_tags(ps.view(1, *ps.shape))[0]
                               for ps in b_predictions]]

    # Do this so if it's accidentally called it throws an error
    def _prediction2label(self, prediction):
        raise NotImplementedError


class Multi_Label(_Tkn_Base):
    htype = "multi_label"
    predic_func = nn.Sigmoid()
    _full_pad_tag = ["PAD"]
    _none_tag = []
    _i_tkn_blacklist = ["[CLS]", "[SEP]"]

    def loss_calc(self, logits, head_data, tfm_data, class_loss_weights=None):
        labels, loss_mask, b_n_tkns_per_word = self.single_input_loss_vars(head_data, tfm_data)
        _logits = logits.view(-1, self._num_predictable_labels)
        _labels = labels.view(-1, self._num_total_labels).type_as(_logits)
        _labels = _labels[:,:self._num_predictable_labels]  # Cut off extra non-predicting labels
        loss_func = nn.BCEWithLogitsLoss(pos_weight=class_loss_weights)

        if loss_mask is not None:
            active_loss = (loss_mask.view(-1) == 1).view(-1, 1)
            active_logits = torch.where(active_loss, _logits, _labels)
            return loss_func(active_logits, _labels)
        else:
            return loss_func(_logits, _labels)

    def _tag2label(self, tag):
        return [int(tag_k in tag) for tag_k in self.tag_list]

    def _label2tag(self, label):
        return [tag for i, tag in enumerate(self.tag_list) if label[i] == 1]

    def _prediction2label(self, prediction):
        extra_labels = [0 for _ in self._extra_non_predicting_tags]
        return np.array([int(lp > 0.5) for lp in prediction] + extra_labels)

    def _force_prediction2label(self, prediction):
        prediction[np.argmax(prediction)] = 1
        return self._prediction2label(prediction)

    @staticmethod
    def tag_list_from_b_tags(b_tags):
        return list(set([t for tags in b_tags for tag in tags for t in tag]))

    def get_label_weights(self, labels, n):
        _labels = torch.tensor(labels).view(-1, self._num_total_labels)
        _labels = _labels[:,:self._num_predictable_labels]  # Cut off extra non-predicting labels
        pos_counts = _labels.sum(axis=0)
        total_counts = _labels.size(0)
        w = ((total_counts - pos_counts) / (pos_counts + 1)) ** n
        return w

    def accuracy(self, b_true_labels, b_pred_labels):
        tp, fp, fn = 0, 0, 0
        for true_labels, pred_labels in zip(b_true_labels, b_pred_labels):
            for t, p in zip(true_labels, pred_labels):
                if any(t != self._full_pad_label):
                    tp += (t * p).sum().item()
                    fp += ((1 - t) * p).sum().item()
                    fn += (t * (1 - p)).sum().item()
        return get_prf1a(tp, fp, fn, (fp + fn))

    def get_loss_masks(self, b_labels):
        return [[float(any(label != self._full_pad_label)) for label in labels]
                for labels in b_labels]

    def tag2str(self, tag):
        return "" if tag == self._none_tag else ', '.join([str(t) for t in tag])


class Multi_Label_Seq(Multi_Label):
    _i_tkn_blacklist = None
    _i_tkn_whitelist = ["[CLS]"]


class Entity_Link(_Head_Base):
    htype = "link"
    _none_tag = []
    _full_pad_tag = []
    _predic_func = nn.Sigmoid()

    # Tag is a list of tuples for each token, tuple contains id and the link type
    #     e.g. 7 words with the 1st and 3rd with same tag and linked to the tag on 5th word
    #          with the 4th and 7th words also on the same tag would be:
    #               [[("t0", "same_tag"), ("l0", "linked")],
    #                [],
    #                [("t0", "same_tag"), ("l0", "linked")],
    #                [("t1", "same_tag")],
    #                [("l0", "linked")],
    #                [],
    #                [("t1", "same_tag")]]
    # All ids must have the same link type
    # Label is a upper triangular matrix of length equal to number of tokens
    # Each element represents the links between 2 tokens, it's a vector of size num_labels
    # with appropriate 1's and 0's for each possible link type
    # Tags are stored in a dict (so are active_tkn_idxs) which are keyed by possible link sets
    # (Note this is not the same as link type)
    # This is so we can predict separately for lots of different things with the same classifier
    # For the fgeom case the link sets could be the different tags (e.g. species|human,
    # phenotype|adhesion) and a single link type of same_tag
    # This also means when we predict links for our tags we aren't wasting time checking if 2
    # completely different tags are the same tag or not when they can't possibly be
    # Calculate label pos_weight across all dicts together since they use same classifier

    @classmethod
    def predic_func(cls, x):
        return {k: cls._predic_func(v) for k, v in x.items()}

    def __init__(self, name, num_labels, input_size, combine_label_weights=True, **kwargs):
        self._combine_label_weights = combine_label_weights
        super().__init__(name, num_labels, input_size*2, **kwargs)

    def __call__(self, tfm_output, head_data):
        active_tkn_idxs = head_data["extra_inputs"]["active_tkn_idxs"]
        active_tkn_idxs = {k: [[i for i, x in enumerate(entry_idxs) if x]
                               for entry_idxs in v] for k, v in active_tkn_idxs.items()}

        logits_dict = {}
        n_tkns = tfm_output.shape[1]
        for k, at_idxs in active_tkn_idxs.items():
            # Dims are batch, tkns, hidden size
            assert len(tfm_output) == len(at_idxs)  # Check equal batch size

            # We need large negative number so when sigmoid it ends close to 0
            logits = torch.zeros((1,))
            logits = logits.new_full((len(tfm_output), n_tkns, n_tkns,
                                      self._num_predictable_labels), -100, device=self.cuda_device)

            for n, entry_idxs in enumerate(at_idxs):
                for i, j in pairs(entry_idxs):
                    # Keep things upper triangular
                    i, j = min(i,j), max(i,j)
                    logits[n,i,j] = self._classifier(torch.cat((tfm_output[n,i], tfm_output[n,j])))
            logits_dict[k] = logits.requires_grad_(True)

        return logits_dict

    def _tags2labels(self, tags, k):
        labels = np.zeros((len(tags), len(tags), self._num_predictable_labels))
        tag_id_indexes = {}
        tag_id_types = {}

        # Build up dict of tag link indices and types
        for i, tag in enumerate(tags):
            for t_id, link_type in tag:
                if t_id in tag_id_indexes.keys() and t_id in tag_id_types.keys():
                    tag_id_indexes[t_id].append(i)
                    assert link_type == tag_id_types[t_id]
                elif t_id not in tag_id_indexes.keys() and t_id not in tag_id_types.keys():
                    tag_id_indexes[t_id] = [i]
                    tag_id_types[t_id] = link_type
                else:
                    raise Exception("Uh-oh")

        # Iterate through dict
        for t_id, linked_idxs in tag_id_indexes.items():
            for i, j in pairs(linked_idxs):
                # Keep things upper triangular, though not strictly neccessary here due to above
                i, j = min(i,j), max(i,j)
                labels[i][j][self.tag_list.index(tag_id_types[t_id])] = 1

        return labels

    def _labels2tags(self, labels, k):
        idn = 0
        tags = [[] for _ in range(len(labels))]
        for i, label in enumerate(labels):
            for j, link_types_label in enumerate(label):
                link_types = [tag for n, tag in enumerate(self.tag_list)
                              if link_types_label[n] == 1]
                for link_type in link_types:
                    tags[i].append((f"l{idn}", link_type))
                    tags[j].append((f"l{idn}", link_type))
                    idn += 1
        return tags

    def predictions2labels(self, predictions):
        return np.array([[[int(x > 0.5) for x in tkn_tkn_link] for tkn_tkn_link in tkn_predictions]
                         for tkn_predictions in predictions])

    def b_tags2b_labels(self, b_tags):
        return {k: [self._tags2labels(tags, k) for tags in ts] for k, ts in b_tags.items()}

    def b_labels2b_tags(self, b_labels):
        return {k: [self._labels2tags(labels, k) for labels in ls]
                for k, ls in b_labels.items()}

    def b_predictions2b_labels(self, b_predictions):
        return {k: [self.predictions2labels(predictions) for predictions in ps]
                for k, ps in b_predictions.items()}

    def tags2processed_labels(self, b_tags, _):
        return {k: np.array(v) for k, v in self.b_tags2b_labels(b_tags).items()}

    def loss_calc(self, logits, head_data, tfm_data, class_loss_weights=None):
        labels, loss_mask, b_n_tkns_per_word = self.single_input_loss_vars(head_data, tfm_data)
        loss = None
        for k in logits.keys():
            w = class_loss_weights if self._combine_label_weights else class_loss_weights[k]
            _logits = logits[k].view(-1, self._num_predictable_labels)
            _labels = labels[k].view(-1, self._num_predictable_labels).type_as(_logits)
            if loss is None:
                loss = nn.BCEWithLogitsLoss(pos_weight=w)(_logits, _labels)
            else:
                loss += nn.BCEWithLogitsLoss(pos_weight=w)(_logits, _labels)
        return loss

    def tag_list_from_b_tags(self, b_tags):
        return set([t for ts in b_tags.values() for tags in ts for tag in tags for _, t in tag])

    def extend_data(self, b_tkns_per_tag, b_tags, active_tkn_idxs, maxlen=None):
        new_b_tags = {k: _Head_Base.extend_data(self, b_tkns_per_tag, v, maxlen=maxlen)[0]
                         for k, v in b_tags.items()}
        new_active_tkn_idxs = {k: [[i for idx, n in zip(idxs, tkns_per_tag) for i in [idx]*n]
                                   for idxs, tkns_per_tag in zip(v, b_tkns_per_tag)]
                               for k, v in active_tkn_idxs.items()}
        new_active_tkn_idxs = {k: pad_sequences(v, maxlen=maxlen, dtype=bool, value=False)
                               for k, v in new_active_tkn_idxs.items()}
        return new_b_tags, {"active_tkn_idxs": new_active_tkn_idxs}


    def get_label_weights(self, b_labels, n, active_tkn_idxs):
        assert b_labels.keys() == active_tkn_idxs.keys()

        p = {k: torch.zeros((self._num_predictable_labels)) for k in b_labels.keys()}
        t = {k: torch.zeros((self._num_predictable_labels)) for k in b_labels.keys()}

        for k, labels in b_labels.items():
            active_tkn_idxs_k = [[i for i, x in enumerate(entry_idxs) if x]
                               for entry_idxs in active_tkn_idxs[k]]
            assert len(labels) == len(active_tkn_idxs_k)
            for e_num, entry_idxs in enumerate(active_tkn_idxs_k):
                for i, j in pairs(entry_idxs):
                    i, j = min(i,j), max(i,j)
                    p[k] += labels[e_num,i,j]
                    t[k] += 1

        if self._combine_label_weights:
            return ((sum(t.values()) - sum(p.values())) / (sum(p.values()) + 1)) ** n
        else:
            return {k: ((sum(t[k].values()) - sum(v.values())) / (sum(v.values()) + 1)) ** n
                    for k, v in p.items()}

    @staticmethod
    def bblabels2blabels(b_b_labels):
        return {k: [x for xs in v for x in xs] for k, v in ld2dl(b_b_labels).items()}

    def accuracy(self, b_true_labels, b_pred_labels, combine_score=True):
        assert b_true_labels.keys() == b_pred_labels.keys()

        tp = {k: 0 for k in b_true_labels.keys()}
        fp = {k: 0 for k in b_true_labels.keys()}
        fn = {k: 0 for k in b_true_labels.keys()}

        for k, v in b_true_labels.items():
            for true_labels, pred_labels in zip(v, b_pred_labels[k]):
                tp[k] += (true_labels * pred_labels).sum().item()
                fp[k] += ((1 - true_labels) * pred_labels).sum().item()
                fn[k] += (true_labels * (1 - pred_labels)).sum().item()

        if combine_score:
            fp = sum(fp.values())
            fn = sum(fn.values())
            return get_prf1a(sum(tp.values()), fp, fn, (fp + fn))
        else:
            return {k: get_prf1a(tp[k], v, fn[k], (v + fn[k])) for k, v in fp.items()}

    def get_loss_masks(self, b_labels):
        return None


    @staticmethod
    def b_condense(b_xs, b_n_tkns_per_word, method="first"):
        def f_func(xs, i, j, *_):
            return xs[i][j]

        def a_func(xs, i, j, ni, nj):
            assert isinstance(xs, (np.ndarray, torch.Tensor))
            return xs[i:i+ni,j:j+nj].mean(axis=(0,1))

        def m_func(xs, i, j, ni, nj):
            if isinstance(xs, np.ndarray):
                return xs[i:i+ni,j:j+nj].max(axis=(0,1))
            elif isinstance(xs, torch.Tensor):
                return xs[i:i+ni,j:j+nj].amax(axis=(0,1))
            else:
                raise Exception

        method_funcs = {
            "first": f_func,
            "average": a_func,
            "maximum": m_func
        }
        func = method_funcs[method]

        new_b_xs = {}

        for k, k_b_xs in b_xs.items():
            new_k_b_xs = []

            for ps, n_tkns_per_word in zip(k_b_xs, b_n_tkns_per_word):
                assert sum(n_tkns_per_word) <= len(ps)

                new_ps = np.zeros((len(n_tkns_per_word), len(n_tkns_per_word), ps.shape[-1]))

                i = 0
                for new_li, ni in enumerate(n_tkns_per_word):
                    if ni != 0:
                        j = 0
                        for new_lj, nj in enumerate(n_tkns_per_word):
                            if nj != 0:
                                new_ps[new_li][new_lj] = func(ps, i, j, ni, nj)
                                j += nj
                        i += ni

                new_k_b_xs.append(copy_type(ps, new_ps))
            new_b_xs[k] = new_k_b_xs
        return new_b_xs


    @staticmethod
    def b_tags2lists_of_tags(b_tags):
        return [dl2ld(tags) for tags in dl2ld(b_tags)]

    def tag2str(self, tag_dict):
        tag_strs = []
        for k, v in tag_dict:
            if v != self._none_tag:
                tag_strs.append(', '.join([f"{k}_{i}_{t}" for i, t in v]))
        return ', '.join(tag_strs)

    @staticmethod
    def apply_schema_to_tag_list(tag_list, schema):
        return tag_list


# DERIVATIVE CLASSES

class NonLin_Single_Label(NonLinMixin, Single_Label): pass
class NonLin_Multi_Label(NonLinMixin, Multi_Label): pass
class NonLin_Multi_Label_Seq(NonLinMixin, Multi_Label_Seq): pass

