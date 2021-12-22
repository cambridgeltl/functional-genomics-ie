import json
import argparse

from util.core import ensure_file_ext


def main(args):

    i_path = ensure_file_ext(args.txt, "txt")

    if args.name is not None:
        o_path = ensure_file_ext(args.name, "json")
    else:
        o_path = i_path.split('.')[0] + ".json"

    with open(i_path) as f:
        in_txt = f.read()

    entries = in_txt.split('\n\n')
    pairs = [x.split('\n') for x in entries]

    out_dict = {x[0]: x[1] for x in pairs if len(x) == 2}

    print(f"{len(out_dict)} items stored")

    with open(o_path, 'w', encoding="utf-8") as f:
        json.dump(out_dict, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Convert a txt file into a json dict. Files should be organised in pairs of lines with empty lines in between. First line in the pair becomes the key and the second the value of the resulting dictionary entries")
    parser.add_argument("txt", help="Source text file name")
    parser.add_argument("-n", "--name", default=None, help="Output json file name")
    main(parser.parse_args())

