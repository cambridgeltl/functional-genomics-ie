import json

import torch

from transformers import AutoTokenizer

from src.dataloading import load_txt_data, load_raw_json_data
from src.datahandler import DataHandler
from src.model import Custom_Model
from src.custom_datatypes import deep_eD

from util.core import printv, get_time_stamp, ensure_file_ext, pairs

# Note:
# For clarity tags will refer to the actual tags on the data e.g. "PAD" and label will
# refer to the tensor used for the machine learning e.g. [0] or [0, 1, 1, 0]
# Essentially: Tag -> Human representation, Label -> Machine representation


class ModelHandler:

    def __init__(self, config):
        v = config.get("VERBOSE", 0) >= 1
        self.config = config

        printv(f"[I|Model] Loading Tokenizer", verbose_flag=v)
        tknizer_model = config.get("TOKENIZER_MODEL", config["TRANSFORMER_MODEL"])
        tokenizer = AutoTokenizer.from_pretrained(tknizer_model,
                                                       **config.get("TOKENIZER_KWARGS", {}))

        # To neatly hold all our data
        self.dh = DataHandler(tokenizer=tokenizer, max_token_length=config["MAX_TOKEN_LENGTH"])

        printv(f"[I|Model] Loading Model", verbose_flag=v)
        self.model = Custom_Model(config, self.dh.max_token_length)
        self.model.cuda_setup()

        # Bit hacky but helps for some deploy stuff
        self.extra_models = {}

        # For when we need to label entry inputs, use this dict
        self.entry_names = None

    @classmethod
    def get(cls, config):
        if config["TYPE"] == "pretrained":
            return cls(config)
        elif config["TYPE"] == "existing":
            mh = cls.load(config["PATH"])
            mh.extra_models = {k: cls.load(p).model
                               for k, p in config.get("EXTRA_MODELS", {}).items()}
            return mh
        else:
            raise Exception("[UE] Model type error not caught")

    @staticmethod
    def load(path):
        mh = torch.load(ensure_file_ext(path, "pkl"), map_location=torch.device('cpu'))
        mh.model.cuda_setup()
        return mh

    def save(self, name):
        torch.save(self, f"outputs/models/{name}.pkl")

    def reset_model(self, preserve_tag_list=True):
        tag_list = self.model.tag_list
        self.model = Custom_Model(self.config, self.dh.max_token_length)
        self.model.cuda_setup()

        if preserve_tag_list:
            self.model.tag_list = tag_list

    # Takes data from a source and fills input_ids, tags and tag_list
    def get_file_data(self, config):

        v_num = config.get("VERBOSE", 0)
        v1 = v_num >= 1
        v2 = v_num >= 2

        if not self.dh.is_empty:
            print("[W] Data handler was not empty, resetting it")
            self.dh.reset()
            assert self.dh.is_empty

        printv(f"[I|Data] Loading data from file", verbose_flag=v1)
        if config["FILETYPE"] == "json_fgeom":
            sep_sentences = config.get("SEP_SENTENCES", False)
            input_data, tag_data = self.model.load_fgeom_json_data(path=config["PATH"],
                                                            sep_sentences=sep_sentences)
        elif config["FILETYPE"] == "txt":
            input_data, tag_data = load_txt_data(config["PATH"])

        elif config["FILETYPE"] == "json_raw":
            input_data, tag_data, entry_idxs = load_raw_json_data(config["PATH"])
            self.entry_names = entry_idxs

        else:
            raise Exception(f"Unrecognised filetype {config['FILETYPE']} in config")

        printv(f"[I|Data] Pre-processing input data", verbose_flag=v1)
        input_data = self.model.pre_process_input_data(input_data)

        printv(f"[I|Data] Processing transformer data", verbose_flag=v1)
        self.dh.set_single_text_data(input_data["tfm"])

        if tag_data is not None:

            printv(f"[I|Data] Processing tag data", verbose_flag=v1)
            self.dh.set_tag_data(self.model, tag_data, input_data["head"],
                            config.get("BALANCE_CLASSES", 0))

            printv(f"[I|Data] Tag list: {self.model.tag_list}", verbose_flag=v2)
            printv(f"[I|Data] Tag weights: {self.dh.class_loss_weights}", verbose_flag=v2)

        else:
            printv("[I|Data] No tag data found", verbose_flag=v2)


    def train(self, train_dataloader, val_dataloader, config):
        if "CUSTOM_PS2LS" in config.keys():
            self.model.set_custom_ps2ls(config["CUSTOM_PS2LS"])
        return self.model.train_model(train_dataloader, val_dataloader,
                                      config, self.dh.class_loss_weights)

    def test(self, test_dataloader, config):

        v1 = config.get("VERBOSE", 0) >= 1
        printv("[I|Test] Testing model", verbose_flag=v1)

        if "CUSTOM_PS2LS" in config.keys():
            self.model.set_custom_ps2ls(config["CUSTOM_PS2LS"])

        loss, accuracy = self.model.validate(test_dataloader, self.dh.class_loss_weights)
        loss = loss / len(test_dataloader)

        printv(f"[I|Test] Test loss: {loss}", verbose_flag=v1)
        printv(f"[I|Test] Test accuracy: {accuracy}", verbose_flag=v1)

        return loss, accuracy


    def deploy_mode(self, config):
        v1 = config["DEPLOY"].get("VERBOSE", 0) >= 1
        v2 = config["DEPLOY"].get("VERBOSE", 0) >= 2
        link_mode = "LINK" in config["DEPLOY"]

        if "EXISTING_OUTPUT_FOLDER" in config["DATA"]:
            folder = config["DATA"]["EXISTING_OUTPUT_FOLDER"]
            printv(f"[I|DEPLOY] Using existing data from {folder}", verbose_flag=v1)

            printv(f"[I|DEPLOY] Loading tag output", verbose_flag=v1)
            with open(f"{folder}/b_word_tag_pairs.json") as f:
                b_word_tag_pairs = json.load(f)

            with open(f"{folder}/tag_entry_names.json") as f:
                self.entry_names = json.load(f)

            if link_mode:
                if "link" not in self.extra_models.keys():
                    raise Exception("Link prediction is in deploy config but there was no link model")

                link_model = self.extra_models["link"]

                printv(f"[I|DEPLOY] Loading link output", verbose_flag=v1)
                with open(f"{folder}/b_word_link_pairs.json") as f:
                    b_word_link_pairs = json.load(f)

            else:
                link_model = None
                b_word_link_pairs = None

        else:
            printv("[I|Deploy] Loading tag data", verbose_flag=v1)
            self.get_file_data(config["DATA"])
            d_dataloader = self.dh.get_dataloader(batch_size=config["DATA"]["BATCH_SIZE"])

            # TODO: Make this function with multi-input / make less hacky
            raw_texts = self.dh._text_data["default"]["raw_texts"]

            printv("[I|Deploy] Predicting tags", verbose_flag=v1)
            b_tags = self.model.predict_tags(d_dataloader, verbose_flag=v2)

            printv("[I|Deploy] Generating tag output", verbose_flag=v1)
            b_word_tag_pairs = self.model.get_word_tag_pairs(raw_texts, b_tags)

            if link_mode:
                printv("[I|Deploy] Loading link data", verbose_flag=v1)
                if "link" not in self.extra_models.keys():
                    raise Exception("Link prediction is in deploy config but there was no link model")

                link_model = self.extra_models["link"]
                active_tkn_idxs = self.model.get_tagged_word_idxs(b_tags)

                # This code is very hacky and should almost certainly be rewritten
                # Essentially taking the words which are marked as to get links for
                # And then accounting for the tokenization and max input length
                # This is also written to match a specific model and will easily break with other setups
                tkns_per_word = self.dh._text_data["default"]["n_tkns_per_word"]
                active_tkn_idxs = [[i in idxs for i in range(link_model.max_input_length)]
                                   for idxs in active_tkn_idxs]
                active_tkn_idxs = [[i for idx, n in zip(idxs, tkns_per_tag) for i in [idx]*n]
                                    for idxs, tkns_per_tag in zip(active_tkn_idxs, tkns_per_word)]
                active_tkn_idxs = [[entry[i] if i < len(entry) else False
                                    for i in range(link_model.max_input_length)]
                                   for entry in active_tkn_idxs]
                extra_model_data = {"heads": {k: {"extra_inputs":
                                                  {"active_tkn_idxs": {"all": active_tkn_idxs}}}
                                              for k in link_model._heads.keys()}}

                self.dh.update_model_data(extra_model_data)
                l_dataloader = self.dh.get_dataloader(batch_size=config["DATA"]["BATCH_SIZE"])

                printv("[I|Deploy] Predicting links", verbose_flag=v1)
                b_link_tags = link_model.predict_tags(l_dataloader, verbose_flag=v2)

                printv("[I|Deploy] Generating link output", verbose_flag=v1)
                b_word_link_pairs = link_model.get_word_tag_pairs(raw_texts, b_link_tags)

            else:
                b_word_link_pairs = None
                link_model = None

            if "SAVE_MODEL_OUTPUT_FOLDER" in config["DEPLOY"]:
                folder = config["DEPLOY"]["SAVE_MODEL_OUTPUT_FOLDER"]
                printv("[I|Deploy] Saving intermediate output", verbose_flag=v1)

                with open(f"{folder}/b_word_tag_pairs.json", 'w', encoding="utf-8") as f:
                    json.dump(b_word_tag_pairs, f, ensure_ascii=False, indent=4)

                if not hasattr(self, "entry_names"):
                    self.entry_names = None

                with open(f"{folder}/tag_entry_names.json", 'w', encoding="utf-8") as f:
                    json.dump(self.entry_names, f, ensure_ascii=False, indent=4)

                if link_mode:
                    with open(f"{folder}/b_word_link_pairs.json", 'w', encoding="utf-8") as f:
                        json.dump(b_word_link_pairs, f, ensure_ascii=False, indent=4)

        self.deploy_output(config["DEPLOY"], b_word_tag_pairs, b_word_link_pairs, link_model,
                           verbose=v1)

    def deploy_output(self, config, b_word_tag_pairs, b_word_link_pairs=None, link_model=None,
                      verbose=False):
        ignored_heads = config.get("IGNORED_HEADS", None)
        specific_head = config.get("SPECIFIC_HEAD", None)
        output_type = config["OUTPUT"]

        assert (b_word_link_pairs is None) == (link_model is None)

        if link_model is not None:
            link_ignored_heads = config["LINK"].get("IGNORED_HEADS", None)
            specific_link_head = config["LINK"].get("SPECIFIC_HEAD", None)
            b_word_data_pairs = [[(w, (t, b_word_link_pairs[i][j][1]))
                                  for j, (w, t) in enumerate(entry)]
                                 for i, entry in enumerate(b_word_tag_pairs)]

        if output_type in ["print", "txt"]:
            printv("[I|Deploy] Processing output", verbose_flag=verbose)
            w_sep, e_sep = ("\n", "\n\n") if config.get("NEWLINE_WORDS", False) else (" ", "\n")

            if link_model is not None:
                entry_txts = [w_sep.join([f"{str(w)} {self.model.tag2str(t, ignored_heads)} {link_model.tag2str(l, ['link_same_tag_only'])}"
                                          if t != "" else w for w, (t, l) in wtps])
                              for wtps in b_word_data_pairs]
            else:
                entry_txts = [w_sep.join([f"{str(w)} {self.model.tag2str(t, ignored_heads)}"
                                          if t != "" else w for w, t in wtps])
                              for wtps in b_word_tag_pairs]

            if hasattr(self, "entry_names") and self.entry_names is not None:
                for n, i in self.entry_names.items():
                    entry_txts[i] = f"{n}:\n{entry_txts[i]}"

            output_str = e_sep.join(entry_txts)

            printv("[I|Deploy] Outputting", verbose_flag=verbose)
            if config["OUTPUT"] == "print":
                print(output_str)

            elif output_type == "txt":
                with open(config.get("PATH", "model_output.txt"), 'w') as f:
                    f.write(output_str)

            else:
                raise Exception("Bad code - make sure all options in this branch are covered")

        elif output_type == "json":
            printv("[I|Deploy] Processing output", verbose_flag=verbose)
            if self.entry_names is None:
                raise Exception("To output as json you need named entries, try using json input")

            b_word_tag_pairs = self.model.clean_word_tag_pairs(b_word_tag_pairs, ignored_heads,
                                                               specific_head)

            if link_model is not None:
                # This applies the general link cleaning
                b_word_link_pairs = link_model.clean_word_tag_pairs(b_word_link_pairs,
                                                                    link_ignored_heads,
                                                                    specific_link_head)
                # This is a specific clean that ought to be refactored nicely into the general one
                pass

            result_obj = []

            for n, i in self.entry_names.items():
                entry_obj = {"PMID": n, "TEXT": ' '.join(w for w, _ in b_word_tag_pairs[i])}
                entry_obj["TAG_DATA"] = [f"{j}, {w} {t}"
                                         for j, (w, t) in enumerate(b_word_tag_pairs[i])
                                         if t is not None]

                if link_model is not None:
                    entry_obj["LINK_DATA"] = [f"{j}, {w} {l}"
                                              for j, (w, l) in enumerate(b_word_link_pairs[i])
                                              if l is not None]

                    # Get a dict of link ids and have vals be lists of word indices
                    link_group_word_idxs = {}
                    for j, (_, ls) in enumerate(b_word_link_pairs[i]):
                        if ls is not None:
                            for l in ls:
                                if l in link_group_word_idxs.keys():
                                    if j not in link_group_word_idxs[l]:
                                        link_group_word_idxs[l].append(j)
                                else:
                                    link_group_word_idxs[l] = [j]

                    entry_obj["LINK_WORD_GROUPS"] = list(link_group_word_idxs.values())

                    # Get the tags from the words and return the sets of linked tags
                    raw_linked_tags = []
                    for idxs in link_group_word_idxs.values():
                        tags = []

                        for idx in idxs:
                            word, tag = b_word_tag_pairs[i][idx]
                            if tag is not None:
                                # The [2:] removes the Schema (Hacky yes, should be done properly)
                                word_tags = [(k, v[2:]) for k, v in tag.items()]
                                for (tt1, tv1) in word_tags:
                                    present = False
                                    for (_, tt2, tv2) in tags:
                                        if tt1 == tt2 and tv1 == tv2:
                                            present = True
                                            break
                                    if not present:
                                        tags.append((word, tt1,tv1))

                        raw_linked_tags.append(tags)

                    entry_obj["LINKED_TAGS_RAW"] = raw_linked_tags

                    # Convert the groups of linked tags into pairs of linked head outputs
                    linked_tags = []
                    for lset in raw_linked_tags:

                        for ((w1, k1, v1), (w2, k2, v2)) in pairs(lset):
                            if k1 != k2:
                                pair_dict = {k1: {"val": v1, "words": [w1]},
                                             k2: {"val": v2, "words": [w2]}}

                                present = False
                                for j, existing_pair_dict in enumerate(linked_tags):
                                    ((ek1, d1), (ek2, d2)) = existing_pair_dict.items()

                                    ev1 = d1["val"]
                                    ev2 = d2["val"]

                                    if all([ek1==k1, ek2==k2, ev1==v1, ev2==v2]):
                                        present = True
                                        if w1 not in linked_tags[j][ek1]["words"]:
                                            linked_tags[j][ek1]["words"].append(w1)
                                        if w2 not in linked_tags[j][ek2]["words"]:
                                            linked_tags[j][ek2]["words"].append(w2)
                                    if all([ek1==k2, ek2==k1, ev1==v2, ev2==v1]):
                                        present = True
                                        if w2 not in linked_tags[j][ek1]["words"]:
                                            linked_tags[j][ek1]["words"].append(w2)
                                        if w1 not in linked_tags[j][ek2]["words"]:
                                            linked_tags[j][ek2]["words"].append(w1)

                                if not present:
                                    linked_tags.append(pair_dict)

                    # Filter if we are looking for specific combinations
                    if "LINKED_TAGS_PAIRS" in config["LINK"]:
                        ltps = config["LINK"]["LINKED_TAGS_PAIRS"]
                        new_linked_tags = []
                        for pair_dict in linked_tags:
                            ((k1, _), (k2, _)) = pair_dict.items()
                            for (ltp1, ltp2) in ltps:
                                if (k1 == ltp1 and k2 == ltp2) or (k1 == ltp2 and k2 == ltp1):
                                    new_linked_tags.append(pair_dict)
                                    break
                        linked_tags = new_linked_tags

                    entry_obj["LINKED_TAGS"] = linked_tags

                if "JSON_FIELDS" in config:
                    keys_to_write = config["JSON_FIELDS"]
                    entry_obj = {k: v for k, v in entry_obj.items() if k in keys_to_write}

                result_obj.append(entry_obj)

            printv("[I|Deploy] Outputting", verbose_flag=verbose)
            with open(config.get("PATH", "model_output.json"),
                      'w', encoding="utf-8") as f:
                json.dump(result_obj, f, ensure_ascii=False, indent=4)

        else:
            raise Exception(f"Unrecognised output type {config['OUTPUT']}")


    def train_mode(self, config):
        v1 = config["TRAINING"].get("VERBOSE", 0) >= 1
        k = config["TRAINING"].get("K_FOLDS", 0)
        bs = config["DATA"]["BATCH_SIZE"]
        self.get_file_data(config["DATA"])

        printv("[I|Train Handler] Training model", verbose_flag=v1)
        if k > 0:
            dataloader_pairs = self.dh.get_k_fold_dataloaders(k=k, batch_size=bs)

            histories = []
            for i, d_loaders in enumerate(dataloader_pairs):

                printv(f"[I|Train Handler] Fold {i+1}/{k}...", verbose_flag=v1)
                histories.append(self.train(*d_loaders, config=config["TRAINING"]))

                printv("[I|Train Handler] Resetting model", verbose_flag=v1)
                self.reset_model()

            # Average fold training for history
            history = deep_eD(histories[0])
            for h in histories[1:]:
                history = history.combine(deep_eD(h))
            history = history.div(len(histories))

            if config["TRAINING"].get("DO_FINAL_TRAIN", True):
                printv(f"[I|Train Handler] Final training", verbose_flag=v1)
                final_dataloader = self.dh.get_dataloader(batch_size=bs)
                final_history = self.train(final_dataloader, None, config=config["TRAINING"])
                history["train_losses"] = final_history["train_losses"]

            # Add back in our k-fold specific values just for verification / interest purposes
            history["k_fold_train_individual_histories"] = histories

        else:
            dataloaders = self.dh.get_tr_val_dataloaders(batch_size=bs)
            history = self.train(*dataloaders, config=config["TRAINING"])

        # Get dict we will save now so we can add to it if testing
        db_path = "./outputs/outputs_db.json"
        with open(db_path) as f:
            outputs_db = json.load(f)

        name = f"{config['TRAINING']['TRAINED_NAME']}_{get_time_stamp()}"
        outputs_db[name] = {
            "model_path": f"./outputs/models/{name}",
            "training_config": config,
            "history": history
        }

        printv("[I|Train Handler] Testing model", verbose_flag=v1)
        if "TESTING" in config:
            self.dh.reset()
            self.get_file_data(config["TEST_DATA"])
            test_dataloader = self.dh.get_dataloader(batch_size=config["TEST_DATA"]["BATCH_SIZE"])
            t_loss, t_accuracy = self.test(test_dataloader, config["TESTING"])
            outputs_db[name]["testing"] = {"loss": t_loss, "accuracy": t_accuracy}

        printv("[I|Train Handler] Saving model", verbose_flag=v1)
        self.save(name)

        printv("[I|Train Handler] Saving training history", verbose_flag=v1)
        with open(db_path, 'w', encoding="utf-8") as f:
            json.dump(outputs_db, f, ensure_ascii=False, indent=4)


    def test_mode(self, config):
        self.get_file_data(config["DATA"])
        d_loader = self.dh.get_dataloader(batch_size=config["DATA"]["BATCH_SIZE"])
        self.test(d_loader, config["TESTING"])

