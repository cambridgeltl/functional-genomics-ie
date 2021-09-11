import json
import argparse
import os
import xmltodict

from util.core import ensure_list, ensure_file_ext, ensure_folder

from transformers import AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1", do_lower_case=True)


def flatten_list_once(nested_list: list):
    flattened = []
    for l in nested_list:
        flattened.extend(l)
    return flattened


def process_text(text: str):
    """
    "Some sentence.\n\nIt may contain \nline breaks." -->
    ["Some", "sentence.", "It", "may", "contain", "line", "breaks."]
    """
    filtered = [x for x in text.split('\n') if x != '']
    return flatten_list_once([[y for y in x.split(' ') if y != ''] for x in filtered])


def get_schema(tag, word, s_pos, e_pos):
    # First need to get position of word in tag for schema if it's tagged
    # Schema tags are Beginning, Inner, Outer, End and Singleton
    schema_tag = "O"
    span_ranges = [x.split('~') for x in tag["@spans"].split(',')]
    tag_words = [[y for y in x.split(' ') if y != '']
                 for x  in tag["@text"].split('...')]

    assert len(span_ranges) == len(tag_words)
    assert all(len(x) == 2 for x in span_ranges)

    def word_match(tgt_word, start=False, end=False):
        word_splitters = ["-", "/"]

        if word == tgt_word:
            return True
        if word[-1] in [".", ",", ":", ";"] and word[:-1] == tgt_word:
            return True
        if start and any(word.split(x)[-1] == tgt_word for x in word_splitters):
            return True
        if end and any(word.split(x)[0] == tgt_word for x in word_splitters):
            return True
        return False

    # If there's an unpacking error here then there must be a weird span range
    # Like 120~145~160 which is silly
    # Fuzzy check on pos and validate with tag_words as sometimes the pos
    # slips by 1
    # s_pos, e_pos => start position, end position
    # tx_pos => target x position
    for (ts_pos, te_pos), words in zip(span_ranges, tag_words):
        ts_pos, te_pos = int(ts_pos), int(te_pos)

        sob = s_pos <= ts_pos+1  # Start on or before
        soa = ts_pos-1 <= s_pos < te_pos  # Start on or after
        eob = ts_pos < e_pos <= te_pos+1  # End on or before
        eoa = te_pos-1 <= e_pos  # End on or after

        b = sob and eob and word_match(words[0], start=True)
        e = soa and eoa and word_match(words[-1], end=True)
        i = soa and eob and any(word_match(x) for x in words)
        s = sob and eoa and word_match(words[0], start=True, end=True)

        if s:
            # assert len(words) == 1
            schema_tag = "S"
        elif b:
            # assert len(words) >= 2
            schema_tag = "B"
        elif e:
            # assert len(words) >= 2
            schema_tag = "E"
        elif i:
            # assert len(words) >= 3
            schema_tag = "I"
        if b or e or i or s:
            break

    return schema_tag


