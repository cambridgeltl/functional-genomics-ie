import json
import argparse

from util.core import ensure_file_ext


def main(args):

    i_path = ensure_file_ext(args.db, "json")
    o_path = ensure_file_ext(args.name, "json")

    with open(i_path) as f:
        inp_data = [(x, y) for x, y in json.load(f).items()]

    assert len(inp_data) >= args.num
    entries = [x for x, _ in zip(inp_data, range(args.num))]

    with open(o_path, 'w', encoding="utf-8") as f:
        json.dump({k: v for k, v in entries}, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Split up a json database")
    parser.add_argument("db", help="Source database file")
    parser.add_argument("num", type=int, help="Number of entries to use")
    parser.add_argument("name", help="Name / path of output file")
    main(parser.parse_args())

