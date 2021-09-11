import json
import argparse
import numpy as np

from util.core import ensure_file_ext


def r2(x):
    return round(x,2)


def category_tag_info(category_tags):
    return '\n'.join([f"* {tag_name.title()}: {tag_data['T']}, {tag_data['M']}, {r2(tag_data['A'])}"
                      for tag_name, tag_data in category_tags.items()])


def md_template(title, an_d):

    entry_info = '\n'.join([
        f"""**Title**:
{name},
Words: {en_d["WORDS"]},
Tokens: {en_d["TOKENS"]}\\
Tag data:
Total: {en_d["TOTAL_TAGS"]},
Unique: {en_d["UNIQUE_TAGS"]},
Max tags: {en_d["MAX_TAGS"]},
Tagged words: {en_d["TAGGED_WORDS"]} ({round(en_d["TAG_FRAC"]*100)}%),
Avg tags: {r2(en_d["AVG_TAGS"])},
MC words: {en_d["MULTI_CAT_WORDS"]}\\
Link data:
Total: {en_d["TOTAL_LINKS"]},
Unique: {en_d["UNIQUE_LINKS"]},
Max links (tag, word): ({en_d["MAX_LINKS_PER_TAG"]}, {en_d["MAX_LINKS_PER_WORD"]}),
Linked (tags, words): ({en_d["LINKED_TAGS"]} ({r2(en_d["LINK_TAG_FRAC"]*100)}%), {en_d["LINKED_WORDS"]} ({r2(en_d["LINK_WORD_FRAC"]*100)}%))\\
Avg links (tag, word): ({r2(en_d["AVG_TAG_LINKS"])}, {r2(en_d["AVG_WORD_LINKS"])}),
Schema counts (B, I, E, S): ({en_d["SCHEMA_B"]}, {en_d["SCHEMA_I"]}, {en_d["SCHEMA_E"]}, {en_d["SCHEMA_S"]})
"""
        for name, en_d in an_d["INDIVIDUAL_ENTRIES"].items()
    ])

    label_category_info = '\n'.join([f"""### {category_title.title()}

{category_tag_info(category_tags)}
""" for category_title, category_tags in an_d["LABELS"].items()])

    return f"""---
title: Rough Analysis of {title}
geometry: margin=2cm
---

# General Information

* Num. Entries: {an_d["NUM_ENTRIES"]}
* Tokenizer used: dmis-lab/biobert-v1.1

### Definitions:

* Words represent the number of entities that have been considered distinct during the proccess of assigning tags to part of the text, it is essentially the text split on spaces
* Tokens are the actual pieces of data going into the model, punctuation is split from words and some large words are split down into smaller parts
* Total tags is the total number of tags across all words (If two or more words are part of the same tag this counts as a tag for each word)
* Unique tags is the total number of tags that are unique (not part of same tag)
* Max tags is the most tags a single word has
* Tagged words is the number of words that have at least one tag
* Tagged words % is the percentage of words that are tagged, it's given in brackets for individual entries.
* Avg tags is the average number of tags per word that is tagged
* MC words is the number of words with tags across multiple categories
* Total links is the total number of links across all tags (If two or more tags are linked this counts as a link for each one)
* Unique links is the total number of links that are unique (not part of the same link)
* Max links is the most amount of links a single tag or word has associated with it
* Linked tags, words is the number of tags or words that have links
* Linked % tags, words is the percentage of tags or words with links
* Avg links per tag, word is the average number of links per tag or word
* The schema used is BIES as it is all encompassing and models can convert to a lower resolution if wanted (Beginning, Inner, End, Singleton)

## Sizes

* Average words: {an_d["WORDS"]["AVG"]}
* Maximum words: {an_d["WORDS"]["MAX"]}
* Minimum words: {an_d["WORDS"]["MIN"]}\\
* Average tokens: {an_d["TOKENS"]["AVG"]}
* Maximum tokens: {an_d["TOKENS"]["MAX"]}
* Minimum tokens: {an_d["TOKENS"]["MIN"]}\\
* Entries with over 512 tokens: {an_d["TOKENS"][">512"]}/{an_d["NUM_ENTRIES"]}, {r2((an_d["TOKENS"][">512"]/an_d["NUM_ENTRIES"])*100)}%


## Tags

### Maximums

* Total tags: {an_d["TAG_MAX"]["TOTAL_TAGS"]}
* Unique tags: {an_d["TAG_MAX"]["UNIQUE_TAGS"]}
* Max tags: {an_d["TAG_MAX"]["MAX_TAGS"]}
* Tagged words: {an_d["TAG_MAX"]["TAGGED_WORDS"]}
* Tagged words %: {r2(an_d["TAG_MAX"]["TAG_FRAC"]*100)}%
* Avg tags: {r2(an_d["TAG_MAX"]["AVG_TAGS"])}
* MC words: {an_d["TAG_MAX"]["MULTI_CAT_WORDS"]}

### Averages

* Total tags: {r2(an_d["TAG_AVG"]["TOTAL_TAGS"])}
* Unique tags: {r2(an_d["TAG_AVG"]["UNIQUE_TAGS"])}
* Max tags: {r2(an_d["TAG_AVG"]["MAX_TAGS"])}
* Tagged words: {r2(an_d["TAG_AVG"]["TAGGED_WORDS"])}
* Tagged words %: {r2(an_d["TAG_AVG"]["TAG_FRAC"]*100)}%
* Avg tags: {r2(an_d["TAG_AVG"]["AVG_TAGS"])}
* MC words: {r2(an_d["TAG_AVG"]["MULTI_CAT_WORDS"])}


## Links

### Maximums

* Total links: {an_d["LINK_MAX"]["TOTAL_LINKS"]}
* Unique links: {an_d["LINK_MAX"]["UNIQUE_LINKS"]}
* Max links per tag, word: {an_d["LINK_MAX"]["MAX_LINKS_PER_TAG"]}, {an_d["LINK_MAX"]["MAX_LINKS_PER_WORD"]}
* Linked tags, words: {an_d["LINK_MAX"]["LINKED_TAGS"]}, {an_d["LINK_MAX"]["LINKED_WORDS"]}
* Linked % tags, words: {r2(an_d["LINK_MAX"]["LINK_TAG_FRAC"]*100)}%, {r2(an_d["LINK_MAX"]["LINK_WORD_FRAC"]*100)}%
* Avg links per tag, word: {r2(an_d["LINK_MAX"]["AVG_TAG_LINKS"])}, {r2(an_d["LINK_MAX"]["AVG_WORD_LINKS"])}

### Averages

* Total links: {r2(an_d["LINK_AVG"]["TOTAL_LINKS"])}
* Unique links: {r2(an_d["LINK_AVG"]["UNIQUE_LINKS"])}
* Max links per tag, word: {r2(an_d["LINK_AVG"]["MAX_LINKS_PER_TAG"])}, {r2(an_d["LINK_AVG"]["MAX_LINKS_PER_WORD"])}
* Linked tags, words: {r2(an_d["LINK_AVG"]["LINKED_TAGS"])}, {r2(an_d["LINK_AVG"]["LINKED_WORDS"])}
* Linked % tags, words: {r2(an_d["LINK_AVG"]["LINK_TAG_FRAC"]*100)}%, {r2(an_d["LINK_AVG"]["LINK_WORD_FRAC"]*100)}%
* Avg links per tag, word: {r2(an_d["LINK_AVG"]["AVG_TAG_LINKS"])}, {r2(an_d["LINK_AVG"]["AVG_WORD_LINKS"])}


## Schema

* Maximums (B, I, E, S): {an_d["SCHEMA_B_MAX"]}, {an_d["SCHEMA_I_MAX"]}, {an_d["SCHEMA_E_MAX"]}, {an_d["SCHEMA_S_MAX"]}
* Averages (B, I, E, S): {an_d["SCHEMA_B_AVG"]}, {an_d["SCHEMA_I_AVG"]}, {an_d["SCHEMA_E_AVG"]}, {an_d["SCHEMA_S_AVG"]}


## Labels

* Label: Total, Maximum per entry, Average per entry

{label_category_info}

# Information on each entry

{entry_info}

"""

