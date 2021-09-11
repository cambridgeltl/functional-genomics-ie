import json
import argparse


if __name__ == "__main__":

    # CLI
    parser = argparse.ArgumentParser(description="Combine two or more json databases")
    parser.add_argument("dbs", nargs='+', help="Paths to json database files")
    parser.add_argument("-n", "--name", default=None, help="Name of output file")
    args = parser.parse_args()

    output_path = args.name + ".json" if args.name.split('.')[-1] != "json" else args.name

    new_db = {}

    for db_path in args.dbs:
        with open(db_path) as f:
            data = json.load(f)
        new_db.update(data)

    with open(output_path, 'w', encoding="utf-8") as f:
        json.dump(new_db, f, ensure_ascii=False, indent=4)

