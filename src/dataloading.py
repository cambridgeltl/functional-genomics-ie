import pandas as pd
import numpy as np
import json

from util.core import list_of_dicts_to_dict_of_lists as ld2dl


def ld2dl2(x):
    return ld2dl([ld2dl(y) for y in x])


def get_fgeom_tags(word_data, tag_categories):
    category_tags = [(k, t["schema"]) for k in tag_categories.keys() for t in word_data[k]]
    field_categories = {k: v for v, fields in tag_categories.items() for k in fields}
    tags = {k: [(t[k], t["schema"]) for t in word_data[v]] for k, v in field_categories.items()}
    tags["category"] = category_tags
    return tags


def get_single_label_tag(tags, tag_counts):
    tag_counts.append((None, 0.5))
    tags = [t for t, _ in tag_counts]
    counts = [x for _, x in tag_counts]
    return tags[np.argmax(counts)]


def link_set_name(field, value):
    return f"{field}|{'_'.join(value.split(' '))}"


def get_fgeom_links(entry_data, tag_categories):
    def get_ids_for_word(ws):
        links = []
        for c, fs in tag_categories.items():
            for tag in ws[c]:
                links.extend([("links", l_id, "linked") for l_id in tag["link_ids"]])
                for f in fs:
                    links.append((link_set_name(f,tag[f]), tag["id"], "linked"))
        return links

    return [get_ids_for_word(word) for word in entry_data]


def load_fgeom_json_data(path, heads, raw_tag_categories, sep_sentences=False):
    # heads should be of form (Name, Type), e.g. (category, single_label)

    if sep_sentences:
        raise Exception("Currently unsupported with new dataloader")

    with open(path) as f:
        entries = list(json.load(f).values())

    tag_categories = {k: list(v["fields"].keys()) for k, v in raw_tag_categories.items()}

    words = [[word_data["WORD"] for word_data in entry] for entry in entries]
    input_data = {"tfm": words, "head": {}}

    def process_tags(tag_schema_pairs, multilabel, schema_func):
        if schema_func is not None:
            tags = [f"{schema_func(s)}-{t}" for t, s in tag_schema_pairs]
        else:
            tags = [t for t, _ in tag_schema_pairs]
        t_set = list(set(tags))
        tag_counts = [(t, tags.count(t)) for t in t_set]
        return t_set if multilabel else get_single_label_tag(tags, tag_counts)

    raw_tag_data = ld2dl2([[get_fgeom_tags(word_data, tag_categories) for word_data in entry]
                           for entry in entries])
    tag_data = {}  # {head: tags}

    for k, h_type, schema_func in heads:
        if k in raw_tag_data.keys():
            multilabel = h_type == "multi_label"
            tag_data[k] = [[process_tags(x, multilabel, schema_func) for x in xs]
                           for xs in raw_tag_data[k]]
        elif h_type == "link":
            raw_link_data = [get_fgeom_links(entry, tag_categories) for entry in entries]
            if k == "link_all":
                link_data = {"all": [[[(l_id, l) for _, l_id, l in x] for x in xs]
                                     for xs in raw_link_data]}
            elif k == "link_same_tag_and_link":
                link_data = {"all": [[[(l_id, "link" if l_type == "links" else "same_tag")
                                       for l_type, l_id, _ in x] for x in xs]
                                     for xs in raw_link_data]}
            elif k == "link_only":
                link_data = {"all": [[[(l_id, "linked")
                                       for l_type, l_id, _ in x if l_type == "links"] for x in xs]
                                     for xs in raw_link_data]}
            elif k == "link_same_tag_only":
                link_data = {"all": [[[(l_id, "linked")
                                       for l_type, l_id, _ in x if l_type != "links"] for x in xs]
                                     for xs in raw_link_data]}
            elif k == "link_same_tag_only_split":
                link_sets = set([l_type for xs in raw_link_data for x in xs
                                 for l_type, _, _ in x if l_type != "links"])
                link_data = {k: [[[] for _ in xs] for xs in raw_link_data] for k in link_sets}
                for i, xs in enumerate(raw_link_data):
                    for j, x in enumerate(xs):
                        for l_type, l_id, l in x:
                            link_data[l_type][i][j].append((l_id, l))
            else:
                raise Exception("Unsupported link head name")
            tag_data[k] = link_data
            linked_tkn_idxs = {k: [[x != [] for x in xs] for xs in xss]
                               for k, xss in link_data.items()}
            input_data["head"][k] = {"active_tkn_idxs": linked_tkn_idxs}

    assert len(heads) == len(tag_data.keys())
    return input_data, tag_data


def load_csv_data(path):
    # Helper function to extract data from pandas dataframe
    def process_sentence_data(s):
        return [(w, t) for w, t in zip(s["Word"].values.tolist(),
                                       s["Tag"].values.tolist())]

    data = pd.read_csv(path, encoding="latin1").fillna(method="ffill")
    return list(data.groupby("Sentence #").apply(process_sentence_data))


def load_txt_data(path):
    with open(path, 'r') as f:
        entries = f.read().split('\n')
    words = [entry.split(' ') for entry in entries if entry != '']
    return {"tfm": words, "head": {}}, None

def load_raw_json_data(path):
    with open(path) as f:
        entries = json.load(f)
    pairs = list(entries.items())
    words = [entry_txt.split(' ') for _, entry_txt in pairs]
    entry_idxs = {k: i for i, (k, _) in enumerate(pairs)}
    return {"tfm": words, "head": {}}, None, entry_idxs

