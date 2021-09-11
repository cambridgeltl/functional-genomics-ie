import json
import time

from transformers import AdamW, get_linear_schedule_with_warmup, AutoModel

import torch
from torch.nn import Module, Dropout
from torch.nn.utils import clip_grad_norm_

from src.heads import Single_Label, Multi_Label, Entity_Link, CRF
from src.misc import get_cuda_info, dict_dget
from src.dataloading import load_fgeom_json_data
from src.custom_datatypes import deep_eD

from util.core import list_of_dicts_to_dict_of_lists as ld2dl
from util.core import dict_of_lists_to_list_of_dicts as dl2ld
from util.core import printv


head_types = {x.htype: x for x in [Single_Label, Multi_Label, Entity_Link, CRF]}

optimizers = {"AdamW": AdamW}

# TODO: Make this a proper part of Custom_Model class
def fgeom_predictions2labels(model, predictions):
    # First convert the categories onto a per prediction bases instead of batch basis
    predictions = [dl2ld(_dict) for _dict in dl2ld(predictions)]

    c_head = model._heads["category"]

    category_heads = {"PA": ["description"], "C": ["species", "experiment_type"],
                      "E": ["phenotype", "activity"]}

    def get_individual_label_dict(p):

        r_dict = {"category": c_head._prediction2label(p["category"])}

        # First get list of categories regardless of category head type
        categories = c_head._label2tag(r_dict["category"])
        if isinstance(c_head, Single_Label):
            categories = [] if categories is c_head._none_tag else [categories]

        # Now we iterate through 'required' predictions and force them, otherwise we assume none
        for category, heads in category_heads.items():
            for head in heads:

                # Need to force prediction
                if category in categories:
                    r_dict[head] = model._heads[head]._force_prediction2label(p[head])
                else:
                    r_dict[head] = model._heads[head]._none_label

        return r_dict

    labels = [[get_individual_label_dict(p) for p in ps] for ps in predictions]
    return ld2dl([ld2dl(x) for x in labels])

predictions2labels_funcs = {
    "fgeom": fgeom_predictions2labels
}


