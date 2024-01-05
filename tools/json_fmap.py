import json
import argparse
import copy


def pa_effect_pairs(json_obj):

    def keep_specific_tag_pairs(in_dict, pairs):
        assert all(len(x) == 2 for x in pairs)

        def matching(present_keys):
            assert len(present_keys) == 2

            for p1, p2 in pairs:
                if (p1 in present_keys) and (p2 in present_keys):
                    return True

            return False

        out_dict = copy.deepcopy(in_dict)
        out_dict["LINKED_TAGS"] = [pair_dict for pair_dict in out_dict["LINKED_TAGS"]
                                   if matching(pair_dict.keys())]
        return out_dict

    return [keep_specific_tag_pairs(entry, [("effect", "perturbing_action")]) for entry in json_obj]


def filter_empty_linked_tags(json_obj):
    return [entry for entry in json_obj
            if entry["LINKED_TAGS"] != []]

def filter_data_fields(json_obj):
    black_list = ["TAG_DATA", "LINK_DATA"]
    return [{k: v for k, v in entry.items() if k not in black_list}
            for entry in json_obj]


arg_func_map = {
    "pa_effect_pairs": pa_effect_pairs,
    "filter_empty_linked_tags": filter_empty_linked_tags,
    "filter_data_fields": filter_data_fields
}


def main(args):
    with open(args.inp) as f:
        json_obj = json.load(f)

    for func in args.funcs:
        json_obj = arg_func_map[func](json_obj)

    with open(args.out, 'w', encoding='utf-8') as f:
        json.dump(json_obj, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Map functions over json files")
    parser.add_argument("inp", help="Name of input json file")
    parser.add_argument("funcs", nargs="+",
                        help=f"Function to use, current options: {', '.join(arg_func_map.keys())}")
    parser.add_argument("out", help="Name of output json file")

    main(parser.parse_args())

