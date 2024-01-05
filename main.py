import os
import argparse
import json
import traceback

from datetime import datetime
from util.core import printv, ensure_file_ext
from src.model_handler import ModelHandler
from src.analysis import analyse_mode


def main(config_path):
    with open(config_path) as f:
        config = json.load(f)

    # Setting of global verbose
    global_v = config.get("VERBOSE", None)
    if global_v is not None:
        for sub_config in config.values():
            if isinstance(sub_config, dict) and "VERBOSE" not in sub_config.keys():
                sub_config["VERBOSE"] = global_v

    if config["MODE"] in {"train", "test", "deploy"}:
        model_handler = ModelHandler.get(config["MODEL"])
        mode_funcs = {
            "train": model_handler.train_mode,
            "test": model_handler.test_mode,
            "deploy": model_handler.deploy_mode
        }
    else:
        mode_funcs = {"analyse": analyse_mode}

    mode_funcs[config["MODE"]](config)


if __name__ == "__main__":
    # CLI Args
    # TODO: Add args for data folder, model folder, history folder and possibly more
    parser = argparse.ArgumentParser(description="CLI tool for training, testing and analysing bert models. If you get any unexpected errors ([UE]) then some code is wrong and there is a bug or logical error. If you get normal errors ([E]) then you have made a mistake.")
    parser.add_argument("config_paths", nargs='*',
                        help="Json config files that defines mode and parameters of operation")
    parser.add_argument("-f", "--config_folders", nargs='*',
                        help="Folders to run config files from, will try and run any .json file")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Execute verbosely")
    parser.add_argument("-r", "--recursive", action="store_true",
                        help="Search folders given via -f recursively")

    # Parse to get flags
    args = parser.parse_args()
    v = args.verbose
    r = args.recursive

    printv("[I] Program starting...", verbose_flag=v)
    printv(f"[T] {datetime.now()}", verbose_flag=v)

    if args.config_paths is None and args.config_folders is None:
        raise Exception("[E] No configs provided, see main.py -h")

    configs = args.config_paths[:]
    config_folders = args.config_folders

    def get_configs_from_folder(path):
        cfg_paths = []

        # Iterate through contents of folder
        for child in os.listdir(path):
            p = os.path.join(path, child)

            # If found a new folder, recurse
            if os.path.isdir(p) and r:
                cfg_paths.extend(get_configs_from_folder(p))

            # Else check it's json and add to paths
            elif child.split('.')[-1] == "json":
                cfg_paths.append(p)

        return cfg_paths

    if config_folders is not None:
        for config_folder in config_folders:
            configs.extend(get_configs_from_folder(config_folder))

    s_configs = []
    f_configs = []

    printv(f"[I] Found {len(configs)} configs:", verbose_flag=v)
    printv('\n'.join(configs), verbose_flag=v)

    for i, c in enumerate(configs):
        try:
            c = ensure_file_ext(c, "json")
            printv(f"[I] Loading config {i+1}/{len(configs)} {c}", verbose_flag=v)
            printv(f"[T] {datetime.now()}", verbose_flag=v)
            main(c)
        except Exception as e:
            print(f"[E] Got an error in config {c}:")
            traceback.print_exc()
            f_configs.append(c)
        else:
            s_configs.append(c)

    s_string = ', '.join(s_configs) if s_configs != [] else "None"
    f_string = ', '.join(f_configs) if f_configs != [] else "None"

    printv("[I] Finished", verbose_flag=v)
    printv(f"[I] Successful: {s_string}", verbose_flag=v)
    printv(f"[I] Failed: {f_string}", verbose_flag=v)
    printv(f"[T] {datetime.now()}", verbose_flag=v)
    printv("[I] Program exiting...", verbose_flag=v)

