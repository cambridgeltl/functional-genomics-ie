import json
import argparse


from src.misc import asymetric_split, shuffle_items
from util.core import ensure_file_ext


def main(args):

    i_path = ensure_file_ext(args.db, "json")
    o_folder = args.folder + "/" if args.folder[-1] != "/" else args.folder

    # Checking things...
    try:
        name_weight_pairs = [(x, float(y)) for x, y in zip(args.names_and_weights[::2],
                                                           args.names_and_weights[1::2])]
    except ValueError:
        raise Exception(f"Bad value for weight in name_weight_pairs {args.name_weight_pairs}")

    if len(name_weight_pairs) < 2:
        raise Exception(f"Not enough names and weights given (need 2+), only found {name_weight_pairs}")


    w_sum = sum(x for _, x in name_weight_pairs)
    name_weight_pairs = [(x, y/w_sum) for x, y in name_weight_pairs]
    name_lead_frac_pairs = []
    added_weights = []
    for name, weight in name_weight_pairs:
        name_lead_frac_pairs.append((name, weight / (1-sum(added_weights))))
        added_weights.append(weight)

    with open(i_path) as f:
        inp_data = [(x, y) for x, y in json.load(f).items()]

    if args.random:
        inp_data, = shuffle_items(inp_data)

    name_entries_pairs = []
    for name, lf in name_lead_frac_pairs[:-1]:
        (entry_data,), (inp_data,) = asymetric_split(inp_data, leading_fraction=lf)
        name_entries_pairs.append((name, entry_data))
    name_entries_pairs.append((name_lead_frac_pairs[-1][0], inp_data))

    for name, entries in name_entries_pairs:
        fpath = o_folder + ensure_file_ext(name, "json")
        with open(fpath, 'w', encoding="utf-8") as f:
            json.dump({k: v for k, v in entries}, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Split up a json database")
    parser.add_argument("db", help="Source database file")
    parser.add_argument("-r", "--random", action="store_true", default=False,
                        help="Whether to randomise splitting")
    parser.add_argument("names_and_weights", nargs='+',
                        help="A file name followed by a weight for the amount of the source db to go into this one, e.g. db_1 0.4 db_2 0.35 db_3 0.25")
    parser.add_argument("-f", "--folder", default="./",
                        help="Folder for output databases")
    main(parser.parse_args())

