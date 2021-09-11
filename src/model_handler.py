import numpy as np
import json

import torch

from transformers import AutoTokenizer

from src.misc import pad_sequences
from src.dataloading import load_txt_data
from src.datahandler import DataHandler
from src.model import Custom_Model
from src.custom_datatypes import deep_eD

from util.core import printv, get_time_stamp, ensure_file_ext

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

    @classmethod
    def get(cls, config):
        if config["TYPE"] == "pretrained":
            return cls(config)
        elif config["TYPE"] == "existing":
            mh = cls.load(config["PATH"])
            mh.extra_models = {k: cls.load(p).model
                               for k, p in config.get("EXTRA_PATHS", {}).items()}
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
        self.get_file_data(config["DATA"])
        d_dataloader = self.dh.get_dataloader(batch_size=config["DATA"]["BATCH_SIZE"])

        v1 = config["DEPLOY"].get("VERBOSE", 0) >= 1

        printv("[I|Deploy] Predicting tags", verbose_flag=v1)
        b_tags = self.model.predict_tags(d_dataloader)

        if config["DEPLOY"].get("LINK", False):
            # assert "link" in self.extra_models.keys()
            active_tkn_idxs = self.model.get_tagged_word_idxs(b_tags)
            print(active_tkn_idxs)

        printv("[I|Deploy] Generating output", verbose_flag=v1)
        ignored_heads = config["DEPLOY"].get("IGNORED_HEADS", None)

        # TODO: Make this function with multi-input / make less hacky
        b_word_tag_pairs = self.model.get_word_tag_pairs(
            self.dh._text_data["default"]["raw_texts"], b_tags, ignored_heads=ignored_heads)

        w_sep, e_sep = ("\n", "\n\n") if config["DEPLOY"].get("NEWLINE_WORDS", False) else (" ", "\n")
        output_str = e_sep.join([w_sep.join([f"{w} {t}" if t != "" else w for w, t in wtps])
                                 for wtps in b_word_tag_pairs])

        printv("[I|Deploy] Outputting", verbose_flag=v1)
        if config["DEPLOY"]["OUTPUT"] == "print":
            print(output_str)

        elif config["DEPLOY"]["OUTPUT"] == "txt":
            with open(config["DEPLOY"].get("PATH", "model_output.txt"), 'w') as f:
                f.write(output_str)

        else:
            raise Exception(f"Unrecognised output type {config['DEPLOY']['OUTPUT']}")


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