def get_tag_label_counts_of_word(word_datum, tag_lists, tag_categories):
    parent_key = {}
    for category, data in tag_categories.items():
        for f in data["fields"].keys():
            parent_key[f] = category
    labels = {k: [x[k] for x in word_datum[pk]] for k, pk in parent_key.items()}
    return {k: {l: labels[k].count(l) for l in ls}
            for k, ls in tag_lists.items()}


def get_tag_label_counts_of_entry(word_data_list, tag_lists, tag_categories):
    word_counts = [get_tag_label_counts_of_word(x, tag_lists, tag_categories)
                   for x in word_data_list]
    return {k: {l: sum([x[k][l] for x in word_counts]) for l in ls}
            for k, ls in tag_lists.items()}


def analyse_entry(word_data_list, tag_lists, tag_categories):
    en_d = {"WORDS": len(word_data_list)}
    en_d["TOKENS"] = sum([len(x["TOKENS"]) for x in word_data_list])

    # Tag data
    tag_ids = set()
    def count_tags(word_datum):
        nonlocal tag_ids
        category_tag_ids = {k: [x["id"] for x in word_datum[k]] for k in tag_categories.keys()}

        total = []
        used_categories = 0
        for v in category_tag_ids.values():
            total.extend(v)
            used_categories += v != []

        unique = {x for x in total if x not in tag_ids}
        for u in unique:
            tag_ids.add(u)

        multi_categories = used_categories > 1
        return (len(total), len(unique), multi_categories)

    count_tuples = [count_tags(word_datum) for word_datum in word_data_list]
    tags_per_word = [x for x,_,_ in count_tuples]
    total_tags = sum(tags_per_word)
    tagged_words = sum([x > 0 for x in tags_per_word])

    en_d["TOTAL_TAGS"] = total_tags
    en_d["UNIQUE_TAGS"] = sum([y for _,y,_ in count_tuples])
    en_d["MAX_TAGS"] = max(tags_per_word) if tags_per_word != [] else 0
    en_d["TAGGED_WORDS"] = tagged_words
    en_d["TAG_FRAC"] = tagged_words / len(count_tuples) if tagged_words != 0 else 0
    en_d["AVG_TAGS"] = total_tags / tagged_words if total_tags != 0 else 0
    en_d["MULTI_CAT_WORDS"] = sum([z for _,_,z in count_tuples])

    # Link data
    link_ids = set()
    def count_links(word_datum):
        nonlocal link_ids
        category_link_ids = {k: [x["link_ids"] for x in word_datum[k]]
                             for k in tag_categories.keys()}

        total = []
        for v in category_link_ids.values():
            total.extend(v)

        flattened_ids = []
        for tag_link_ids in total:
            flattened_ids.extend(tag_link_ids)

        unique = {x for x in flattened_ids if x not in link_ids}
        for u in unique:
            link_ids.add(u)

        return ([len(x) for x in total], len(unique))

    # Link counts is a 2 layer list where 1st layer is word datums and 2nd layer is tag datums
    link_counts_pairs = [count_links(word_datum) for word_datum in word_data_list]
    link_counts = [x for x,_ in link_counts_pairs]
    link_counts = [x for x in link_counts if x != []]
    total_links = sum([sum(x) for x in link_counts])
    linked_tags = sum([sum([y > 0 for y in x]) for x in link_counts])
    linked_words = sum([sum(x) > 0 for x in link_counts])

    en_d["TOTAL_LINKS"] = total_links
    en_d["UNIQUE_LINKS"] = sum([y for _,y in link_counts_pairs])
    en_d["MAX_LINKS_PER_TAG"] = max([max(x) for x in link_counts
                                     if x != []]) if link_counts != [] else 0
    en_d["MAX_LINKS_PER_WORD"] = max([sum(x) for x in link_counts]) if link_counts != [] else 0
    en_d["LINKED_TAGS"] = linked_tags
    en_d["LINKED_WORDS"] = linked_words
    en_d["LINK_TAG_FRAC"] = linked_tags / total_tags if total_tags != 0 else 0
    en_d["LINK_WORD_FRAC"] = linked_words / len(count_tuples) if linked_words != 0 else 0
    en_d["AVG_TAG_LINKS"] = total_links / linked_tags if total_links != 0 else 0
    en_d["AVG_WORD_LINKS"] = total_links / linked_words if total_links != 0 else 0

    en_d["LABEL_DATA"] = get_tag_label_counts_of_entry(word_data_list, tag_lists, tag_categories)

    # Schema data
    category_tag_schemas = {k: [tag["schema"] for w in word_data_list for tag in w[k]]
                        for k in tag_categories.keys()}
    schema_tags = []
    for v in category_tag_schemas.values():
        schema_tags.extend(v)

    en_d["SCHEMA_B"] = schema_tags.count("B")
    en_d["SCHEMA_I"] = schema_tags.count("I")
    en_d["SCHEMA_E"] = schema_tags.count("E")
    en_d["SCHEMA_S"] = schema_tags.count("S")

    return en_d