def process_xml_data(input_dict, tag_categories, title):
    """
    Output will be a list of dictionaries with each entry being for a single word

    Structure of the dictionaries:
        Word itself
        5 label tags which are comprised of (category, description, id, link_id) where:
            id will be the same for words from the same tag
            link_id will be the same for all words that are part of linked tags

    It may not be feasible to feed in the whole paragraph at once to the model however breaking things down into sentences will break the relationships between some tags so this model is needed to preserve data.
    From this data that is more manageable for our models can be derived
    """

    data = input_dict["Genomics_ConceptTask"]
    raw_text = data["TEXT"]
    try:
        raw_tags = data["TAGS"]
    except KeyError:
        raw_tags = None

    word_list = process_text(raw_text)
    output_data = []

    # This will make sure that we get the next, not first occourence for each word
    visited_words = {}

    # As '\n' is seen as one character by the span ranges, we will replace all \n's with spaces
    refined_raw_text = ' '.join(raw_text.split('\n')) + " "

    # Returns next position of a word in refined_raw_text
    # Still some failures, most notably on numbers with punctuation in them (e.g. 6,024)
    def get_word_position(word: str):
        char_pos = 0
        word_pos = 0
        word_left_to_match = word
        next_char_is_word_start = True

        for char in refined_raw_text:

            # We have fully matched the word
            if word_left_to_match == "":
                return word_pos

            else:
                not_visited = True
                if char_pos in visited_words.keys():
                    prev_word = visited_words[char_pos]
                    min_length = min(len(word), len(prev_word))
                    if prev_word[:min_length] == word[:min_length]:
                        not_visited = False
                    else:
                        not_visited = True

                matching = char == word_left_to_match[0]
                start_of_possible_match = next_char_is_word_start and not_visited and matching
                middle_of_possible_match = word_left_to_match != word and matching

                # We are matching our word
                if  middle_of_possible_match or start_of_possible_match:
                    if start_of_possible_match:
                        word_pos = char_pos
                    char_pos += 1
                    word_left_to_match = word_left_to_match[1:]

                # Not matching
                else:
                    char_pos += 1
                    word_left_to_match = word

            next_char_is_word_start = char == ' '

        # Something has gone wrong and we couldn't match the word
        return -1

    sentence_num = 0

    # We need to fetch the tags (if any) for each word
    for word in word_list:

        # Get the tokens generated by this word
        tokens = tokenizer.tokenize(word)

        # Get position of word in text`
        pos = get_word_position(word)
        end_pos = pos + len(word)

        # Update visited words
        visited_words[pos] = word

        # Defaults for tags, list because some words have multiple tag entries for the same category
        tag_category_lists = {k: [] for k in tag_categories.keys()}

        """
        categories = {"PERTURBING_ACTION": {"list": perturbing_action,
                                            "tag_fields": ["@description"],
                                            "entity_linking_field": "@perturbing_actionID"},
                      "CONTEXT": {"list": context,
                                  "tag_fields": ["@experiment_type", "@species"],
                                  "entity_linking_field": "@contextID"},
                      "EFFECT": {"list": effect, "tag_fields": ["@phenotype", "@activity"],
                                 "entity_linking_field": "@effectID"}}
        """

        if raw_tags is not None:
            # Get all the tags that contain this word
            for category_name, category_data in tag_categories.items():

                try:
                    # Check for single entries
                    tag_list = ensure_list(raw_tags[category_name])

                    for tag in tag_list:
                        schema_tag = get_schema(tag, word, pos, end_pos)

                        if schema_tag != "O":
                            entity_id = tag["@id"]
                            info_dict = {"id": entity_id, "link_ids": [], "schema": schema_tag}

                            # Get data from tag
                            generated_tags = {k: tag[v["mae_field"]]
                                              for k, v in category_data["fields"].items()}
                            for k, v in generated_tags.items():
                                info_dict[k] = v

                            # Check if there's links and if it's a linked tag
                            try:
                                links = ensure_list(raw_tags["ENTITY_LINKING"])
                                for link in links:
                                    if link[category_data["entity_linking_field"]] == entity_id:
                                        info_dict["link_ids"].append(link["@id"])

                            # No linking so we move on
                            except KeyError:
                                pass

                            tag_category_lists[category_name].append(info_dict)

                # No tags of this type provided so we move on
                except KeyError:
                    pass

        output_datum = {"WORD": word, "TOKENS": tokens, "SENTENCE": sentence_num, "POS": pos}
        output_datum.update(tag_category_lists)
        output_data.append(output_datum)
        if word[-1] == ".":
            sentence_num += 1

    return output_data


if __name__ == "__main__":

    # CLI for selecting source and destination folders of data
    parser = argparse.ArgumentParser(description="Convert the xml data generated by MAE to json format for usage in ml models and other tools")
    parser.add_argument("-s", "--source", default="./",
                        help="Source folder of mae xml files")
    parser.add_argument("-n", "--name", default="data",
                        help="Name of json file")
    parser.add_argument("-c", "--tag_categories", default="tag_categories.json",
                        help="Name of json file with tag categories in it")
    parser.add_argument("-r", "--raw", action="store_true",
                        help="Whether or not to save raw json data before processing")
    args = parser.parse_args()

    input_path = ensure_folder(args.source)
    output_path = ensure_file_ext(args.name, "json")

    with open(ensure_file_ext(args.tag_categories, "json")) as f:
        tag_categories = json.load(f)

    # This will hold all our data read in from the xml files
    xml_data = {}

    for fname in os.listdir(input_path):
        if fname.endswith(".xml"):
            with open(input_path + fname) as f:
                xml_data[fname] = xmltodict.parse(f.read())

    if args.raw:
        with open(output_path[:-5] + "_raw.json", 'w', encoding="utf-8") as f:
            json.dump(xml_data, f, ensure_ascii=False, indent=4)

    output_data = {k: process_xml_data(v, tag_categories, k) for k,v in xml_data.items()}
    with open(output_path, 'w', encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)

