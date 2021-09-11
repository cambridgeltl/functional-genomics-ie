#!/bin/sh

# Stop if anything fails
set -e

cd json_data

echo "Performing anaylsis"
python ../tools/rough_analyser.py -s marked_and_linked.json -n ../analysis/marked_and_linked.md
python ../tools/rough_analyser.py -s marked_unlinked.json -n ../analysis/marked_unlinked.md
python ../tools/rough_analyser.py -s unmarked.json -n ../analysis/unmarked.md
python ../tools/rough_analyser.py -s v2_marked_and_linked.json -n ../analysis/v2_marked_and_linked.md -t tag_list_definitions_v2 -c tag_categories_v2
python ../tools/rough_analyser.py -s v2_marked_unlinked.json -n ../analysis/v2_marked_unlinked.md -t tag_list_definitions_v2 -c tag_categories_v2
python ../tools/rough_analyser.py -s v2_unmarked.json -n ../analysis/v2_unmarked.md -t tag_list_definitions_v2 -c tag_categories_v2
python ../tools/rough_analyser.py -s all_marked.json -n ../analysis/all_marked.md
python ../tools/rough_analyser.py -s all_marked_train.json -n ../analysis/all_marked_train.md
python ../tools/rough_analyser.py -s all_marked_test.json -n ../analysis/all_marked_test.md
python ../tools/rough_analyser.py -s marked_and_linked_train.json -n ../analysis/marked_and_linked_train.md
python ../tools/rough_analyser.py -s marked_and_linked_test.json -n ../analysis/marked_and_linked_test.md
python ../tools/rough_analyser.py -s v2_all_marked.json -n ../analysis/v2_all_marked.md -t tag_list_definitions_v2 -c tag_categories_v2
python ../tools/rough_analyser.py -s v2_all_marked_train.json -n ../analysis/v2_all_marked_train.md -t tag_list_definitions_v2 -c tag_categories_v2
python ../tools/rough_analyser.py -s v2_all_marked_test.json -n ../analysis/v2_all_marked_test.md -t tag_list_definitions_v2 -c tag_categories_v2
python ../tools/rough_analyser.py -s v2_marked_and_linked_train.json -n ../analysis/v2_marked_and_linked_train.md -t tag_list_definitions_v2 -c tag_categories_v2
python ../tools/rough_analyser.py -s v2_marked_and_linked_test.json -n ../analysis/v2_marked_and_linked_test.md -t tag_list_definitions_v2 -c tag_categories_v2

echo "Generating pdfs"
cd ../analysis
pandoc marked_and_linked.md -s -o pdfs/marked_and_linked.pdf
pandoc marked_unlinked.md -s -o pdfs/marked_unlinked.pdf
pandoc unmarked.md -s -o pdfs/unmarked.pdf
pandoc v2_marked_and_linked.md -s -o pdfs/v2_marked_and_linked.pdf
pandoc v2_marked_unlinked.md -s -o pdfs/v2_marked_unlinked.pdf
pandoc v2_unmarked.md -s -o pdfs/v2_unmarked.pdf
pandoc all_marked.md -s -o pdfs/all_marked.pdf
pandoc all_marked_train.md -s -o pdfs/all_marked_train.pdf
pandoc all_marked_test.md -s -o pdfs/all_marked_test.pdf
pandoc marked_and_linked_train.md -s -o pdfs/marked_and_linked_train.pdf
pandoc marked_and_linked_test.md -s -o pdfs/marked_and_linked_test.pdf
pandoc v2_all_marked.md -s -o pdfs/v2_all_marked.pdf
pandoc v2_all_marked_train.md -s -o pdfs/v2_all_marked_train.pdf
pandoc v2_all_marked_test.md -s -o pdfs/v2_all_marked_test.pdf
pandoc v2_marked_and_linked_train.md -s -o pdfs/v2_marked_and_linked_train.pdf
pandoc v2_marked_and_linked_test.md -s -o pdfs/v2_marked_and_linked_test.pdf

