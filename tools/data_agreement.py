import json
import argparse
import copy

from util.core import ensure_file_ext


def r2(x):
    return round(x,2)


def perc(x):
    return r2(x*100)


def md_template(name1, name2, num_entries1, num_entries2, data_comparisons):
    per_entry_analysis = '\n\n'.join([
        f"""Title: {title},
Total Score: {r2(data['TOTAL_SCORE'])}/{data['TOTAL_TAGGED_WORDS']},
Match Percentage: {perc(data['FRACTION']) if data['FRACTION'] >= 0 else '-'}%"""
        for title, data in data_comparisons.items()
    ])
    total_tagged_words = sum([data["TOTAL_TAGGED_WORDS"] for data in data_comparisons.values()])
    total_score = sum([data["TOTAL_SCORE"] for data in data_comparisons.values()])
    overall_score = total_score / total_tagged_words if total_score != 0 else -1
    fractions = {data["FRACTION"]:k for k, data in data_comparisons.items() if data["FRACTION"] != -1}
    max_fraction = max(fractions.keys())
    max_fraction_entry = fractions[max_fraction]
    min_fraction = min(fractions.keys())
    min_fraction_entry = fractions[min_fraction]

    return f"""---
title: Analysis of Similarity Between 2 Tag Sets
geometry: margin=2.5cm
---

## File information

**File 1:** {name1}, {num_entries1} entries

**File 2:** {name2}, {num_entries2} entries

Matching entry titles: {len(data_comparisons)}


## How similarity is calculated

Each token (word) in the text it is given a score from 0-1 unless neither annotator has tagged it,
in which case it is ignored.
The score is based on what fraction of the tags for that word match, regardless of linking.

**Note**: If words that are not tagged are counted as matches, %'s go up to 90-100% range.


## Overall

Total similarity: {perc(overall_score) if overall_score >= 0 else "-"}%

Best match: {max_fraction_entry}, {perc(max_fraction)}%


## Analysis of each matching entry

{per_entry_analysis}

"""


def no_tags(d1entry, d2entry):
    categories = {"PERTURBING_ACTION", "CONTEXT", "EFFECT"}
    for category in categories:
        d1category = d1entry[category]
        d2category = d2entry[category]
        if d1category != [] or d2category != []:
            return False
    return True


def get_tag_match_data(d1entry, d2entry):
    categories = {"PERTURBING_ACTION": ["description"],
                  "CONTEXT": ["experiment_type", "species"],
                  "EFFECT": ["phenotype", "activity"]}
    all_fields = [x for fields in categories.values() for x in fields]

    # Collect tag values into dicts that are keyed by fields
    d1tags = {}
    d2tags = {}

    for category, fields in categories.items():
        for field in fields:
            values1 = [tag[field] for tag in d1entry[category]]
            d1tags[field] = values1
            values2 = [tag[field] for tag in d2entry[category]]
            d2tags[field] = values2

    # The token will be given a score: how many tags match / how many tags could of matched
    possible_matches = 0
    matches = 0

    # Copy so we can manipulate without having to worry about reconstruction
    d2tagsc = copy.deepcopy(d2tags)

    for field in all_fields:
        for tag_val1 in d1tags[field]:

            # First check if tag exists in other token
            if tag_val1 in d2tagsc[field]:
                matches += 1
                possible_matches += 1

                # Remove so we know at the end if there are any left
                d2tagsc[field].remove(tag_val1)

            else:
                possible_matches += 1

        # Any tags left in second token are non-matches
        possible_matches += len(d2tagsc[field])

    score = matches / possible_matches
    return score, d1tags, d2tags


if __name__ == "__main__":

    # CLI for selecting sources and destinations of data
    parser = argparse.ArgumentParser(description="Check the agreement between 2 sets of json data produced by maexml_to_json.py")
    parser.add_argument("js1", type=str, help="First json file")
    parser.add_argument("js2", type=str, help="Second json file")
    parser.add_argument("-n", "--name", default="comparison",
                        help="Name of generated analysis file")
    parser.add_argument("-r", "--raw", action="store_true",
                        help="Whether or not to save raw analysis comparisons")
    args = parser.parse_args()

    file1_path = ensure_file_ext(args.js1, "json")
    file2_path = ensure_file_ext(args.js2, "json")
    output_path = ensure_file_ext(args.name, "md")
    raw_data_output_path = output_path.split('.')[0] + "_raw.json"

    data_comparisons = {}

    with open(file1_path) as f1:
        with open(file2_path) as f2:
            data1 = json.load(f1)
            data2 = json.load(f2)

    total_entries1 = len(data1.keys())
    total_entries2 = len(data2.keys())

    matching_keys = [x for x in data1.keys() if x in data2.keys()]
    total_matching = len(matching_keys)

    for key in matching_keys:
        d1 = data1[key]
        d2 = data2[key]

        # Check lengths are the same (Same number of words)
        # TODO: Improve this bit
        if len(d1) != len(d2):
            data_comparisons[key] = f"Word lengths unequal: {len(d1)} vs {len(d2)}"
            continue

        total_score = 0
        entry = []
        for i in range(0,len(d1)):
            d1entry = d1[i]
            d2entry = d2[i]
            d1word = d1entry["WORD"]
            d2word = d2entry["WORD"]

            # Check the 2 words are actually equal
            if d1word != d2word:
                entry_dict = {
                    "First Token": d1word,
                    "Second Token": d2word,
                    "Score": 0
                }

            # Skip and don't count words where both are not tagged
            elif no_tags(d1entry, d2entry):
                continue

            else:
                # Check all the relevant tag data is the same, doesn't check links
                score, d1tags, d2tags = get_tag_match_data(d1entry, d2entry)
                total_score += score
                entry_dict = {
                    "Token": d1word,
                    "Score": score,
                    "First Tag Set": d1tags,
                    "Second Tag Set": d2tags
                }
            entry.append(entry_dict)

        data_comparisons[key] = {"TOTAL_TAGGED_WORDS": len(entry),
                                 "TOTAL_SCORE": total_score,
                                 "FRACTION": total_score/len(entry) if len(entry) != 0 else -1,
                                 "RAW_DATA": entry}

    if args.raw:
        with open(raw_data_output_path, 'w', encoding="utf-8") as f:
            json.dump(data_comparisons, f, ensure_ascii=False, indent=4)

    with open(output_path, 'w') as f:
        f.write(md_template(name1=args.js1, name2=args.js2, num_entries1=total_entries1, num_entries2=total_entries2, data_comparisons=data_comparisons))

