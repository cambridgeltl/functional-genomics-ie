import numpy as np

from torch.utils.data import RandomSampler

from src.misc import shuffle_items, asymetric_split, get_n_folds, dataloader, pad_sequences
from src.model import Custom_Model
from util.core import limit_seq_sum

class DataHandler:
    def __init__(self, tokenizer=None, max_token_length=None):
        self.tokenizer = tokenizer
        self.max_token_length = max_token_length
        self.class_loss_weights = None

        # Commented out things are examples

        # This is data that goes into dataloaders and should be well behaved (padded)
        # Batches in forward methods will be batches of this
        # ntpw is just a padded version of n_tkns_per_word in self._text_data
        self._model_data = {

            # Can contain keys for certain heads
            # These can be their own input or a dict of different inputs
            # Each input will have the same keys as default
            "tfm": {
#               "default": {
#                   "iids": None,
#                   "ntpw": None,
#                   "masks": None
#               },
#               "single_input_head_2: {
#                   "input_1": {
#                       "iids": None,
#                       "ntpw": None,
#                       "masks": None
#                   }
#               },
#               "multi_input_head_1": {
#                   "input_1": {
#                       "iids": None,
#                       "ntpw": None,
#                       "masks": None
#                   },
#                   "input_2": {
#                       "iids": None,
#                       "ntpw": None,
#                       "masks": None
#                   }
#               }
            },

            # Will contain a dict of head names and data
            # The data will be a dict with masks, labels and extra inputs
            # No defaults, each head has seperate data
            "heads": {
#               "single_input_head_1": {
#                   "labels": None,
#                   "extra_inputs": None,
#                   "masks": None
#               },
#               "single_input_head_2": {
#                   "input_1": {
#                       "labels": None,
#                       "extra_inputs": None,
#                       "masks": None
#                   }
#               },
#               "multi_input_head_1": {
#                   "input_1": {
#                       "labels": None,
#                       "extra_inputs": None,
#                       "masks": None
#                   },
#                   "input_1": {
#                       "labels": None,
#                       "extra_inputs": None,
#                       "masks": None
#                   }
#               }
            }
        }

        # This is data that is stored for use but does not go in dataloaders
        # Structure similar to self._model_data["tfm"]
        self._text_data = {
#           "default": {
#               "raw_texts": None,
#               "tokenized_texts": None,
#               "n_tkns_per_word": None
#           },
#           "single_input_head_2: {
#               "input_1": {
#                   "raw_texts": None,
#                   "tokenized_texts": None,
#                   "n_tkns_per_word": None
#               }
#           },
#           "multi_input_head_1": {
#               "input_1": {
#                   "raw_texts": None,
#                   "tokenized_texts": None,
#                   "n_tkns_per_word": None
#               },
#               "input_2": {
#                   "raw_texts": None,
#                   "tokenized_texts": None,
#                   "n_tkns_per_word": None
#               }
#           }
        }

    @property
    def is_empty(self):
        a = self.class_loss_weights is None
        b = self._model_data == {"tfm": {}, "heads": {}}
        c = self._text_data == {}
        return a and b and c

    def reset(self):
        self.class_loss_weights = None
        self._model_data = {"tfm": {}, "heads": {}}
        self._text_data = {}


    def set_tag_data(self, model: Custom_Model, tag_data, head_extra_inputs, loss_balance_mult):

        # The heads which work with multi-input data will process it as needed
        n_tkns_per_word = {kh: {ki: vi["n_tkns_per_word"] for ki, vi in vh.items()}
                           if kh != "default" else vh["n_tkns_per_word"]
                           for kh, vh in self._text_data.items()}
        tokenized_texts = {kh: {ki: vi["tokenized_texts"] for ki, vi in vh.items()}
                           if kh != "default" else vh["tokenized_texts"]
                           for kh, vh in self._text_data.items()}

        tags, head_extra_inputs = model.extend_data(n_tkns_per_word, tag_data, head_extra_inputs,
                                                    maxlen=self.max_token_length)

        # Should already be set via config file but this will check tags present in data
        model.tag_list = model.tag_list_from_tags(tag_data)

        labels_dict = model.tags2processed_labels(tags, tokenized_texts)
        masks_dict = model.get_loss_masks(labels_dict)

        self.class_loss_weights = model.get_label_weights(labels_dict, loss_balance_mult,
                                                          head_extra_inputs)

        head_data_dicts = model.form_head_data_dicts(labels_dict, head_extra_inputs, masks_dict)
        self._model_data["heads"] = {k: v for k, v in head_data_dicts.items()}


    def set_text_data(self, entry_texts_dict, heads=None, are_dicts=None):
        are_dicts = are_dicts if are_dicts is not None else set()
        heads = heads if heads is not None else {}

        for k in entry_texts_dict.keys():
            if k not in heads.keys():
                heads[k] = "default"

        for k, entry_texts in entry_texts_dict.items():
            is_dict = k in are_dicts
            self.set_single_text_data(entry_texts, head=heads[k], is_dict=is_dict)


    def set_single_text_data(self, entry_texts, head="default", is_dict=False):

        self._text_data[head] = {}

        def get_text_data(e_texts):
            tokenized_texts_and_n_tkns = [self._tokenize_entry(e) for e in e_texts]
            ts = [token for token, _ in tokenized_texts_and_n_tkns]
            ns = [n_tkns for _, n_tkns in tokenized_texts_and_n_tkns]
            return {"raw_texts": e_texts, "tokenized_texts": ts, "n_tkns_per_word": ns}

        if is_dict:
            assert head != "default"
            assert isinstance(entry_texts, dict)
            self._text_data[head] = {k: get_text_data(v) for k, v in entry_texts.items()}
        else:
            assert not isinstance(entry_texts, dict)
            self._text_data["default"] = get_text_data(entry_texts)

        self._load_single_tfm_data(head=head, is_dict=is_dict)


    def _load_single_tfm_data(self, head="default", is_dict=False):
        self._model_data["tfm"][head] = {}

        def get_iids_ntpw_masks(text_data):
            tokenized_texts = text_data["tokenized_texts"]
            n_tkns_per_word = text_data["n_tkns_per_word"]

            input_pad = 0
            input_ids = pad_sequences([self.tokenizer.convert_tokens_to_ids(tkns)
                                       for tkns in tokenized_texts],
                                      maxlen=self.max_token_length, value=input_pad, dtype=np.int_)

            iids = input_ids
            masks = [[float(i != input_pad) for i in ii] for ii in input_ids]

            _ntpw = [limit_seq_sum(x, self.max_token_length) for x in n_tkns_per_word]
            ntpw = pad_sequences(_ntpw, maxlen=self.max_token_length, value=0, dtype=np.int)

            return {"iids": iids, "ntpw": ntpw, "masks": masks}

        if is_dict:
            assert head != "default"
            t_data = self._text_data[head]
            assert set(t_data.keys()) != {"raw_texts", "tokenized_texts", "n_tkns_per_word"}
            self._model_data["tfm"][head] = {k: get_iids_ntpw_masks(v) for k, v in t_data.items()}
        else:
            t_data = self._text_data["default"]
            assert set(t_data.keys()) == {"raw_texts", "tokenized_texts", "n_tkns_per_word"}
            self._model_data["tfm"]["default"] = get_iids_ntpw_masks(t_data)


    def _tokenize_entry(self, entry_words):
        tokenized_entry = []
        tkns_per_tag = []  # So if we have tags on a token by token basis we can extend them

        for word in entry_words:
            tokenized_word = self.tokenizer.tokenize(word)
            tokenized_entry.extend(tokenized_word)
            tkns_per_tag.append(len(tokenized_word))

        return tokenized_entry, tkns_per_tag


    def get_dataloader(self, batch_size=1, sampler=None):
        return dataloader(self._model_data, batch_size=batch_size, sampler=sampler)


    def get_k_fold_dataloaders(self, batch_size=1, k=4):
        datasets = get_n_folds(self._model_data, n=k, shuffle=True, allow_dicts=True)
        return tuple([tuple([dataloader(*tr, batch_size=batch_size, sampler=RandomSampler),
                             dataloader(*val, batch_size=batch_size)])
                     for tr, val in datasets])


    def get_tr_val_dataloaders(self, batch_size=1, test_size=0.1):
        tr_set, val_set = asymetric_split(*shuffle_items(self._model_data, allow_dicts=True),
                                          leading_fraction=1-test_size, allow_dicts=True)
        return tuple([dataloader(*tr_set, batch_size=batch_size, sampler=RandomSampler),
                      dataloader(*val_set, batch_size=batch_size)])

