#!/bin/sh

# Stop if anything fails
set -e

cd json_data

echo "Converting annotater xml data into json databases"
python ../tools/maexml_to_json.py -s ../raw_data/Marked\ and\ Linked\ Entities -n marked_and_linked.json -r
python ../tools/maexml_to_json.py -s ../raw_data/Marked\ Entities\ No\ Linking -n marked_unlinked.json -r
python ../tools/maexml_to_json.py -s ../raw_data/No\ Marked\ Entities -n unmarked.json -r
python ../tools/maexml_to_json.py -s ../raw_data/V2\ Marked\ and\ Linked\ Entities -n v2_marked_and_linked.json -r -c tag_categories_v2.json
python ../tools/maexml_to_json.py -s ../raw_data/V2\ Marked\ Entities\ No\ Linking -n v2_marked_unlinked.json -r -c tag_categories_v2.json
python ../tools/maexml_to_json.py -s ../raw_data/V2\ No\ Marked\ Entities -n v2_unmarked.json -r -c tag_categories_v2.json

echo "Moving raw data"
mv *_raw.json raw/

echo "Combining and splitting data"
python ../tools/combine_jsons.py marked_and_linked.json marked_unlinked.json -n all_marked.json
python ../tools/combine_jsons.py v2_marked_and_linked.json v2_marked_unlinked.json -n v2_all_marked.json
python ../tools/split_jsons.py all_marked.json all_marked_train.json 0.9 all_marked_test.json 0.1 -r
python ../tools/split_jsons.py v2_all_marked.json v2_all_marked_train.json 0.9 v2_all_marked_test.json 0.1 -r
python ../tools/split_jsons.py marked_and_linked.json marked_and_linked_train.json 0.9 marked_and_linked_test.json 0.1 -r
python ../tools/split_jsons.py v2_marked_and_linked.json v2_marked_and_linked_train.json 0.9 v2_marked_and_linked_test.json 0.1 -r