if __name__ == "__main__":

    # an_d -> analysis dict
    # en_d -> entry dict

    # CLI
    parser = argparse.ArgumentParser(description="Analyse the json data and generate a markdown file summary")
    parser.add_argument("-s", "--source", default="data.json",
                        help="Source json data")
    parser.add_argument("-t", "--tag_file", default="tag_list_definitions.json",
                        help="Path to file containing tags and labels")
    parser.add_argument("-c", "--tag_categories", default="tag_categories.json",
                        help="Name of json file with tag categories in it")
    parser.add_argument("-n", "--name", default=None, help="Name of generated analysis file")
    args = parser.parse_args()

    args.name = args.name if args.name is not None else args.source.split('.')[0]
    o_path = ensure_file_ext(args.name, "md")

    with open(ensure_file_ext(args.source, "json")) as f:
        data = json.load(f)

    with open(ensure_file_ext(args.tag_file, "json")) as f:
        tag_lists = json.load(f)

    with open(ensure_file_ext(args.tag_categories, "json")) as f:
        tag_categories = json.load(f)

    del tag_lists["category"]

    title = args.source.split('/')[-1]
    an_d = {"INDIVIDUAL_ENTRIES": {}, "SIZE_INFO": {}}

    # Store data about each entry
    for name, word_data_list in data.items():
        an_d["INDIVIDUAL_ENTRIES"][name] = analyse_entry(word_data_list, tag_lists, tag_categories)

    entries = an_d["INDIVIDUAL_ENTRIES"].values()

    # Size analysis
    num_entries = len(an_d["INDIVIDUAL_ENTRIES"].keys())
    an_d["NUM_ENTRIES"] = num_entries

    words = [en_d["WORDS"] for en_d in entries]
    avg_size = round(sum(words) / num_entries, 1)
    an_d["WORDS"] = {"MAX": max(words), "MIN": min(words), "AVG": avg_size}

    tokens = [en_d["TOKENS"] for en_d in entries]
    avg_size = round(sum(tokens) / num_entries, 1)
    an_d["TOKENS"] = {"MAX": max(tokens), "MIN": min(tokens), "AVG": avg_size,
                               ">512": sum([t > 512 for t in tokens])}


    # Tag analysis
    an_d["TAG_MAX"] = {}
    an_d["TAG_AVG"] = {}

    tag_keys = {"TOTAL_TAGS", "UNIQUE_TAGS", "MAX_TAGS", "TAGGED_WORDS", "TAG_FRAC", "AVG_TAGS",
                "MULTI_CAT_WORDS"}

    for tkey in tag_keys:
        vals = [en_d[tkey] for en_d in entries]
        an_d["TAG_MAX"][tkey] = max(vals)
        an_d["TAG_AVG"][tkey] = sum(vals) / num_entries


    # Link analysis
    an_d["LINK_MAX"] = {}
    an_d["LINK_AVG"] = {}

    link_keys = {"TOTAL_LINKS", "MAX_LINKS_PER_TAG", "MAX_LINKS_PER_WORD", "LINKED_TAGS",
                 "LINKED_WORDS", "LINK_TAG_FRAC", "LINK_WORD_FRAC", "AVG_TAG_LINKS",
                 "AVG_WORD_LINKS", "UNIQUE_LINKS"}

    for lkey in link_keys:
        vals = [en_d[lkey] for en_d in entries]
        an_d["LINK_MAX"][lkey] = max(vals)
        an_d["LINK_AVG"][lkey] = sum(vals) / num_entries


    # Label analysis
    def kle(k,l):
        x = []
        for y in entries:
            x.append(y["LABEL_DATA"][k][l])
        return x

    an_d["LABELS"] = {}

    # Add some extra stuff for overall categories
    category_counts = {k: [sum([sum(x["LABEL_DATA"][f].values()) for f in v["fields"].keys()])
                           for x in entries]
                       for k, v in tag_categories.items()}
    an_d["LABELS"]["categories"] = {k: {"T": sum(v), "M": max(v), "A": np.mean(v)}
                                    for k, v in category_counts.items()}

    an_d["LABELS"].update({k: {l: {"T": sum(kle(k,l)), "M": max(kle(k,l)), "A": np.mean(kle(k,l))}
                               for l in ls}
                           for k, ls in tag_lists.items()})

    # Schema analysis
    for l in ["B", "I", "E", "S"]:
        l_counts = [x[f"SCHEMA_{l}"] for x in entries]
        an_d[f"SCHEMA_{l}_MAX"] = max(l_counts)
        an_d[f"SCHEMA_{l}_AVG"] = r2(sum(l_counts) / len(entries))

    with open(o_path, 'w') as f:
        f.write(md_template(title=title, an_d=an_d))