class Custom_Model(Module):

    def __init__(self, config, max_input_length):
        super().__init__()
        v = config.get("VERBOSE", 0) >= 1

        tfm_config = config.get("TRANSFORMER_KWARGS", {})
        tfm_kwargs = {"output_attentions": False, "output_hidden_states": False}
        tfm_kwargs.update(tfm_config)
        self.tfm = AutoModel.from_pretrained(config["TRANSFORMER_MODEL"], **tfm_kwargs)

        def get_head(htype, **kwargs):
            return head_types[htype](**kwargs)
        hidden_size = self.tfm.config.hidden_size
        self._heads = {k: get_head(name=k, input_size=hidden_size, **kwargs)
                       for k, kwargs in config["HEADS"].items()}

        schema_funcs = {k: h.schema_func for k, h in self._heads.items()}
        self.tag_list = self.load_tag_list(config.get("TAG_LIST_DEFINITIONS", None),
                                           schema_funcs=schema_funcs, verbose=v)
        self.tag_categories = self.load_tag_categories(config["TAG_CATEGORY_DEFINITIONS"], v)
        self.dropout = Dropout(config.get("DROPOUT", 0.1))
        self.combine_losses = config.get("COMBINE_LOSSES", True)
        self.cuda_device = None
        self.custom_predictions2labels = None
        self.max_input_length = max_input_length

    @property
    def tag_list(self):
        return {k: h.tag_list for k, h in self._heads.items()}

    @tag_list.setter
    def tag_list(self, new_tag_list):
        if new_tag_list is not None:
            for k, tag_list in new_tag_list.items():
                if k in self._heads.keys():
                    self._heads[k].tag_list = tag_list
                else:
                    print(f"[W] Tag list definition given for {k} but there is no head for it")

    def clear_tag_lists(self):
        for h in self._heads.values():
            h.tag_list = None

    def cuda_setup(self):
        using_gpu, self.cuda_device = get_cuda_info()
        if using_gpu:
            self.cuda()
        for h in self._heads.values():
            h.cuda_device = self.cuda_device
            if using_gpu:
                h.cuda()

    def train(self, *args, **kwargs):
        super().train(*args, **kwargs)
        for h in self._heads.values():
            h.train(*args, **kwargs)

    def eval(self, *args, **kwargs):
        super().eval(*args, **kwargs)
        for h in self._heads.values():
            h.eval(*args, **kwargs)

    def pre_process_input_data(self, input_data):
        if isinstance(input_data, dict):
            if set(input_data.keys()) != {"tfm", "head"}:
                raise Exception(f"Input data dict has bad keys {input_data.keys()}, \
                                should be 'tfm' and 'head' only")
        else:
            print("[W] Input data was not a dict, converting it")
            input_data = {"tfm": input_data, "head": {}}

        i_keys = set(input_data["head"].keys())
        h_keys = set(self._heads.keys())

        for key in h_keys - i_keys:
            input_data["head"][key] = {}

        if i_keys - h_keys != set():
            print(f"[W] Extra keys found in input data: {i_keys - h_keys}")

        return input_data


    def apply_schema_to_tag_lists(self, tag_lists, schema_funcs):
        schema = {k: set([f(x) for x in ["B", "I", "E", "S"]])
                  for k, f in schema_funcs.items() if f is not None}
        return {k: h.apply_schema_to_tag_list(tag_lists[k], schema.get(k, None))
                for k, h in self._heads.items()}


    @staticmethod
    def load_tag_categories(fpath, verbose=False):
        printv(f"[I|Model] Loading tag categories from file", verbose_flag=verbose)
        with open(fpath) as f:
            return json.load(f)


    def load_tag_list(self, fpath, schema_funcs=None, verbose=False):
        if fpath is not None:
            printv(f"[I|Model] Loading tags from file", verbose_flag=verbose)
            with open(fpath) as f:
                new_tag_lists = json.load(f)
            if schema_funcs is not None:
                new_tag_lists = self.apply_schema_to_tag_lists(new_tag_lists, schema_funcs)
            return new_tag_lists
        return None


    def set_custom_ps2ls(self, func_name):
        self.custom_predictions2labels = predictions2labels_funcs[func_name]


    def forward(self, model_data, class_loss_weights=None):

        def get_output(i_dict):
            return self.dropout(self.tfm(i_dict["iids"], attention_mask=i_dict["masks"])[0])

        outputs = {kh: {ki: get_output(vi) for ki, vi in vh.items()}
                   if kh != "default" else get_output(vh)
                   for kh, vh in model_data["tfm"].items()}

        logits = {k: h(dict_dget(outputs, k, "default"), model_data["heads"][k])
                  for k, h in self._heads.items()}

        losses = {}
        for k, h_data in model_data["heads"].items():
            clw = class_loss_weights[k].to(self.cuda_device)
            losses[k] = self._heads[k].loss_calc(
                logits[k], head_data=h_data, tfm_data=dict_dget(model_data["tfm"], k, "default"),
                class_loss_weights=clw
            )

        losses = deep_eD(losses)

        return {
            "loss": losses,
            "logits": logits,
            "predictions": deep_eD({k: self._heads[k].predic_func(v) for k, v in logits.items()}),
        }


    def forward_batch(self, batch, grad=True, class_loss_weights=None):
        model_data, = batch
        model_data = deep_eD(model_data).to(self.cuda_device)

        if grad:
            outputs = self(model_data, class_loss_weights=class_loss_weights)
        else:
            with torch.no_grad():
                outputs = self(model_data, class_loss_weights=class_loss_weights)

        # TODO: Make this work for multi-input, WIP
        outputs["b_n_tkns_per_word"] = {kh: {ki: vi["ntpw"].to('cpu').numpy
                                             for ki, vi in vh.items()}
                                        if kh != "default" else vh["ntpw"].to('cpu').numpy()
                                        for kh, vh in model_data["tfm"].items()}
        outputs["b_labels"] = {k: self._heads[k].get_labels(v)
                               for k, v in model_data["heads"].items()}
        outputs["predictions"] = outputs["predictions"].detach().to('cpu').numpy()
        return outputs


    def train_model(self, train_dataloader, val_dataloader, config, class_loss_weights):

        recombination_method = config.get("RECOMBINATION_METHOD", "first")
        v_num = config.get("VERBOSE", 0)
        v1 = v_num >= 1
        v2 = v_num >= 2
        v3 = v_num >= 3

        # Get training params
        params = self.get_train_params(full_finetuning=config.get("FULL_FINETUNING", True))

        # Setup optimizer
        optimizer = optimizers[config["OPTIMIZER_CLASS"]](params, **config["OPTIMIZER_KWARGS"])

        # Scheduler to linearly reduce learning rate
        epochs = config["EPOCHS"]
        total_steps = len(train_dataloader) * epochs
        scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0,
                                                    num_training_steps=total_steps)

        # Fitting model
        loss_values, validation_loss_values = [], []
        validation_accuracy_values = []

        timer = time.time()

        for epoch_num in range(epochs):

            printv(f"[I|Train] Epoch {epoch_num}/{epochs}", verbose_flag=v1)

            # Put model in train mode
            self.train()
            train_loss = 0

            # Training loop
            for step, batch in enumerate(train_dataloader):

                printv(f"[I|Train] Train Batch {step}/{len(train_dataloader)}", verbose_flag=v3)

                # Clear any gradients
                self.zero_grad()

                # Get loss for this batch
                outputs = self.forward_batch(batch, class_loss_weights=class_loss_weights)
                train_loss += outputs["loss"].item()
                if self.combine_losses:
                    total_loss = sum(x for x in outputs["loss"].values())
                    total_loss.backward()
                else:
                    outputs["loss"].backward()

                # Norm gradients to stop them exploding
                clip_grad_norm_(parameters=self.parameters(),
                                max_norm=config.get("MAX_GRAD_NORM", 1))

                # Update parameters & learning rate
                optimizer.step()
                scheduler.step()

            # Calculate average loss over training data and store loss value
            avg_train_loss = train_loss / len(train_dataloader)
            printv(f"[I|Train] Average train loss: {avg_train_loss}", verbose_flag=v2)
            loss_values.append(avg_train_loss)

            if val_dataloader is not None:
                eval_loss, val_acuracy = self.validate(val_dataloader, class_loss_weights, v3,
                                                       recombination_method=recombination_method)
                validation_loss_values.append(eval_loss)

                validation_accuracy_values.append(val_acuracy)

                printv(f"[I|Train] Average validation loss: {eval_loss}", verbose_flag=v2)
                printv(f"[I|Train] Validation Accuracy: {val_acuracy}", verbose_flag=v2)

            new_time = time.time()
            t_taken = new_time - timer
            t_taken_str = time.strftime("%H:%M:%S",time.gmtime(t_taken))
            t_left_str = time.strftime("%H:%M:%S",time.gmtime(t_taken * (epochs - epoch_num - 1)))
            printv(f"[I|Train] Epoch took {t_taken_str}, predicted {t_left_str} left",
                   verbose_flag=v1)
            timer = new_time

        history = {
            "train_losses": loss_values,
            "validation_losses": validation_loss_values,
            "validation_accuracies": validation_accuracy_values
        }

        return history


    def validate(self, val_dataloader, class_loss_weights, v3=False, recombination_method="first"):
        # Put model in evaluation mode
        self.eval()
        eval_loss = 0
        true_labels = {k: [] for k in self._heads.keys()}
        pred_labels = {k: [] for k in self._heads.keys()}

        # Validation loop
        for step, batch in enumerate(val_dataloader):

            printv(f"[I|Train] Validation Batch {step}/{len(val_dataloader)}", verbose_flag=v3)

            # Get loss and predictions for this batch
            outputs = self.forward_batch(batch, grad=False, class_loss_weights=class_loss_weights)
            new_true_labels = self.condense(outputs["b_labels"], outputs["b_n_tkns_per_word"])
            new_pred_labels = self.predictions2condensed_labels(outputs["predictions"],
                                                                outputs["b_n_tkns_per_word"],
                                                                method=recombination_method)

            # Calculate the accuracy for this batch of test sentences
            eval_loss += outputs["loss"].mean().item()

            for k in new_true_labels.keys():
                true_labels[k].append(new_true_labels[k])
                pred_labels[k].append(new_pred_labels[k])

        printv(f"[I|Train] Computing Accuracy", verbose_flag=v3)
        true_labels = self.bblabels2blabels(true_labels)
        pred_labels = self.bblabels2blabels(pred_labels)
        val_acuracy = {k: self._heads[k].accuracy(true_labels[k], pred_labels[k])
                       for k in true_labels.keys()}
        eval_loss = eval_loss / len(val_dataloader)

        return eval_loss, val_acuracy


    def predict_tags(self, dataloader, heads=None, recombination_method="first"):
        heads = self._heads.keys() if heads is None else heads
        self.eval()
        pred_labels = {k: [] for k in heads}

        for batch in dataloader:
            outputs = self.forward_batch(batch, grad=False)
            new_pred_labels = self.predictions2condensed_labels(outputs["predictions"],
                                                                outputs["b_n_tkns_per_word"],
                                                                method=recombination_method)
            for k, v in pred_labels.items():
                v.append(new_pred_labels[k])

        return self.labels2tags(self.bblabels2blabels(pred_labels))


    def bblabels2blabels(self, bblabels):
        return {k: self._heads[k].bblabels2blabels(v) for k, v in bblabels.items()}


    def get_train_params(self, full_finetuning):
        # self.named_parameters() won't yield these parameters
        classifier_params = [(n, p) for h in self._heads.values()
                             for n, p in h.get_named_params()]

        if full_finetuning:
            params = [(n, p) for n, p in self.named_parameters()] + classifier_params
        else:
            params = classifier_params

        # Parameters to not apply weight decay to
        no_decay = ['bias', 'gamma', 'beta']
        optimizer_grouped_parameters = [
            {'params': [p for n, p in params if not any(nd in n for nd in no_decay)],
             'weight_decay_rate': 0.01},
            {'params': [p for n, p in params if any(nd in n for nd in no_decay)],
             'weight_decay_rate': 0.0}
        ]

        return optimizer_grouped_parameters


    def labels2tags(self, b_labels):
        return {k: self._heads[k].b_labels2b_tags(v) for k, v in b_labels.items()}

    def tags2labels(self, b_tags):
        return {k: self._heads[k].b_tags2b_labels(v) for k, v in b_tags.items()}

    def get_label_weights(self, labels, n, head_data):
        return {k: self._heads[k].get_label_weights(ls, n, **head_data[k])
                for k, ls in labels.items()}

    def predictions2condensed_labels(self, b_predictions, b_n_tkns_per_word, method="first"):
        if self.custom_predictions2labels is None:
            cb_ps = self.condense(b_predictions, b_n_tkns_per_word, method=method)
            return {k: self._heads[k].b_predictions2b_labels(p) for k, p in cb_ps.items()}
        else:
            return self.condense(self.custom_predictions2labels(self, b_predictions),
                                 b_n_tkns_per_word)

    def condense(self, b_xs, b_n_tkns_per_word, method="first"):
        return {k: self._heads[k].b_condense(b_xs_k, dict_dget(b_n_tkns_per_word, k, "default"),
                                             method=method)
                for k, b_xs_k in b_xs.items()}

    def load_fgeom_json_data(self, path, sep_sentences=False):
        return load_fgeom_json_data(path, [(k, h.htype, h.schema_func)
                                           for k, h in self._heads.items()],
                                    self.tag_categories,
                                    sep_sentences=sep_sentences)

    def tags2processed_labels(self, b_tags, b_tokens):
        return {k: self._heads[k].tags2processed_labels(t, dict_dget(b_tokens, k, "default"))
                for k, t in b_tags.items()}

    def get_loss_masks(self, b_labels):
        return {k: self._heads[k].get_loss_masks(v) for k, v in b_labels.items()}

    def extend_data(self, tkns_per_word, tags, head_data, maxlen=None):
        new_tags, new_head_data = {}, {}
        for k, t in tags.items():
            new_tags[k], new_head_data[k] = self._heads[k].extend_data(
                dict_dget(tkns_per_word, k, "default"), t, **head_data[k], maxlen=maxlen)
        return new_tags, new_head_data

    def form_head_data_dicts(self, labels, head_extra_inputs, masks):
        assert labels.keys() == head_extra_inputs.keys() == masks.keys()
        return {k: self._heads[k].form_head_data_dict(ls, head_extra_inputs[k], masks[k])
                for k, ls in labels.items()}

    def tag_list_from_tags(self, tags):
        return {k: self._heads[k].tag_list_from_b_tags(v) for k, v in tags.items()}

    def get_tagged_word_idxs(self, b_tags):
        b_tagged_word_idxs = []
        for tags in dl2ld(b_tags):
            tagged_word_idxs = []
            for k, ts in tags.items():
                tagged_word_idxs.extend(self._heads[k].get_tagged_word_idxs(ts))
            b_tagged_word_idxs.append(list(set(tagged_word_idxs)))
        return b_tagged_word_idxs

    def get_word_tag_pairs(self, b_words, b_tags, ignored_heads=None):
        b_tags = {k: self._heads[k].b_tags2lists_of_tags(v) for k, v in b_tags.items()}
        return [[(str(word), self.tag2str(tag, ignored_heads=ignored_heads))
                 for word, tag in zip(words, dl2ld(tags))]
                for words, tags in zip(b_words, dl2ld(b_tags))]

    def tag2str(self, tag, ignored_heads=None):
        str_dict = {k: self._heads[k].tag2str(t) for k, t in tag.items()}

        ignored_heads = set() if ignored_heads is None else ignored_heads
        for head in ignored_heads:
            if head in str_dict.keys():
                del str_dict[head]

        r_str = f"({' | '.join([f'{k}: {v}' for k, v in str_dict.items() if v != ''])})"
        return r_str if r_str != "()" else ''

