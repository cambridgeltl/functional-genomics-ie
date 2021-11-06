---
title: Rough Analysis of marked_unlinked.json
geometry: margin=2cm
---

# General Information

* Num. Entries: 363
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

* Average words: 199.1
* Maximum words: 353
* Minimum words: 94\
* Average tokens: 372.8
* Maximum tokens: 703
* Minimum tokens: 149\
* Entries with over 512 tokens: 32/363, 8.82%


## Tags

### Maximums

* Total tags: 57
* Unique tags: 22
* Max tags: 5
* Tagged words: 50
* Tagged words %: 34.55%
* Avg tags: 1.6
* MC words: 1

### Averages

* Total tags: 14.77
* Unique tags: 5.32
* Max tags: 1.29
* Tagged words: 14.0
* Tagged words %: 7.07%
* Avg tags: 1.04
* MC words: 0.0


## Links

### Maximums

* Total links: 0
* Unique links: 0
* Max links per tag, word: 0, 0
* Linked tags, words: 0, 0
* Linked % tags, words: 0.0%, 0%
* Avg links per tag, word: 0, 0

### Averages

* Total links: 0.0
* Unique links: 0.0
* Max links per tag, word: 0.0, 0.0
* Linked tags, words: 0.0, 0.0
* Linked % tags, words: 0.0%, 0.0%
* Avg links per tag, word: 0.0, 0.0


## Schema

* Maximums (B, I, E, S): 14, 27, 14, 27
* Averages (B, I, E, S): 4.05, 4.34, 4.06, 2.32


## Labels

* Label: Total, Maximum per entry, Average per entry

### Categories

* Perturbing_Action: 1488, 49, 4.1
* Context: 4414, 68, 12.16
* Effect: 3334, 76, 9.18

### Description

* Knock Out: 226, 34, 0.62
* Conditional Knock Out: 105, 15, 0.29
* Knock In: 12, 6, 0.03
* Conditional Knock In: 10, 4, 0.03
* Knock Down: 142, 11, 0.39
* Plasmid Vector: 0, 0, 0.0
* Viral Vector: 11, 6, 0.03
* Pharmacological Inhibition: 339, 17, 0.93
* Decreased Expression Level: 240, 14, 0.66
* Increased Expression Level: 141, 12, 0.39
* Other: 262, 24, 0.72

### Experiment_Type

* Organism: 416, 14, 1.15
* Tumour: 208, 16, 0.57
* Cells: 819, 34, 2.26
* Cell Line: 129, 17, 0.36
* Transformed Cell Line: 442, 15, 1.22
* Primary Culture: 49, 7, 0.13
* Organoid Culture: 41, 14, 0.11
* Cell Transplantation: 0, 0, 0.0
* Xenotransplantation: 98, 24, 0.27
* Other: 3, 3, 0.01
* Not Stated: 2, 2, 0.01

### Species

* Human: 261, 27, 0.72
* Mouse: 370, 14, 1.02
* Rat: 37, 10, 0.1
* Fish: 4, 3, 0.01
* Fly: 5, 3, 0.01
* Yeast: 5, 3, 0.01
* Bacterium: 5, 5, 0.01
* Other: 36, 12, 0.1
* Not Stated: 1484, 32, 4.09

### Phenotype

* Adhesion: 13, 9, 0.04
* Apoptosis: 330, 17, 0.91
* Anoikis: 0, 0, 0.0
* Autophagy: 263, 22, 0.72
* Cell Cycle Arrest: 76, 14, 0.21
* Cell Death: 163, 24, 0.45
* Cell Growth: 48, 14, 0.13
* Cell Survival: 64, 7, 0.18
* Colony Formation: 0, 0, 0.0
* Differentiation: 47, 6, 0.13
* Entosis: 0, 0, 0.0
* Epithelial-Mesenchymal Transition: 33, 10, 0.09
* Ferroptosis: 74, 9, 0.2
* Invasion: 31, 13, 0.09
* Metastasis: 77, 17, 0.21
* Migration: 71, 13, 0.2
* Mitophagy: 25, 7, 0.07
* Necroptosis: 24, 7, 0.07
* Necrosis: 11, 7, 0.03
* Netosis: 0, 0, 0.0
* Oncosis: 7, 7, 0.02
* Proliferation: 88, 10, 0.24
* Pyroptosis: 17, 5, 0.05
* Quiescence: 3, 3, 0.01
* Self-Renewal: 13, 3, 0.04
* Senescence: 14, 3, 0.04
* Transformation: 27, 16, 0.07
* Tumour Growth: 124, 8, 0.34
* Tumourigenesis: 24, 4, 0.07

### Activity

* Causes: 480, 25, 1.32
* Inhibits: 299, 24, 0.82
* Increases: 410, 22, 1.13
* Decreases: 281, 10, 0.77
* Regulates: 82, 8, 0.23
* No Effect: 41, 8, 0.11
* Not Stated: 74, 14, 0.2


# Information on each entry

**Title**:
14_PMID30909789.txt_1_CC.xml,
Words: 133,
Tokens: 269\
Tag data:
Total: 6,
Unique: 3,
Max tags: 1,
Tagged words: 6 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 0, 3, 0)

**Title**:
431_PMID31591470.txt_CC.xml,
Words: 195,
Tokens: 353\
Tag data:
Total: 16,
Unique: 3,
Max tags: 1,
Tagged words: 16 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 8, 4, 0)

**Title**:
333_PMID32938906.txt_CC.xml,
Words: 180,
Tokens: 374\
Tag data:
Total: 18,
Unique: 8,
Max tags: 1,
Tagged words: 18 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 4, 4, 6)

**Title**:
210_PMID30602440.txt_CC.xml,
Words: 110,
Tokens: 213\
Tag data:
Total: 3,
Unique: 1,
Max tags: 1,
Tagged words: 3 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 1)

**Title**:
765_PMID32470390.txt_CC.xml,
Words: 133,
Tokens: 254\
Tag data:
Total: 7,
Unique: 3,
Max tags: 1,
Tagged words: 7 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 2, 2, 1)

**Title**:
579_PMID30788651.txt_CC.xml,
Words: 255,
Tokens: 463\
Tag data:
Total: 17,
Unique: 9,
Max tags: 2,
Tagged words: 16 (6%),
Avg tags: 1.06,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 2, 4, 7)

**Title**:
521_PMID31227933.txt_CC.xml,
Words: 264,
Tokens: 533\
Tag data:
Total: 10,
Unique: 5,
Max tags: 1,
Tagged words: 10 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 2, 3, 2)

**Title**:
615_PMID33278357.txt_CC.xml,
Words: 168,
Tokens: 333\
Tag data:
Total: 2,
Unique: 2,
Max tags: 1,
Tagged words: 2 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (0, 0, 0, 2)

**Title**:
619_PMID32937105.txt_CC.xml,
Words: 156,
Tokens: 265\
Tag data:
Total: 8,
Unique: 2,
Max tags: 1,
Tagged words: 8 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 4, 2, 0)

**Title**:
144_PMID33023943.txt_CC.xml,
Words: 177,
Tokens: 273\
Tag data:
Total: 16,
Unique: 5,
Max tags: 1,
Tagged words: 16 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 8, 3, 2)

**Title**:
375_PMID33462182.txt_CC.xml,
Words: 309,
Tokens: 592\
Tag data:
Total: 27,
Unique: 14,
Max tags: 1,
Tagged words: 27 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 2, 9, 7)

**Title**:
762_PMID31821784.txt_CC.xml,
Words: 141,
Tokens: 276\
Tag data:
Total: 32,
Unique: 5,
Max tags: 2,
Tagged words: 30 (21%),
Avg tags: 1.07,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 20, 5, 2)

**Title**:
794_PMID30753824.txt_CC.xml,
Words: 137,
Tokens: 285\
Tag data:
Total: 27,
Unique: 9,
Max tags: 3,
Tagged words: 23 (17%),
Avg tags: 1.17,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 6, 9, 3)

**Title**:
106_PMID32029550.txt_CC.xml,
Words: 284,
Tokens: 486\
Tag data:
Total: 16,
Unique: 5,
Max tags: 1,
Tagged words: 16 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 6, 4, 2)

**Title**:
650_PMID32659862.txt_CC.xml,
Words: 158,
Tokens: 256\
Tag data:
Total: 6,
Unique: 1,
Max tags: 1,
Tagged words: 6 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 4, 1, 0)

**Title**:
422_PMID31819158.txt_CC.xml,
Words: 251,
Tokens: 479\
Tag data:
Total: 6,
Unique: 1,
Max tags: 1,
Tagged words: 6 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 4, 1, 0)

**Title**:
259_PMID32792353.txt_CC.xml,
Words: 157,
Tokens: 285\
Tag data:
Total: 6,
Unique: 3,
Max tags: 1,
Tagged words: 6 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 1, 1, 3)

**Title**:
373_PMID33436548.txt_CC.xml,
Words: 262,
Tokens: 533\
Tag data:
Total: 17,
Unique: 9,
Max tags: 1,
Tagged words: 17 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 1, 6, 4)

**Title**:
227_PMID32943573.txt_CC.xml,
Words: 271,
Tokens: 442\
Tag data:
Total: 28,
Unique: 8,
Max tags: 2,
Tagged words: 25 (9%),
Avg tags: 1.12,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 13, 6, 3)

**Title**:
287_PMID32381626.txt_CC.xml,
Words: 112,
Tokens: 202\
Tag data:
Total: 5,
Unique: 2,
Max tags: 1,
Tagged words: 5 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 1, 2, 0)

**Title**:
649_PMID32916131.txt_CC.xml,
Words: 151,
Tokens: 266\
Tag data:
Total: 6,
Unique: 3,
Max tags: 1,
Tagged words: 6 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 2)

**Title**:
439_PMID31065106.txt_CC.xml,
Words: 177,
Tokens: 298\
Tag data:
Total: 11,
Unique: 4,
Max tags: 2,
Tagged words: 10 (6%),
Avg tags: 1.1,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 3, 3, 2)

**Title**:
632_PMID33031745.txt_CC.xml,
Words: 171,
Tokens: 334\
Tag data:
Total: 22,
Unique: 5,
Max tags: 2,
Tagged words: 18 (11%),
Avg tags: 1.22,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 9, 5, 3)

**Title**:
561_PMID32737651.txt_CC.xml,
Words: 249,
Tokens: 458\
Tag data:
Total: 50,
Unique: 14,
Max tags: 1,
Tagged words: 50 (20%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (13, 23, 13, 1)

**Title**:
381_PMID33024087.txt_CC.xml,
Words: 185,
Tokens: 336\
Tag data:
Total: 2,
Unique: 1,
Max tags: 1,
Tagged words: 2 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 0)

**Title**:
138_PMID32127357.txt_CC.xml,
Words: 217,
Tokens: 314\
Tag data:
Total: 4,
Unique: 2,
Max tags: 1,
Tagged words: 4 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 0)

**Title**:
353_PMID33483474.txt_CC.xml,
Words: 253,
Tokens: 382\
Tag data:
Total: 4,
Unique: 2,
Max tags: 1,
Tagged words: 4 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 0)

**Title**:
303_PMID33024077.txt_CC.xml,
Words: 147,
Tokens: 242\
Tag data:
Total: 9,
Unique: 3,
Max tags: 1,
Tagged words: 9 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 3, 2, 2)

**Title**:
465_PMID31515511.txt_CC.xml,
Words: 162,
Tokens: 358\
Tag data:
Total: 17,
Unique: 10,
Max tags: 1,
Tagged words: 17 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 3, 3, 8)

**Title**:
239_PMID32193353.txt_CC.xml,
Words: 218,
Tokens: 382\
Tag data:
Total: 57,
Unique: 15,
Max tags: 3,
Tagged words: 38 (17%),
Avg tags: 1.5,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (14, 21, 14, 8)

**Title**:
758_PMID30423296.txt_CC.xml,
Words: 132,
Tokens: 271\
Tag data:
Total: 19,
Unique: 8,
Max tags: 1,
Tagged words: 19 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 5, 5, 4)

**Title**:
4_PMID32186434.txt_CC.xml,
Words: 155,
Tokens: 271\
Tag data:
Total: 24,
Unique: 7,
Max tags: 2,
Tagged words: 20 (13%),
Avg tags: 1.2,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 7, 8, 1)

**Title**:
477_PMID32094512.txt_CC.xml,
Words: 191,
Tokens: 368\
Tag data:
Total: 21,
Unique: 8,
Max tags: 1,
Tagged words: 21 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 7, 6, 2)

**Title**:
94_PMID30741586.txt_CC.xml,
Words: 155,
Tokens: 242\
Tag data:
Total: 7,
Unique: 2,
Max tags: 1,
Tagged words: 7 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 2, 2, 1)

**Title**:
428_PMID31802034.txt_CC.xml,
Words: 210,
Tokens: 435\
Tag data:
Total: 17,
Unique: 7,
Max tags: 1,
Tagged words: 17 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 4, 5, 3)

**Title**:
148_PMID32690724.txt_CC.xml,
Words: 156,
Tokens: 284\
Tag data:
Total: 14,
Unique: 7,
Max tags: 1,
Tagged words: 14 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 3, 4, 3)

**Title**:
359_PMID33116116.txt_CC.xml,
Words: 207,
Tokens: 393\
Tag data:
Total: 9,
Unique: 4,
Max tags: 1,
Tagged words: 9 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 1, 3, 2)

**Title**:
219_PMID29945888.txt_CC.xml,
Words: 228,
Tokens: 397\
Tag data:
Total: 11,
Unique: 3,
Max tags: 1,
Tagged words: 11 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 5, 3, 0)

**Title**:
394_PMID33093458.txt_CC.xml,
Words: 300,
Tokens: 593\
Tag data:
Total: 40,
Unique: 13,
Max tags: 4,
Tagged words: 29 (10%),
Avg tags: 1.38,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (13, 5, 13, 9)

**Title**:
595_PMID30578463.txt_CC.xml,
Words: 262,
Tokens: 543\
Tag data:
Total: 40,
Unique: 13,
Max tags: 1,
Tagged words: 40 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (11, 15, 11, 3)

**Title**:
526_PMID30949883.txt_CC.xml,
Words: 222,
Tokens: 366\
Tag data:
Total: 8,
Unique: 5,
Max tags: 1,
Tagged words: 8 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 6)

**Title**:
735_PMID30905761.txt_CC.xml,
Words: 130,
Tokens: 255\
Tag data:
Total: 13,
Unique: 5,
Max tags: 1,
Tagged words: 13 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 3, 4, 2)

**Title**:
404_PMID32203170.txt_CC.xml,
Words: 254,
Tokens: 557\
Tag data:
Total: 26,
Unique: 12,
Max tags: 1,
Tagged words: 26 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 8, 6, 6)

**Title**:
776_PMID33186519.txt_CC.xml,
Words: 160,
Tokens: 283\
Tag data:
Total: 14,
Unique: 6,
Max tags: 1,
Tagged words: 14 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 2, 6, 0)

**Title**:
498_PMID31819159.txt_CC.xml,
Words: 245,
Tokens: 485\
Tag data:
Total: 11,
Unique: 4,
Max tags: 2,
Tagged words: 8 (3%),
Avg tags: 1.38,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 3, 3, 2)

**Title**:
89_PMID32264736.txt_CC.xml,
Words: 164,
Tokens: 345\
Tag data:
Total: 5,
Unique: 2,
Max tags: 1,
Tagged words: 5 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 1)

**Title**:
544_PMID32100210.txt_CC.xml,
Words: 238,
Tokens: 416\
Tag data:
Total: 14,
Unique: 10,
Max tags: 1,
Tagged words: 14 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 10)

**Title**:
515_PMID32761307.txt_CC.xml,
Words: 226,
Tokens: 370\
Tag data:
Total: 18,
Unique: 6,
Max tags: 1,
Tagged words: 18 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 6, 4, 4)

**Title**:
6_PMID30966861.txt_CC.xml,
Words: 215,
Tokens: 429\
Tag data:
Total: 11,
Unique: 5,
Max tags: 1,
Tagged words: 11 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 2, 3, 3)

**Title**:
556_PMID29435687.txt_CC.xml,
Words: 146,
Tokens: 283\
Tag data:
Total: 8,
Unique: 2,
Max tags: 1,
Tagged words: 8 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 4, 2, 0)

**Title**:
327_PMID33203874.txt_CC.xml,
Words: 235,
Tokens: 426\
Tag data:
Total: 11,
Unique: 6,
Max tags: 1,
Tagged words: 11 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 2, 2, 5)

**Title**:
2_PMID30335591.txt_CC.xml,
Words: 174,
Tokens: 421\
Tag data:
Total: 6,
Unique: 3,
Max tags: 1,
Tagged words: 6 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 0, 3, 0)

**Title**:
46_PMID30821613.txt_CC.xml,
Words: 192,
Tokens: 260\
Tag data:
Total: 14,
Unique: 4,
Max tags: 1,
Tagged words: 14 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 6, 4, 0)

**Title**:
393_PMID33067426.txt_CC.xml,
Words: 232,
Tokens: 386\
Tag data:
Total: 29,
Unique: 12,
Max tags: 4,
Tagged words: 26 (11%),
Avg tags: 1.12,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 7, 6, 10)

**Title**:
82_PMID30304977.txt_CC.xml,
Words: 252,
Tokens: 440\
Tag data:
Total: 9,
Unique: 3,
Max tags: 1,
Tagged words: 9 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 4, 2, 1)

**Title**:
361_PMID32943619.txt_CC.xml,
Words: 233,
Tokens: 397\
Tag data:
Total: 23,
Unique: 8,
Max tags: 2,
Tagged words: 21 (9%),
Avg tags: 1.1,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 5, 7, 4)

**Title**:
351_PMID33097698.txt_CC.xml,
Words: 192,
Tokens: 298\
Tag data:
Total: 14,
Unique: 2,
Max tags: 1,
Tagged words: 14 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 10, 2, 0)

**Title**:
785_PMID33357452.txt_CC.xml,
Words: 171,
Tokens: 348\
Tag data:
Total: 8,
Unique: 3,
Max tags: 1,
Tagged words: 8 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 2, 2, 2)

**Title**:
249_PMID32115406.txt_CC.xml,
Words: 158,
Tokens: 271\
Tag data:
Total: 2,
Unique: 1,
Max tags: 1,
Tagged words: 2 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 0)

**Title**:
648_PMID33147444.txt_CC.xml,
Words: 176,
Tokens: 349\
Tag data:
Total: 4,
Unique: 2,
Max tags: 2,
Tagged words: 3 (2%),
Avg tags: 1.33,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 2)

**Title**:
414_PMID31367011.txt_CC.xml,
Words: 163,
Tokens: 343\
Tag data:
Total: 9,
Unique: 4,
Max tags: 1,
Tagged words: 9 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 1, 1, 6)

**Title**:
560_PMID32591959.txt_CC.xml,
Words: 196,
Tokens: 351\
Tag data:
Total: 12,
Unique: 7,
Max tags: 1,
Tagged words: 12 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 0, 4, 4)

**Title**:
47_PMID32003282.txt_CC.xml,
Words: 207,
Tokens: 414\
Tag data:
Total: 13,
Unique: 3,
Max tags: 1,
Tagged words: 13 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 8, 2, 1)

**Title**:
552_PMID29058102.txt_CC.xml,
Words: 201,
Tokens: 393\
Tag data:
Total: 8,
Unique: 3,
Max tags: 1,
Tagged words: 8 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 2, 3, 0)

**Title**:
107_PMID31911550.txt_CC.xml,
Words: 181,
Tokens: 331\
Tag data:
Total: 8,
Unique: 3,
Max tags: 1,
Tagged words: 8 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 2, 3, 0)

**Title**:
599_PMID32036474.txt_CC.xml,
Words: 266,
Tokens: 538\
Tag data:
Total: 24,
Unique: 9,
Max tags: 1,
Tagged words: 24 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 6, 8, 2)

**Title**:
8_PMID30523761.txt_CC.xml,
Words: 265,
Tokens: 510\
Tag data:
Total: 16,
Unique: 5,
Max tags: 1,
Tagged words: 16 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 6, 5, 0)

**Title**:
590_PMID26386572.txt_CC.xml,
Words: 220,
Tokens: 428\
Tag data:
Total: 15,
Unique: 7,
Max tags: 3,
Tagged words: 13 (6%),
Avg tags: 1.15,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 1, 4, 6)

**Title**:
52_PMID31920157.txt_CC.xml,
Words: 220,
Tokens: 347\
Tag data:
Total: 14,
Unique: 6,
Max tags: 1,
Tagged words: 14 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 5, 3, 3)

**Title**:
13_PMID6735470.txt_CC.xml,
Words: 156,
Tokens: 283\
Tag data:
Total: 2,
Unique: 1,
Max tags: 1,
Tagged words: 2 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 0)

**Title**:
576_PMID30610505.txt_CC.xml,
Words: 251,
Tokens: 478\
Tag data:
Total: 46,
Unique: 9,
Max tags: 2,
Tagged words: 40 (16%),
Avg tags: 1.15,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 27, 9, 1)

**Title**:
449_PMID30442948.txt_CC.xml,
Words: 243,
Tokens: 427\
Tag data:
Total: 14,
Unique: 6,
Max tags: 1,
Tagged words: 14 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 1, 5, 3)

**Title**:
473_PMID33082514.txt_CC.xml,
Words: 169,
Tokens: 283\
Tag data:
Total: 6,
Unique: 3,
Max tags: 1,
Tagged words: 6 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 0, 3, 0)

**Title**:
387_PMID33056980.txt_CC.xml,
Words: 209,
Tokens: 373\
Tag data:
Total: 30,
Unique: 9,
Max tags: 2,
Tagged words: 24 (11%),
Avg tags: 1.25,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 12, 7, 4)

**Title**:
30_PMID30681394.txt_CC.xml,
Words: 163,
Tokens: 352\
Tag data:
Total: 10,
Unique: 5,
Max tags: 1,
Tagged words: 10 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 3, 2, 3)

**Title**:
408_PMID30787392.txt_CC.xml,
Words: 191,
Tokens: 406\
Tag data:
Total: 7,
Unique: 3,
Max tags: 1,
Tagged words: 7 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 1, 3, 0)

**Title**:
78_PMID30929559.txt_CC.xml,
Words: 136,
Tokens: 253\
Tag data:
Total: 3,
Unique: 1,
Max tags: 1,
Tagged words: 3 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 1, 1, 0)

**Title**:
503_PMID29705943.txt_CC.xml,
Words: 265,
Tokens: 509\
Tag data:
Total: 21,
Unique: 9,
Max tags: 2,
Tagged words: 18 (7%),
Avg tags: 1.17,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 3, 6, 6)

**Title**:
653_PMID33142117.txt_CC.xml,
Words: 153,
Tokens: 289\
Tag data:
Total: 9,
Unique: 5,
Max tags: 1,
Tagged words: 9 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 1, 2, 4)

**Title**:
159_PMID32973082.txt_CC.xml,
Words: 277,
Tokens: 661\
Tag data:
Total: 29,
Unique: 7,
Max tags: 1,
Tagged words: 29 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 14, 7, 1)

**Title**:
574_PMID25953318.txt_CC.xml,
Words: 249,
Tokens: 498\
Tag data:
Total: 18,
Unique: 8,
Max tags: 1,
Tagged words: 18 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 6, 4, 4)

**Title**:
480_PMID31827236.txt_CC.xml,
Words: 232,
Tokens: 494\
Tag data:
Total: 15,
Unique: 8,
Max tags: 1,
Tagged words: 15 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 2, 5, 3)

**Title**:
108_PMID33184108.txt_CC.xml,
Words: 215,
Tokens: 349\
Tag data:
Total: 7,
Unique: 4,
Max tags: 1,
Tagged words: 7 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 1, 2, 2)

**Title**:
661_PMID33157039.txt_CC.xml,
Words: 156,
Tokens: 249\
Tag data:
Total: 4,
Unique: 1,
Max tags: 1,
Tagged words: 4 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 0)

**Title**:
386_PMID33311446.txt_CC.xml,
Words: 155,
Tokens: 304\
Tag data:
Total: 10,
Unique: 5,
Max tags: 1,
Tagged words: 10 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 0, 4, 2)

**Title**:
703_PMID31883968.txt_CC.xml,
Words: 126,
Tokens: 223\
Tag data:
Total: 15,
Unique: 4,
Max tags: 1,
Tagged words: 15 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 7, 4, 0)

**Title**:
455_PMID31114027.txt_CC.xml,
Words: 184,
Tokens: 402\
Tag data:
Total: 2,
Unique: 1,
Max tags: 1,
Tagged words: 2 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 0)

**Title**:
350_PMID33257690.txt_CC.xml,
Words: 310,
Tokens: 581\
Tag data:
Total: 43,
Unique: 9,
Max tags: 1,
Tagged words: 43 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (11, 21, 11, 0)

**Title**:
433_PMID31127201.txt_CC.xml,
Words: 185,
Tokens: 374\
Tag data:
Total: 10,
Unique: 5,
Max tags: 2,
Tagged words: 8 (4%),
Avg tags: 1.25,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 0, 3, 4)

**Title**:
420_PMID31748695.txt_CC.xml,
Words: 199,
Tokens: 374\
Tag data:
Total: 14,
Unique: 6,
Max tags: 1,
Tagged words: 14 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 4, 4, 2)

**Title**:
175_PMID32350067.txt_CC.xml,
Words: 213,
Tokens: 377\
Tag data:
Total: 10,
Unique: 3,
Max tags: 1,
Tagged words: 10 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 5, 2, 1)

**Title**:
446_PMID32152555.txt_CC.xml,
Words: 257,
Tokens: 505\
Tag data:
Total: 20,
Unique: 6,
Max tags: 2,
Tagged words: 15 (6%),
Avg tags: 1.33,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 8, 6, 2)

**Title**:
123_PMID32606006.txt_CC.xml,
Words: 171,
Tokens: 329\
Tag data:
Total: 13,
Unique: 6,
Max tags: 1,
Tagged words: 13 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 1, 5, 2)

**Title**:
292_PMID28546513.txt_CC.xml,
Words: 190,
Tokens: 347\
Tag data:
Total: 3,
Unique: 1,
Max tags: 1,
Tagged words: 3 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 1, 1, 0)

**Title**:
721_PMID31588020.txt_CC.xml,
Words: 139,
Tokens: 247\
Tag data:
Total: 10,
Unique: 3,
Max tags: 1,
Tagged words: 10 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 5, 2, 1)

**Title**:
297_PMID31919188.txt_CC.xml,
Words: 162,
Tokens: 308\
Tag data:
Total: 11,
Unique: 5,
Max tags: 1,
Tagged words: 11 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 3, 3, 2)

**Title**:
11_PMID31441366.txt_CC.xml,
Words: 164,
Tokens: 305\
Tag data:
Total: 13,
Unique: 4,
Max tags: 2,
Tagged words: 11 (7%),
Avg tags: 1.18,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 0, 4, 5)

**Title**:
577_PMID31867678.txt_CC.xml,
Words: 240,
Tokens: 388\
Tag data:
Total: 5,
Unique: 2,
Max tags: 1,
Tagged words: 5 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 1, 2, 0)

**Title**:
90_PMID31983283.txt_CC.xml,
Words: 243,
Tokens: 480\
Tag data:
Total: 6,
Unique: 4,
Max tags: 1,
Tagged words: 6 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 2)

**Title**:
528_PMID29777330.txt_CC.xml,
Words: 353,
Tokens: 700\
Tag data:
Total: 5,
Unique: 3,
Max tags: 1,
Tagged words: 5 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 1)

**Title**:
212_PMID28877934.txt_CC.xml,
Words: 108,
Tokens: 202\
Tag data:
Total: 4,
Unique: 2,
Max tags: 2,
Tagged words: 3 (3%),
Avg tags: 1.33,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 2)

**Title**:
709_PMID29455927.txt_CC.xml,
Words: 126,
Tokens: 301\
Tag data:
Total: 10,
Unique: 5,
Max tags: 1,
Tagged words: 10 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 6)

**Title**:
256_PMID30006480.txt_CC.xml,
Words: 176,
Tokens: 332\
Tag data:
Total: 8,
Unique: 4,
Max tags: 1,
Tagged words: 8 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 1, 3, 1)

**Title**:
377_PMID32929059.txt_CC.xml,
Words: 270,
Tokens: 533\
Tag data:
Total: 23,
Unique: 8,
Max tags: 2,
Tagged words: 20 (7%),
Avg tags: 1.15,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 4, 9, 1)

**Title**:
307_PMID33144579.txt_CC.xml,
Words: 209,
Tokens: 393\
Tag data:
Total: 54,
Unique: 22,
Max tags: 2,
Tagged words: 44 (21%),
Avg tags: 1.23,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 9, 9, 27)

**Title**:
320_PMID33106477.txt_CC.xml,
Words: 214,
Tokens: 409\
Tag data:
Total: 8,
Unique: 4,
Max tags: 1,
Tagged words: 8 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 0, 3, 2)

**Title**:
277_PMID31296559.txt_CC.xml,
Words: 185,
Tokens: 329\
Tag data:
Total: 5,
Unique: 3,
Max tags: 1,
Tagged words: 5 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 1, 1, 2)

**Title**:
388_PMID33318476.txt_CC.xml,
Words: 187,
Tokens: 309\
Tag data:
Total: 10,
Unique: 5,
Max tags: 1,
Tagged words: 10 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 2, 3, 2)

**Title**:
129_PMID33483372.txt_CC.xml,
Words: 218,
Tokens: 346\
Tag data:
Total: 33,
Unique: 10,
Max tags: 3,
Tagged words: 29 (13%),
Avg tags: 1.14,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (10, 6, 10, 7)

**Title**:
220_PMID31221665.txt_CC.xml,
Words: 196,
Tokens: 368\
Tag data:
Total: 8,
Unique: 2,
Max tags: 1,
Tagged words: 8 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 0, 3, 2)

**Title**:
749_PMID31935372.txt_CC.xml,
Words: 126,
Tokens: 262\
Tag data:
Total: 6,
Unique: 4,
Max tags: 2,
Tagged words: 5 (4%),
Avg tags: 1.2,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 4)

**Title**:
208_PMID32001512.txt_CC.xml,
Words: 207,
Tokens: 374\
Tag data:
Total: 9,
Unique: 3,
Max tags: 1,
Tagged words: 9 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 3, 3, 0)

**Title**:
366_PMID33127884.txt_CC.xml,
Words: 230,
Tokens: 403\
Tag data:
Total: 25,
Unique: 7,
Max tags: 2,
Tagged words: 20 (9%),
Avg tags: 1.25,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 8, 7, 3)

**Title**:
28_PMID30786811.txt_CC.xml,
Words: 261,
Tokens: 473\
Tag data:
Total: 17,
Unique: 6,
Max tags: 2,
Tagged words: 15 (6%),
Avg tags: 1.13,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 3, 7, 0)

**Title**:
459_PMID33100324.txt_CC.xml,
Words: 163,
Tokens: 328\
Tag data:
Total: 2,
Unique: 1,
Max tags: 1,
Tagged words: 2 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 0)

**Title**:
218_PMID32439635.txt_CC.xml,
Words: 159,
Tokens: 301\
Tag data:
Total: 2,
Unique: 1,
Max tags: 1,
Tagged words: 2 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (0, 0, 0, 2)

**Title**:
383_PMID32963254.txt_CC.xml,
Words: 157,
Tokens: 278\
Tag data:
Total: 10,
Unique: 5,
Max tags: 1,
Tagged words: 10 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 2, 3, 2)

**Title**:
519_PMID31485878.txt_1_CC.xml,
Words: 187,
Tokens: 333\
Tag data:
Total: 10,
Unique: 6,
Max tags: 2,
Tagged words: 8 (4%),
Avg tags: 1.25,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (0, 0, 0, 10)

**Title**:
338_PMID33110074.txt_CC.xml,
Words: 183,
Tokens: 344\
Tag data:
Total: 1,
Unique: 1,
Max tags: 1,
Tagged words: 1 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (0, 0, 0, 1)

**Title**:
270_PMID31171704.txt_CC.xml,
Words: 195,
Tokens: 342\
Tag data:
Total: 2,
Unique: 1,
Max tags: 1,
Tagged words: 2 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 0)

**Title**:
651_PMID33333024.txt_CC.xml,
Words: 161,
Tokens: 300\
Tag data:
Total: 1,
Unique: 1,
Max tags: 1,
Tagged words: 1 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (0, 0, 0, 1)

**Title**:
293_PMID31123067.txt_CC.xml,
Words: 173,
Tokens: 293\
Tag data:
Total: 5,
Unique: 2,
Max tags: 1,
Tagged words: 5 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 2, 1, 1)

**Title**:
206_PMID32883681.txt_CC.xml,
Words: 151,
Tokens: 319\
Tag data:
Total: 9,
Unique: 4,
Max tags: 1,
Tagged words: 9 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 4, 1, 3)

**Title**:
424_PMID29786072.txt_CC.xml,
Words: 245,
Tokens: 549\
Tag data:
Total: 28,
Unique: 10,
Max tags: 1,
Tagged words: 28 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 10, 8, 2)

**Title**:
760_PMID32516590.txt_CC.xml,
Words: 112,
Tokens: 209\
Tag data:
Total: 4,
Unique: 2,
Max tags: 1,
Tagged words: 4 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 1, 1, 1)

**Title**:
268_PMID32561545.txt_CC.xml,
Words: 192,
Tokens: 291\
Tag data:
Total: 13,
Unique: 3,
Max tags: 1,
Tagged words: 13 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 7, 3, 0)

**Title**:
588_PMID26801321.txt_CC.xml,
Words: 224,
Tokens: 398\
Tag data:
Total: 9,
Unique: 5,
Max tags: 1,
Tagged words: 9 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 0, 3, 3)

**Title**:
744_PMID31474569.txt_CC.xml,
Words: 136,
Tokens: 319\
Tag data:
Total: 9,
Unique: 3,
Max tags: 1,
Tagged words: 9 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 3, 3, 0)

**Title**:
96_PMID30669930.txt_CC.xml,
Words: 183,
Tokens: 354\
Tag data:
Total: 21,
Unique: 7,
Max tags: 1,
Tagged words: 21 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 6, 7, 1)

**Title**:
58_PMID31821607.txt_CC.xml,
Words: 185,
Tokens: 357\
Tag data:
Total: 26,
Unique: 7,
Max tags: 1,
Tagged words: 26 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 12, 7, 0)

**Title**:
416_PMID31097789.txt_CC.xml,
Words: 251,
Tokens: 498\
Tag data:
Total: 3,
Unique: 2,
Max tags: 1,
Tagged words: 3 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 1)

**Title**:
241_PMID32115408.txt_CC.xml,
Words: 218,
Tokens: 429\
Tag data:
Total: 35,
Unique: 15,
Max tags: 1,
Tagged words: 35 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 9, 9, 8)

**Title**:
349_PMID33093455.txt_CC.xml,
Words: 243,
Tokens: 573\
Tag data:
Total: 22,
Unique: 7,
Max tags: 2,
Tagged words: 21 (9%),
Avg tags: 1.05,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 7, 5, 5)

**Title**:
362_PMID33051435.txt_CC.xml,
Words: 202,
Tokens: 386\
Tag data:
Total: 21,
Unique: 5,
Max tags: 1,
Tagged words: 21 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 10, 5, 1)

**Title**:
633_PMID33125892.txt_CC.xml,
Words: 154,
Tokens: 283\
Tag data:
Total: 10,
Unique: 4,
Max tags: 1,
Tagged words: 10 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 3, 3, 1)

**Title**:
151_PMID32341035.txt_CC.xml,
Words: 229,
Tokens: 385\
Tag data:
Total: 15,
Unique: 5,
Max tags: 1,
Tagged words: 15 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 6, 4, 1)

**Title**:
795_PMID28810147.txt_CC.xml,
Words: 132,
Tokens: 275\
Tag data:
Total: 8,
Unique: 2,
Max tags: 1,
Tagged words: 8 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 4, 2, 0)

**Title**:
440_PMID31337872.txt_CC.xml,
Words: 259,
Tokens: 534\
Tag data:
Total: 9,
Unique: 3,
Max tags: 1,
Tagged words: 9 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 3, 2, 2)

**Title**:
676_PMID32795415.txt_CC.xml,
Words: 148,
Tokens: 314\
Tag data:
Total: 16,
Unique: 6,
Max tags: 1,
Tagged words: 16 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 6, 4, 2)

**Title**:
435_PMID31097787.txt_CC.xml,
Words: 170,
Tokens: 318\
Tag data:
Total: 27,
Unique: 11,
Max tags: 1,
Tagged words: 27 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 10, 5, 7)

**Title**:
204_PMID28143833.txt_CC.xml,
Words: 205,
Tokens: 301\
Tag data:
Total: 13,
Unique: 3,
Max tags: 1,
Tagged words: 13 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 6, 3, 1)

**Title**:
520_PMID32338336.txt_CC.xml,
Words: 246,
Tokens: 446\
Tag data:
Total: 7,
Unique: 4,
Max tags: 1,
Tagged words: 7 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 0, 3, 1)

**Title**:
296_PMID31171700.txt_CC.xml,
Words: 202,
Tokens: 282\
Tag data:
Total: 9,
Unique: 2,
Max tags: 1,
Tagged words: 9 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 6, 1, 1)

**Title**:
495_PMID32814877.txt.xml,
Words: 185,
Tokens: 353\
Tag data:
Total: 5,
Unique: 3,
Max tags: 1,
Tagged words: 5 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 1, 1, 2)

**Title**:
121_PMID32217695.txt_CC.xml,
Words: 214,
Tokens: 445\
Tag data:
Total: 13,
Unique: 5,
Max tags: 3,
Tagged words: 11 (5%),
Avg tags: 1.18,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 2, 3, 5)

**Title**:
342_PMID33082328.txt_CC.xml,
Words: 209,
Tokens: 433\
Tag data:
Total: 25,
Unique: 5,
Max tags: 1,
Tagged words: 25 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 15, 5, 0)

**Title**:
722_PMID30645973.txt_CC.xml,
Words: 122,
Tokens: 203\
Tag data:
Total: 25,
Unique: 6,
Max tags: 2,
Tagged words: 17 (14%),
Avg tags: 1.47,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 6, 9, 1)

**Title**:
205_PMID32079653.txt_CC.xml,
Words: 197,
Tokens: 321\
Tag data:
Total: 15,
Unique: 2,
Max tags: 1,
Tagged words: 15 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 11, 2, 0)

**Title**:
781_PMID30889383.txt_CC.xml,
Words: 131,
Tokens: 241\
Tag data:
Total: 4,
Unique: 2,
Max tags: 1,
Tagged words: 4 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 0)

**Title**:
688_PMID32822574.txt_CC.xml,
Words: 159,
Tokens: 279\
Tag data:
Total: 14,
Unique: 5,
Max tags: 2,
Tagged words: 11 (7%),
Avg tags: 1.27,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 4, 3, 4)

**Title**:
258_PMID29773557.txt_CC.xml,
Words: 107,
Tokens: 217\
Tag data:
Total: 15,
Unique: 4,
Max tags: 2,
Tagged words: 13 (12%),
Avg tags: 1.15,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 4, 5, 1)

**Title**:
279_PMID32217664.txt_CC.xml,
Words: 217,
Tokens: 352\
Tag data:
Total: 2,
Unique: 1,
Max tags: 1,
Tagged words: 2 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 0)

**Title**:
565_PMID31768842.txt_CC.xml,
Words: 225,
Tokens: 424\
Tag data:
Total: 4,
Unique: 3,
Max tags: 1,
Tagged words: 4 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (0, 0, 0, 4)

**Title**:
443_PMID30042493.txt_CC.xml,
Words: 195,
Tokens: 391\
Tag data:
Total: 10,
Unique: 4,
Max tags: 1,
Tagged words: 10 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 2, 4, 0)

**Title**:
55_PMID31177911.txt_CC.xml,
Words: 187,
Tokens: 356\
Tag data:
Total: 22,
Unique: 10,
Max tags: 1,
Tagged words: 22 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (10, 2, 10, 0)

**Title**:
167_PMID33293428.txt_CC.xml,
Words: 214,
Tokens: 446\
Tag data:
Total: 15,
Unique: 6,
Max tags: 2,
Tagged words: 14 (7%),
Avg tags: 1.07,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 5, 2, 6)

**Title**:
553_PMID29236198.txt_CC.xml,
Words: 263,
Tokens: 444\
Tag data:
Total: 16,
Unique: 5,
Max tags: 1,
Tagged words: 16 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 6, 4, 2)

**Title**:
301_PMID33116120.txt_CC.xml,
Words: 282,
Tokens: 588\
Tag data:
Total: 19,
Unique: 7,
Max tags: 1,
Tagged words: 19 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 3, 7, 2)

**Title**:
742_PMID32679107.txt_CC.xml,
Words: 121,
Tokens: 224\
Tag data:
Total: 5,
Unique: 2,
Max tags: 1,
Tagged words: 5 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 3)

**Title**:
191_PMID32156781.txt_CC.xml,
Words: 257,
Tokens: 435\
Tag data:
Total: 21,
Unique: 6,
Max tags: 2,
Tagged words: 19 (7%),
Avg tags: 1.11,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 5, 8, 0)

**Title**:
209_PMID30692202.txt_CC.xml,
Words: 173,
Tokens: 308\
Tag data:
Total: 18,
Unique: 2,
Max tags: 1,
Tagged words: 18 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 14, 2, 0)

**Title**:
502_PMID28289909.txt_CC.xml,
Words: 242,
Tokens: 489\
Tag data:
Total: 42,
Unique: 14,
Max tags: 2,
Tagged words: 39 (16%),
Avg tags: 1.08,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (13, 12, 13, 4)

**Title**:
37_PMID30909843.txt_CC.xml,
Words: 237,
Tokens: 423\
Tag data:
Total: 4,
Unique: 2,
Max tags: 1,
Tagged words: 4 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 0)

**Title**:
364_PMID3320108.txt_CC.xml,
Words: 214,
Tokens: 354\
Tag data:
Total: 8,
Unique: 5,
Max tags: 1,
Tagged words: 8 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 4)

**Title**:
693_PMID32991842.txt_CC.xml,
Words: 161,
Tokens: 262\
Tag data:
Total: 27,
Unique: 5,
Max tags: 2,
Tagged words: 24 (15%),
Avg tags: 1.12,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 16, 5, 1)

**Title**:
720_PMID32679108.txt_CC.xml,
Words: 122,
Tokens: 215\
Tag data:
Total: 14,
Unique: 3,
Max tags: 2,
Tagged words: 13 (11%),
Avg tags: 1.08,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 8, 1, 4)

**Title**:
116_PMID32193290.txt_CC.xml,
Words: 159,
Tokens: 285\
Tag data:
Total: 7,
Unique: 3,
Max tags: 1,
Tagged words: 7 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 1, 2, 2)

**Title**:
582_PMID30778709.txt_CC.xml,
Words: 256,
Tokens: 501\
Tag data:
Total: 15,
Unique: 4,
Max tags: 2,
Tagged words: 12 (5%),
Avg tags: 1.25,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 3, 5, 2)

**Title**:
131_PMID32265223.txt_CC.xml,
Words: 166,
Tokens: 366\
Tag data:
Total: 11,
Unique: 4,
Max tags: 1,
Tagged words: 11 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 3, 3, 2)

**Title**:
594_PMID28168327.txt_CC.xml,
Words: 207,
Tokens: 369\
Tag data:
Total: 14,
Unique: 5,
Max tags: 1,
Tagged words: 14 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 3, 5, 1)

**Title**:
624_PMID32778225.txt_CC.xml,
Words: 135,
Tokens: 282\
Tag data:
Total: 14,
Unique: 6,
Max tags: 1,
Tagged words: 14 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 5, 3, 3)

**Title**:
348_PMID33024074.txt_CC.xml,
Words: 283,
Tokens: 519\
Tag data:
Total: 1,
Unique: 1,
Max tags: 1,
Tagged words: 1 (0%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (0, 0, 0, 1)

**Title**:
231_PMID30692207.txt_CC.xml,
Words: 173,
Tokens: 345\
Tag data:
Total: 23,
Unique: 8,
Max tags: 2,
Tagged words: 20 (12%),
Avg tags: 1.15,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 7, 7, 2)

**Title**:
780_PMID32559497.txt_CC.xml,
Words: 132,
Tokens: 245\
Tag data:
Total: 4,
Unique: 2,
Max tags: 1,
Tagged words: 4 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 1, 1, 1)

**Title**:
201_PMID32079652.txt_CC.xml,
Words: 231,
Tokens: 443\
Tag data:
Total: 12,
Unique: 5,
Max tags: 2,
Tagged words: 10 (4%),
Avg tags: 1.2,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 2, 4, 2)

**Title**:
187_PMID32393661.txt_CC.xml,
Words: 211,
Tokens: 384\
Tag data:
Total: 12,
Unique: 6,
Max tags: 2,
Tagged words: 11 (5%),
Avg tags: 1.09,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 0, 4, 4)

**Title**:
409_PMID31209362.txt_CC.xml,
Words: 155,
Tokens: 274\
Tag data:
Total: 17,
Unique: 7,
Max tags: 2,
Tagged words: 16 (10%),
Avg tags: 1.06,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 3, 5, 4)

**Title**:
374_PMID33106471.txt_CC.xml,
Words: 308,
Tokens: 491\
Tag data:
Total: 14,
Unique: 7,
Max tags: 1,
Tagged words: 14 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 2, 5, 2)

**Title**:
200_PMID32522824.txt_CC.xml,
Words: 250,
Tokens: 470\
Tag data:
Total: 8,
Unique: 3,
Max tags: 1,
Tagged words: 8 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 1, 3, 1)

**Title**:
186_PMID32098780.txt_CC.xml,
Words: 204,
Tokens: 385\
Tag data:
Total: 19,
Unique: 7,
Max tags: 1,
Tagged words: 19 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 5, 7, 0)

**Title**:
291_PMID30366905.txt_CC.xml,
Words: 176,
Tokens: 289\
Tag data:
Total: 3,
Unique: 1,
Max tags: 1,
Tagged words: 3 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 1, 1, 0)

**Title**:
334_PMID33056982.txt_CC.xml,
Words: 184,
Tokens: 381\
Tag data:
Total: 12,
Unique: 5,
Max tags: 1,
Tagged words: 12 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 2, 5, 0)

**Title**:
163_PMID33115807.txt_CC.xml,
Words: 255,
Tokens: 438\
Tag data:
Total: 5,
Unique: 2,
Max tags: 1,
Tagged words: 5 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 1, 2, 0)

**Title**:
113_PMID32029551.txt_CC.xml,
Words: 223,
Tokens: 437\
Tag data:
Total: 25,
Unique: 10,
Max tags: 1,
Tagged words: 25 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 5, 8, 4)

**Title**:
482_PMID31367013.txt_CC.xml,
Words: 212,
Tokens: 459\
Tag data:
Total: 29,
Unique: 9,
Max tags: 2,
Tagged words: 23 (11%),
Avg tags: 1.26,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 9, 9, 2)

**Title**:
379_PMID33311447.txt_CC.xml,
Words: 211,
Tokens: 357\
Tag data:
Total: 4,
Unique: 1,
Max tags: 1,
Tagged words: 4 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 2, 1, 0)

**Title**:
513_PMID32627119.txt_CC.xml,
Words: 264,
Tokens: 527\
Tag data:
Total: 14,
Unique: 8,
Max tags: 2,
Tagged words: 13 (5%),
Avg tags: 1.08,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 10)

**Title**:
157_PMID32132110.txt_CC.xml,
Words: 242,
Tokens: 374\
Tag data:
Total: 29,
Unique: 8,
Max tags: 1,
Tagged words: 29 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 13, 7, 2)

**Title**:
487_PMID32661288.txt_CC.xml,
Words: 305,
Tokens: 531\
Tag data:
Total: 4,
Unique: 2,
Max tags: 1,
Tagged words: 4 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 0)

**Title**:
246_PMID32139423.txt_CC.xml,
Words: 151,
Tokens: 276\
Tag data:
Total: 6,
Unique: 2,
Max tags: 1,
Tagged words: 6 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 2, 2, 0)

**Title**:
71_PMID32521192.txt_CC.xml,
Words: 197,
Tokens: 372\
Tag data:
Total: 9,
Unique: 2,
Max tags: 1,
Tagged words: 9 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 5, 2, 0)

**Title**:
726_PMID31668947.txt_CC.xml,
Words: 124,
Tokens: 243\
Tag data:
Total: 21,
Unique: 4,
Max tags: 2,
Tagged words: 19 (15%),
Avg tags: 1.11,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 12, 4, 1)

**Title**:
411_PMID30692641.txt_CC.xml,
Words: 228,
Tokens: 414\
Tag data:
Total: 23,
Unique: 10,
Max tags: 2,
Tagged words: 22 (10%),
Avg tags: 1.05,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 4, 7, 5)

**Title**:
23_PMID30208757.txt_CC.xml,
Words: 170,
Tokens: 320\
Tag data:
Total: 17,
Unique: 6,
Max tags: 1,
Tagged words: 17 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 4, 6, 1)

**Title**:
551_PMID31605257.txt_CC.xml,
Words: 258,
Tokens: 412\
Tag data:
Total: 22,
Unique: 7,
Max tags: 1,
Tagged words: 22 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 8, 7, 0)

**Title**:
211_PMID31416966.txt_CC.xml,
Words: 243,
Tokens: 424\
Tag data:
Total: 22,
Unique: 7,
Max tags: 1,
Tagged words: 22 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 8, 5, 4)

**Title**:
79_PMID31448673.txt_CC.xml,
Words: 153,
Tokens: 313\
Tag data:
Total: 6,
Unique: 3,
Max tags: 1,
Tagged words: 6 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 0, 3, 0)

**Title**:
768_PMID32619407.txt_CC.xml,
Words: 122,
Tokens: 247\
Tag data:
Total: 8,
Unique: 1,
Max tags: 1,
Tagged words: 8 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 6, 1, 0)

**Title**:
723_PMID31715132.txt_CC.xml,
Words: 126,
Tokens: 221\
Tag data:
Total: 24,
Unique: 6,
Max tags: 2,
Tagged words: 23 (18%),
Avg tags: 1.04,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 12, 5, 2)

**Title**:
529_PMID31111379.txt_CC.xml,
Words: 262,
Tokens: 631\
Tag data:
Total: 32,
Unique: 14,
Max tags: 1,
Tagged words: 32 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 7, 9, 7)

**Title**:
83_PMID30741592.txt_CC.xml,
Words: 263,
Tokens: 436\
Tag data:
Total: 25,
Unique: 9,
Max tags: 1,
Tagged words: 25 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 7, 7, 4)

**Title**:
792_PMID32220301.txt_CC.xml,
Words: 136,
Tokens: 242\
Tag data:
Total: 7,
Unique: 4,
Max tags: 1,
Tagged words: 7 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 0, 3, 1)

**Title**:
563_PMID29978434.txt_CC.xml,
Words: 195,
Tokens: 302\
Tag data:
Total: 21,
Unique: 8,
Max tags: 1,
Tagged words: 21 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 5, 7, 2)

**Title**:
727_PMID30991027.txt_CC.xml,
Words: 113,
Tokens: 222\
Tag data:
Total: 39,
Unique: 8,
Max tags: 2,
Tagged words: 32 (28%),
Avg tags: 1.22,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (10, 17, 10, 2)

**Title**:
587_PMID28176146.txt_CC.xml,
Words: 248,
Tokens: 419\
Tag data:
Total: 14,
Unique: 6,
Max tags: 1,
Tagged words: 14 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 3, 4, 3)

**Title**:
382_PMID33188167.txt_CC.xml,
Words: 269,
Tokens: 421\
Tag data:
Total: 10,
Unique: 3,
Max tags: 1,
Tagged words: 10 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 4, 3, 0)

**Title**:
567_PMID27770267.txt_CC.xml,
Words: 286,
Tokens: 479\
Tag data:
Total: 35,
Unique: 11,
Max tags: 2,
Tagged words: 34 (12%),
Avg tags: 1.03,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (10, 13, 10, 2)

**Title**:
538_PMID32418059.txt_CC.xml,
Words: 252,
Tokens: 551\
Tag data:
Total: 33,
Unique: 10,
Max tags: 1,
Tagged words: 33 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 13, 9, 2)

**Title**:
104_PMID32605995.txt_CC.xml,
Words: 204,
Tokens: 355\
Tag data:
Total: 23,
Unique: 7,
Max tags: 2,
Tagged words: 19 (9%),
Avg tags: 1.21,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 4, 9, 1)

**Title**:
469_PMID32144381.txt_CC.xml,
Words: 270,
Tokens: 535\
Tag data:
Total: 25,
Unique: 8,
Max tags: 3,
Tagged words: 19 (7%),
Avg tags: 1.32,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 8, 6, 5)

**Title**:
427_PMID30349076.txt_CC.xml,
Words: 207,
Tokens: 415\
Tag data:
Total: 3,
Unique: 2,
Max tags: 1,
Tagged words: 3 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 1)

**Title**:
317_PMID33188203.txt_CC.xml,
Words: 117,
Tokens: 226\
Tag data:
Total: 10,
Unique: 5,
Max tags: 1,
Tagged words: 10 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 2, 2, 4)

**Title**:
511_PMID31974865.txt_CC.xml,
Words: 232,
Tokens: 446\
Tag data:
Total: 23,
Unique: 5,
Max tags: 2,
Tagged words: 20 (9%),
Avg tags: 1.15,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 10, 6, 1)

**Title**:
358_PMID33257655.txt_CC.xml,
Words: 271,
Tokens: 516\
Tag data:
Total: 4,
Unique: 2,
Max tags: 1,
Tagged words: 4 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 0)

**Title**:
169_PMID32269045.txt_CC.xml,
Words: 242,
Tokens: 396\
Tag data:
Total: 6,
Unique: 2,
Max tags: 1,
Tagged words: 6 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 2, 2, 0)

**Title**:
476_PMID29459771.txt_CC.xml,
Words: 256,
Tokens: 455\
Tag data:
Total: 30,
Unique: 15,
Max tags: 1,
Tagged words: 30 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (10, 2, 10, 8)

**Title**:
472_PMID31222041.txt_CC.xml,
Words: 264,
Tokens: 472\
Tag data:
Total: 2,
Unique: 2,
Max tags: 1,
Tagged words: 2 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (0, 0, 0, 2)

**Title**:
602_PMID33301708.txt_CC.xml,
Words: 151,
Tokens: 260\
Tag data:
Total: 17,
Unique: 7,
Max tags: 1,
Tagged words: 17 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 4, 5, 3)

**Title**:
272_PMID30842217.txt_CC.xml,
Words: 151,
Tokens: 257\
Tag data:
Total: 7,
Unique: 2,
Max tags: 1,
Tagged words: 7 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 3, 2, 0)

**Title**:
118_PMID32816860.txt_CC.xml,
Words: 184,
Tokens: 319\
Tag data:
Total: 5,
Unique: 3,
Max tags: 1,
Tagged words: 5 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 3)

**Title**:
196_PMID32213544.txt_CC.xml,
Words: 196,
Tokens: 392\
Tag data:
Total: 18,
Unique: 5,
Max tags: 1,
Tagged words: 18 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 9, 4, 1)

**Title**:
128_PMID32193288.txt_CC.xml,
Words: 199,
Tokens: 391\
Tag data:
Total: 28,
Unique: 8,
Max tags: 1,
Tagged words: 28 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 14, 6, 2)

**Title**:
63_PMID31696776.txt_CC.xml,
Words: 209,
Tokens: 422\
Tag data:
Total: 9,
Unique: 4,
Max tags: 1,
Tagged words: 9 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 2, 3, 1)

**Title**:
371_PMID33323928.txt_CC.xml,
Words: 218,
Tokens: 423\
Tag data:
Total: 11,
Unique: 5,
Max tags: 1,
Tagged words: 11 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 2, 4, 1)

**Title**:
524_PMID32418060.txt_CC.xml,
Words: 219,
Tokens: 382\
Tag data:
Total: 8,
Unique: 3,
Max tags: 1,
Tagged words: 8 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 2, 3, 0)

**Title**:
506_PMID30710195.txt_CC.xml,
Words: 255,
Tokens: 547\
Tag data:
Total: 20,
Unique: 10,
Max tags: 2,
Tagged words: 15 (6%),
Avg tags: 1.33,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 0, 4, 12)

**Title**:
39_PMID30676840.txt_CC.xml,
Words: 261,
Tokens: 468\
Tag data:
Total: 15,
Unique: 6,
Max tags: 1,
Tagged words: 15 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 4, 5, 1)

**Title**:
517_PMID33068199.txt_CC.xml,
Words: 166,
Tokens: 351\
Tag data:
Total: 10,
Unique: 6,
Max tags: 1,
Tagged words: 10 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 8)

**Title**:
461_PMID31570856.txt_CC.xml,
Words: 194,
Tokens: 447\
Tag data:
Total: 18,
Unique: 7,
Max tags: 5,
Tagged words: 14 (7%),
Avg tags: 1.29,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 2, 4, 8)

**Title**:
137_PMID32816913.txt_CC.xml,
Words: 191,
Tokens: 356\
Tag data:
Total: 3,
Unique: 1,
Max tags: 1,
Tagged words: 3 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 1, 1, 0)

**Title**:
558_PMID31691131.txt_CC.xml,
Words: 167,
Tokens: 294\
Tag data:
Total: 20,
Unique: 10,
Max tags: 1,
Tagged words: 20 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 4, 3, 10)

**Title**:
713_PMID29657128.txt_CC.xml,
Words: 132,
Tokens: 227\
Tag data:
Total: 4,
Unique: 1,
Max tags: 1,
Tagged words: 4 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 2, 1, 0)

**Title**:
344_PMID33060560.txt_CC.xml,
Words: 229,
Tokens: 466\
Tag data:
Total: 25,
Unique: 10,
Max tags: 1,
Tagged words: 25 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 6, 9, 1)

**Title**:
514_PMID31993850.txt_CC.xml,
Words: 254,
Tokens: 540\
Tag data:
Total: 21,
Unique: 11,
Max tags: 1,
Tagged words: 21 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 2, 6, 7)

**Title**:
570_PMID29858716.txt_CC.xml,
Words: 266,
Tokens: 423\
Tag data:
Total: 20,
Unique: 8,
Max tags: 1,
Tagged words: 20 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 5, 6, 3)

**Title**:
555_PMID33230593.txt_CC.xml,
Words: 230,
Tokens: 468\
Tag data:
Total: 10,
Unique: 4,
Max tags: 1,
Tagged words: 10 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 0, 5, 0)

**Title**:
677_PMID33007268.txt_CC.xml,
Words: 151,
Tokens: 233\
Tag data:
Total: 20,
Unique: 5,
Max tags: 2,
Tagged words: 19 (13%),
Avg tags: 1.05,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 8, 5, 2)

**Title**:
483_PMID31831874.txt_CC.xml,
Words: 222,
Tokens: 397\
Tag data:
Total: 17,
Unique: 8,
Max tags: 1,
Tagged words: 17 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 3, 6, 2)

**Title**:
605_PMID32795413.txt_CC.xml,
Words: 138,
Tokens: 253\
Tag data:
Total: 4,
Unique: 3,
Max tags: 1,
Tagged words: 4 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 2)

**Title**:
326_PMID33293527.txt_CC.xml,
Words: 221,
Tokens: 394\
Tag data:
Total: 15,
Unique: 4,
Max tags: 1,
Tagged words: 15 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 8, 3, 1)

**Title**:
540_PMID31243498.txt_CC.xml,
Words: 211,
Tokens: 401\
Tag data:
Total: 42,
Unique: 18,
Max tags: 1,
Tagged words: 42 (20%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (11, 12, 11, 8)

**Title**:
569_PMID28012059.txt_CC.xml,
Words: 205,
Tokens: 402\
Tag data:
Total: 34,
Unique: 10,
Max tags: 1,
Tagged words: 34 (17%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (10, 12, 10, 2)

**Title**:
111_PMID32816857.txt_CC.xml,
Words: 224,
Tokens: 407\
Tag data:
Total: 11,
Unique: 3,
Max tags: 2,
Tagged words: 10 (4%),
Avg tags: 1.1,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 5, 2, 2)

**Title**:
160_PMID32366480.txt_CC.xml,
Words: 240,
Tokens: 424\
Tag data:
Total: 13,
Unique: 4,
Max tags: 1,
Tagged words: 13 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 5, 4, 0)

**Title**:
618_PMID33147445.txt_CC.xml,
Words: 152,
Tokens: 246\
Tag data:
Total: 7,
Unique: 2,
Max tags: 1,
Tagged words: 7 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 3, 2, 0)

**Title**:
330_PMID33203867.txt_CC.xml,
Words: 225,
Tokens: 383\
Tag data:
Total: 31,
Unique: 10,
Max tags: 1,
Tagged words: 31 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (10, 10, 10, 1)

**Title**:
134_PMID32641409.txt_CC.xml,
Words: 223,
Tokens: 448\
Tag data:
Total: 26,
Unique: 6,
Max tags: 1,
Tagged words: 26 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 14, 6, 0)

**Title**:
500_PMID30442947.txt_CC.xml,
Words: 167,
Tokens: 309\
Tag data:
Total: 8,
Unique: 2,
Max tags: 2,
Tagged words: 5 (3%),
Avg tags: 1.6,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 0, 3, 2)

**Title**:
21_PMID31184563.txt_CC.xml,
Words: 223,
Tokens: 407\
Tag data:
Total: 22,
Unique: 10,
Max tags: 1,
Tagged words: 22 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 4, 7, 4)

**Title**:
238_PMID31753913.txt_CC.xml,
Words: 202,
Tokens: 359\
Tag data:
Total: 6,
Unique: 2,
Max tags: 2,
Tagged words: 4 (2%),
Avg tags: 1.5,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 1, 2, 1)

**Title**:
406_PMID30568238.txt_CC.xml,
Words: 164,
Tokens: 295\
Tag data:
Total: 12,
Unique: 4,
Max tags: 1,
Tagged words: 12 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 3, 2, 5)

**Title**:
769_PMID29533781.txt_CC.xml,
Words: 128,
Tokens: 255\
Tag data:
Total: 10,
Unique: 5,
Max tags: 2,
Tagged words: 9 (7%),
Avg tags: 1.11,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 1, 4, 1)

**Title**:
368_PMID33093476.txt_CC.xml,
Words: 190,
Tokens: 317\
Tag data:
Total: 23,
Unique: 8,
Max tags: 1,
Tagged words: 23 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 6, 8, 1)

**Title**:
313_PMID33099572.txt_CC.xml,
Words: 140,
Tokens: 284\
Tag data:
Total: 5,
Unique: 2,
Max tags: 1,
Tagged words: 5 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 1, 2, 0)

**Title**:
314_PMID32968054.txt_CC.xml,
Words: 214,
Tokens: 372\
Tag data:
Total: 23,
Unique: 9,
Max tags: 1,
Tagged words: 23 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 6, 7, 3)

**Title**:
69_PMID30773986.txt_CC.xml,
Words: 174,
Tokens: 326\
Tag data:
Total: 14,
Unique: 5,
Max tags: 1,
Tagged words: 14 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 4, 5, 0)

**Title**:
759_PMID30423294.txt_CC.xml,
Words: 131,
Tokens: 215\
Tag data:
Total: 3,
Unique: 1,
Max tags: 1,
Tagged words: 3 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 1, 1, 0)

**Title**:
800_PMID31631026.txt_CC.xml,
Words: 129,
Tokens: 281\
Tag data:
Total: 28,
Unique: 8,
Max tags: 3,
Tagged words: 25 (19%),
Avg tags: 1.12,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 9, 6, 7)

**Title**:
493_PMID32139900.txt_CC.xml,
Words: 248,
Tokens: 494\
Tag data:
Total: 12,
Unique: 5,
Max tags: 1,
Tagged words: 12 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 3, 4, 1)

**Title**:
275_PMID31395742.txt_CC.xml,
Words: 171,
Tokens: 292\
Tag data:
Total: 1,
Unique: 1,
Max tags: 1,
Tagged words: 1 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (0, 0, 0, 1)

**Title**:
305_PMID32951003.txt_CC.xml,
Words: 230,
Tokens: 453\
Tag data:
Total: 23,
Unique: 10,
Max tags: 2,
Tagged words: 22 (10%),
Avg tags: 1.05,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 3, 6, 8)

**Title**:
793_PMID31287991.txt_CC.xml,
Words: 140,
Tokens: 294\
Tag data:
Total: 1,
Unique: 1,
Max tags: 1,
Tagged words: 1 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (0, 0, 0, 1)

**Title**:
464_PMID31645676.txt_CC.xml,
Words: 207,
Tokens: 382\
Tag data:
Total: 15,
Unique: 6,
Max tags: 1,
Tagged words: 15 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 5, 4, 2)

**Title**:
507_PMID30877409.txt_CC.xml,
Words: 196,
Tokens: 396\
Tag data:
Total: 11,
Unique: 6,
Max tags: 1,
Tagged words: 11 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 1, 4, 2)

**Title**:
432_PMID30683918.txt_CC.xml,
Words: 257,
Tokens: 572\
Tag data:
Total: 27,
Unique: 12,
Max tags: 1,
Tagged words: 27 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (10, 5, 10, 2)

**Title**:
92_PMID_30894052.txt_CC.xml,
Words: 161,
Tokens: 312\
Tag data:
Total: 29,
Unique: 11,
Max tags: 1,
Tagged words: 29 (18%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 8, 9, 3)

**Title**:
496_PMID32737443.txt_CC.xml,
Words: 186,
Tokens: 355\
Tag data:
Total: 15,
Unique: 6,
Max tags: 2,
Tagged words: 13 (7%),
Avg tags: 1.15,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 1, 6, 2)

**Title**:
240_PMID32241802.txt_CC.xml,
Words: 138,
Tokens: 254\
Tag data:
Total: 31,
Unique: 7,
Max tags: 2,
Tagged words: 27 (20%),
Avg tags: 1.15,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 15, 8, 0)

**Title**:
12_PMID30917721.txt_CC.xml,
Words: 196,
Tokens: 412\
Tag data:
Total: 10,
Unique: 4,
Max tags: 2,
Tagged words: 9 (5%),
Avg tags: 1.11,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 1, 4, 1)

**Title**:
445_PMID31988495.txt_CC.xml,
Words: 241,
Tokens: 397\
Tag data:
Total: 18,
Unique: 7,
Max tags: 1,
Tagged words: 18 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 5, 6, 1)

**Title**:
284_PMID32354836.txt_CC.xml,
Words: 286,
Tokens: 511\
Tag data:
Total: 4,
Unique: 2,
Max tags: 1,
Tagged words: 4 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 1, 1, 1)

**Title**:
389_PMID33239613.txt_CC.xml,
Words: 241,
Tokens: 428\
Tag data:
Total: 11,
Unique: 6,
Max tags: 1,
Tagged words: 11 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 0, 5, 1)

**Title**:
603_PMID32946783.txt_CC.xml,
Words: 159,
Tokens: 256\
Tag data:
Total: 0,
Unique: 0,
Max tags: 0,
Tagged words: 0 (0%),
Avg tags: 0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (0, 0, 0, 0)

**Title**:
253_PMID31558567.txt_CC.xml,
Words: 206,
Tokens: 378\
Tag data:
Total: 30,
Unique: 14,
Max tags: 1,
Tagged words: 30 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 7, 6, 11)

**Title**:
788_PMID32516591.txt_CC.xml,
Words: 123,
Tokens: 219\
Tag data:
Total: 8,
Unique: 2,
Max tags: 1,
Tagged words: 8 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 4, 2, 0)

**Title**:
283_PMID32273287.txt_CC.xml,
Words: 218,
Tokens: 379\
Tag data:
Total: 30,
Unique: 8,
Max tags: 1,
Tagged words: 30 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 14, 7, 2)

**Title**:
460_PMID33273695.txt_CC.xml,
Words: 155,
Tokens: 280\
Tag data:
Total: 4,
Unique: 2,
Max tags: 1,
Tagged words: 4 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 0)

**Title**:
188_PMID32561531.txt_CC.xml,
Words: 180,
Tokens: 267\
Tag data:
Total: 6,
Unique: 2,
Max tags: 1,
Tagged words: 6 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 2, 2, 0)

**Title**:
25_PMID31203721.txt_CC.xml,
Words: 209,
Tokens: 396\
Tag data:
Total: 32,
Unique: 11,
Max tags: 2,
Tagged words: 29 (14%),
Avg tags: 1.1,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (10, 10, 10, 2)

**Title**:
74_PMID31971848.txt_CC.xml,
Words: 112,
Tokens: 206\
Tag data:
Total: 2,
Unique: 1,
Max tags: 1,
Tagged words: 2 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 0)

**Title**:
26_PMID31362587.txt_CC.xml,
Words: 225,
Tokens: 507\
Tag data:
Total: 35,
Unique: 11,
Max tags: 2,
Tagged words: 29 (13%),
Avg tags: 1.21,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (10, 12, 10, 3)

**Title**:
215_PMID31048544.txt_CC.xml,
Words: 127,
Tokens: 244\
Tag data:
Total: 11,
Unique: 3,
Max tags: 1,
Tagged words: 11 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 6, 2, 1)

**Title**:
300_PMID32912900.txt_CC.xml,
Words: 155,
Tokens: 237\
Tag data:
Total: 41,
Unique: 6,
Max tags: 2,
Tagged words: 31 (20%),
Avg tags: 1.32,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 25, 8, 0)

**Title**:
398_PMID33311488.txt_CC.xml,
Words: 162,
Tokens: 292\
Tag data:
Total: 16,
Unique: 6,
Max tags: 1,
Tagged words: 16 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 3, 6, 1)

**Title**:
346_PMID33431801.txt_CC.xml,
Words: 269,
Tokens: 593\
Tag data:
Total: 20,
Unique: 9,
Max tags: 1,
Tagged words: 20 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 5, 5, 5)

**Title**:
559_PMID30911960.txt_CC.xml,
Words: 219,
Tokens: 409\
Tag data:
Total: 7,
Unique: 4,
Max tags: 1,
Tagged words: 7 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 1, 2, 2)

**Title**:
739_PMID31056398.txt_CC.xml,
Words: 114,
Tokens: 194\
Tag data:
Total: 2,
Unique: 1,
Max tags: 1,
Tagged words: 2 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 0)

**Title**:
447_PMID31434979.txt_CC.xml,
Words: 185,
Tokens: 390\
Tag data:
Total: 9,
Unique: 3,
Max tags: 1,
Tagged words: 9 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 3, 2, 2)

**Title**:
376_PMID33139721.txt_CC.xml,
Words: 273,
Tokens: 468\
Tag data:
Total: 18,
Unique: 7,
Max tags: 1,
Tagged words: 18 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 6, 5, 2)

**Title**:
177_PMID33229341.txt_CC.xml,
Words: 216,
Tokens: 436\
Tag data:
Total: 10,
Unique: 3,
Max tags: 1,
Tagged words: 10 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 3, 3, 1)

**Title**:
288_PMID30366907.txt_CC.xml,
Words: 169,
Tokens: 325\
Tag data:
Total: 3,
Unique: 1,
Max tags: 1,
Tagged words: 3 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 1, 1, 0)

**Title**:
583_PMID32409930.txt_CC.xml,
Words: 208,
Tokens: 327\
Tag data:
Total: 15,
Unique: 9,
Max tags: 2,
Tagged words: 14 (7%),
Avg tags: 1.07,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 0, 4, 7)

**Title**:
336_PMID32943605.txt_CC.xml,
Words: 246,
Tokens: 465\
Tag data:
Total: 26,
Unique: 10,
Max tags: 3,
Tagged words: 24 (10%),
Avg tags: 1.08,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 8, 5, 8)

**Title**:
322_PMID33051453.txt_CC.xml,
Words: 262,
Tokens: 466\
Tag data:
Total: 36,
Unique: 10,
Max tags: 1,
Tagged words: 36 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 18, 7, 4)

**Title**:
660_PMID33002410.txt_CC.xml,
Words: 163,
Tokens: 296\
Tag data:
Total: 3,
Unique: 1,
Max tags: 1,
Tagged words: 3 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 1, 1, 0)

**Title**:
278_PMID32763910.txt_CC.xml,
Words: 210,
Tokens: 358\
Tag data:
Total: 13,
Unique: 3,
Max tags: 1,
Tagged words: 13 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 6, 3, 1)

**Title**:
534_PMID30767087.txt_CC.xml,
Words: 258,
Tokens: 451\
Tag data:
Total: 29,
Unique: 8,
Max tags: 2,
Tagged words: 28 (11%),
Avg tags: 1.04,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 12, 8, 1)

**Title**:
572_PMID30430397.txt_CC.xml,
Words: 215,
Tokens: 408\
Tag data:
Total: 24,
Unique: 9,
Max tags: 1,
Tagged words: 24 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 5, 8, 3)

**Title**:
746_PMID33385331.txt_CC.xml,
Words: 154,
Tokens: 301\
Tag data:
Total: 17,
Unique: 5,
Max tags: 1,
Tagged words: 17 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 7, 5, 0)

**Title**:
441_PMID31819147.txt_CC.xml,
Words: 143,
Tokens: 230\
Tag data:
Total: 14,
Unique: 5,
Max tags: 1,
Tagged words: 14 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 6, 3, 2)

**Title**:
766_PMID31031016.txt_CC.xml,
Words: 142,
Tokens: 295\
Tag data:
Total: 8,
Unique: 3,
Max tags: 1,
Tagged words: 8 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 1, 3, 1)

**Title**:
136_PMID32156776.txt_CC.xml,
Words: 225,
Tokens: 336\
Tag data:
Total: 24,
Unique: 7,
Max tags: 2,
Tagged words: 23 (10%),
Avg tags: 1.04,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 9, 6, 3)

**Title**:
580_PMID30084053.txt_CC.xml,
Words: 215,
Tokens: 409\
Tag data:
Total: 18,
Unique: 8,
Max tags: 2,
Tagged words: 17 (8%),
Avg tags: 1.06,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 1, 7, 3)

**Title**:
156_PMID32816905.txt_CC.xml,
Words: 249,
Tokens: 437\
Tag data:
Total: 16,
Unique: 4,
Max tags: 1,
Tagged words: 16 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 7, 4, 1)

**Title**:
179_PMID32732220.txt_CC.xml,
Words: 259,
Tokens: 541\
Tag data:
Total: 9,
Unique: 6,
Max tags: 1,
Tagged words: 9 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 0, 3, 3)

**Title**:
547_PMID31359205.txt_1_CC.xml,
Words: 150,
Tokens: 279\
Tag data:
Total: 8,
Unique: 5,
Max tags: 1,
Tagged words: 8 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 0, 3, 2)

**Title**:
689_PMID33157038.txt_CC.xml,
Words: 140,
Tokens: 263\
Tag data:
Total: 5,
Unique: 1,
Max tags: 1,
Tagged words: 5 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 3, 1, 0)

**Title**:
252_PMID29674394.txt_CC.xml,
Words: 227,
Tokens: 457\
Tag data:
Total: 14,
Unique: 5,
Max tags: 2,
Tagged words: 13 (6%),
Avg tags: 1.08,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 3, 3, 5)

**Title**:
233_PMID31395741.txt_CC.xml,
Words: 260,
Tokens: 534\
Tag data:
Total: 36,
Unique: 10,
Max tags: 2,
Tagged words: 30 (12%),
Avg tags: 1.2,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (13, 10, 13, 0)

**Title**:
467_PMID29786075.txt_CC.xml,
Words: 230,
Tokens: 394\
Tag data:
Total: 18,
Unique: 6,
Max tags: 1,
Tagged words: 18 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 8, 4, 2)

**Title**:
754_PMID31185211.txt_CC.xml,
Words: 129,
Tokens: 273\
Tag data:
Total: 6,
Unique: 4,
Max tags: 1,
Tagged words: 6 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 2)

**Title**:
357_PMID32908134.txt_CC.xml,
Words: 200,
Tokens: 409\
Tag data:
Total: 12,
Unique: 4,
Max tags: 2,
Tagged words: 9 (4%),
Avg tags: 1.33,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 0, 4, 4)

**Title**:
630_PMID32931733.txt_CC.xml,
Words: 161,
Tokens: 352\
Tag data:
Total: 4,
Unique: 2,
Max tags: 1,
Tagged words: 4 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 1, 1, 1)

**Title**:
731_PMID29622463.txt_CC.xml,
Words: 117,
Tokens: 202\
Tag data:
Total: 4,
Unique: 2,
Max tags: 1,
Tagged words: 4 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 0)

**Title**:
152_PMID33055221.txt_CC.xml,
Words: 200,
Tokens: 373\
Tag data:
Total: 30,
Unique: 9,
Max tags: 2,
Tagged words: 29 (14%),
Avg tags: 1.03,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 12, 8, 2)

**Title**:
243_PMID32943575.txt_CC.xml,
Words: 105,
Tokens: 184\
Tag data:
Total: 8,
Unique: 4,
Max tags: 3,
Tagged words: 6 (6%),
Avg tags: 1.33,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 4)

**Title**:
471_PMID31160717.txt_CC.xml,
Words: 219,
Tokens: 473\
Tag data:
Total: 16,
Unique: 8,
Max tags: 1,
Tagged words: 16 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 3, 5, 3)

**Title**:
451_PMID31296961.txt_CC.xml,
Words: 175,
Tokens: 343\
Tag data:
Total: 5,
Unique: 2,
Max tags: 1,
Tagged words: 5 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 1, 2, 0)

**Title**:
95_PMID31983282.txt_CC.xml,
Words: 191,
Tokens: 389\
Tag data:
Total: 8,
Unique: 3,
Max tags: 1,
Tagged words: 8 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 3, 2, 1)

**Title**:
610_PMID32645325.txt_CC.xml,
Words: 145,
Tokens: 290\
Tag data:
Total: 8,
Unique: 2,
Max tags: 1,
Tagged words: 8 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 4, 2, 0)

**Title**:
541_PMID29936643.txt_CC.xml,
Words: 327,
Tokens: 703\
Tag data:
Total: 5,
Unique: 3,
Max tags: 1,
Tagged words: 5 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 1)

**Title**:
198_PMID32238357.txt_CC.xml,
Words: 252,
Tokens: 472\
Tag data:
Total: 26,
Unique: 8,
Max tags: 2,
Tagged words: 22 (9%),
Avg tags: 1.18,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 11, 6, 3)

**Title**:
363_PMID33004801.txt_CC.xml,
Words: 149,
Tokens: 323\
Tag data:
Total: 9,
Unique: 3,
Max tags: 1,
Tagged words: 9 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 3, 2, 2)

**Title**:
40_PMID31920150.txt_CC.xml,
Words: 165,
Tokens: 314\
Tag data:
Total: 4,
Unique: 2,
Max tags: 1,
Tagged words: 4 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 0)

**Title**:
17_PMID30755075.txt_CC.xml,
Words: 197,
Tokens: 317\
Tag data:
Total: 10,
Unique: 5,
Max tags: 2,
Tagged words: 9 (5%),
Avg tags: 1.11,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 1, 3, 3)

**Title**:
475_PMID33139930.txt_CC.xml,
Words: 218,
Tokens: 387\
Tag data:
Total: 4,
Unique: 2,
Max tags: 1,
Tagged words: 4 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 0)

**Title**:
62_PMID31234698.txt_CC.xml,
Words: 147,
Tokens: 256\
Tag data:
Total: 28,
Unique: 8,
Max tags: 2,
Tagged words: 27 (18%),
Avg tags: 1.04,
MC words: 1\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 14, 6, 2)

**Title**:
245_PMID30463905.txt_CC.xml,
Words: 214,
Tokens: 424\
Tag data:
Total: 12,
Unique: 6,
Max tags: 1,
Tagged words: 12 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 0, 6, 0)

**Title**:
56_PMID32267786.txt_CC.xml,
Words: 110,
Tokens: 200\
Tag data:
Total: 38,
Unique: 6,
Max tags: 1,
Tagged words: 38 (35%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 26, 6, 0)

**Title**:
65_PMID30898011.txt_CC.xml,
Words: 206,
Tokens: 412\
Tag data:
Total: 24,
Unique: 7,
Max tags: 1,
Tagged words: 24 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 9, 6, 3)

**Title**:
49_PMID32160078.txt_CC.xml,
Words: 263,
Tokens: 591\
Tag data:
Total: 22,
Unique: 9,
Max tags: 1,
Tagged words: 22 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 4, 9, 0)

**Title**:
85_PMID32070194.txt_CC.xml,
Words: 209,
Tokens: 412\
Tag data:
Total: 11,
Unique: 3,
Max tags: 2,
Tagged words: 8 (4%),
Avg tags: 1.38,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 2, 3, 3)

**Title**:
557_PMID32632545.txt_CC.xml,
Words: 184,
Tokens: 377\
Tag data:
Total: 15,
Unique: 6,
Max tags: 2,
Tagged words: 13 (7%),
Avg tags: 1.15,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 3, 5, 2)

**Title**:
76_PMID33292048.txt_CC.xml,
Words: 144,
Tokens: 251\
Tag data:
Total: 10,
Unique: 4,
Max tags: 1,
Tagged words: 10 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 3, 3, 1)

**Title**:
474_PMID29666477.txt_CC.xml,
Words: 209,
Tokens: 383\
Tag data:
Total: 4,
Unique: 2,
Max tags: 1,
Tagged words: 4 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 0, 2, 0)

**Title**:
657_PMID32621799.txt_CC.xml,
Words: 159,
Tokens: 253\
Tag data:
Total: 9,
Unique: 4,
Max tags: 1,
Tagged words: 9 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 3, 2, 2)

**Title**:
736_PMID30799057.txt_CC.xml,
Words: 129,
Tokens: 230\
Tag data:
Total: 10,
Unique: 3,
Max tags: 2,
Tagged words: 7 (5%),
Avg tags: 1.43,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 1, 3, 3)

**Title**:
192_PMID32107211.txt_CC.xml,
Words: 231,
Tokens: 432\
Tag data:
Total: 1,
Unique: 1,
Max tags: 1,
Tagged words: 1 (0%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (0, 0, 0, 1)

**Title**:
286_PMID30842215.txt_CC.xml,
Words: 218,
Tokens: 351\
Tag data:
Total: 5,
Unique: 2,
Max tags: 1,
Tagged words: 5 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 3)

**Title**:
184_PMID32928921.txt_CC.xml,
Words: 242,
Tokens: 463\
Tag data:
Total: 23,
Unique: 5,
Max tags: 1,
Tagged words: 23 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 10, 5, 3)

**Title**:
180_PMID32816912.txt_CC.xml,
Words: 256,
Tokens: 454\
Tag data:
Total: 9,
Unique: 3,
Max tags: 1,
Tagged words: 9 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 4, 2, 1)

**Title**:
328_PMID33097691.txt_CC.xml,
Words: 301,
Tokens: 591\
Tag data:
Total: 13,
Unique: 3,
Max tags: 1,
Tagged words: 13 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 7, 3, 0)

**Title**:
27_PMID31208283.txt_CC.xml,
Words: 262,
Tokens: 476\
Tag data:
Total: 51,
Unique: 13,
Max tags: 4,
Tagged words: 45 (17%),
Avg tags: 1.13,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 19, 8, 16)

**Title**:
255_PMID32354837.txt_CC.xml,
Words: 185,
Tokens: 353\
Tag data:
Total: 2,
Unique: 1,
Max tags: 1,
Tagged words: 2 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 0)

**Title**:
543_PMID27878656.txt_CC.xml,
Words: 287,
Tokens: 452\
Tag data:
Total: 31,
Unique: 12,
Max tags: 1,
Tagged words: 31 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 9, 7, 8)

**Title**:
343_PMID33099578.txt_CC.xml,
Words: 212,
Tokens: 358\
Tag data:
Total: 15,
Unique: 7,
Max tags: 1,
Tagged words: 15 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 3, 4, 4)

**Title**:
273_PMID31171699.txt_CC.xml,
Words: 166,
Tokens: 360\
Tag data:
Total: 8,
Unique: 4,
Max tags: 1,
Tagged words: 8 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 1, 3, 1)

**Title**:
452_PMID31209359.txt_CC.xml,
Words: 155,
Tokens: 306\
Tag data:
Total: 3,
Unique: 2,
Max tags: 1,
Tagged words: 3 (2%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 1)

**Title**:
41_PMID30871407.txt_CC.xml,
Words: 208,
Tokens: 463\
Tag data:
Total: 20,
Unique: 9,
Max tags: 1,
Tagged words: 20 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 2, 9, 0)

**Title**:
457_PMID30470795.txt_CC.xml,
Words: 303,
Tokens: 692\
Tag data:
Total: 25,
Unique: 8,
Max tags: 2,
Tagged words: 24 (8%),
Avg tags: 1.04,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 9, 7, 2)

**Title**:
217_PMID31857346.txt_CC.xml,
Words: 166,
Tokens: 316\
Tag data:
Total: 9,
Unique: 3,
Max tags: 1,
Tagged words: 9 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 3, 3, 0)

**Title**:
385_PMID33082307.txt_CC.xml,
Words: 187,
Tokens: 438\
Tag data:
Total: 11,
Unique: 4,
Max tags: 1,
Tagged words: 11 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 3, 3, 2)

**Title**:
57_PMID30982460.txt_CC.xml,
Words: 159,
Tokens: 317\
Tag data:
Total: 2,
Unique: 1,
Max tags: 1,
Tagged words: 2 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 0)

**Title**:
542_PMID31894447.txt_CC.xml,
Words: 223,
Tokens: 386\
Tag data:
Total: 20,
Unique: 9,
Max tags: 1,
Tagged words: 20 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 6, 2, 10)

**Title**:
585_PMID30879165.txt_CC.xml,
Words: 94,
Tokens: 149\
Tag data:
Total: 10,
Unique: 3,
Max tags: 1,
Tagged words: 10 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 3, 3, 1)

**Title**:
216_PMID31467087.txt_CC.xml,
Words: 207,
Tokens: 369\
Tag data:
Total: 11,
Unique: 4,
Max tags: 1,
Tagged words: 11 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 5, 2, 2)

**Title**:
88_PMID30957640.txt_CC.xml,
Words: 245,
Tokens: 510\
Tag data:
Total: 19,
Unique: 11,
Max tags: 2,
Tagged words: 15 (6%),
Avg tags: 1.27,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (0, 0, 0, 19)

**Title**:
402_PMID30737476.txt_CC.xml,
Words: 263,
Tokens: 483\
Tag data:
Total: 20,
Unique: 7,
Max tags: 2,
Tagged words: 18 (7%),
Avg tags: 1.11,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 2, 8, 2)

**Title**:
202_PMID32001510.txt_CC.xml,
Words: 216,
Tokens: 409\
Tag data:
Total: 3,
Unique: 2,
Max tags: 1,
Tagged words: 3 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 0, 1, 1)

**Title**:
412_PMID30742091.txt_CC.xml,
Words: 250,
Tokens: 468\
Tag data:
Total: 35,
Unique: 8,
Max tags: 2,
Tagged words: 27 (11%),
Avg tags: 1.3,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 16, 9, 1)

**Title**:
578_PMID31538267.txt_CC.xml,
Words: 185,
Tokens: 350\
Tag data:
Total: 28,
Unique: 15,
Max tags: 1,
Tagged words: 28 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 4, 5, 14)

**Title**:
488_PMID31907391.txt_CC.xml,
Words: 206,
Tokens: 365\
Tag data:
Total: 35,
Unique: 13,
Max tags: 1,
Tagged words: 35 (17%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (12, 10, 12, 1)

**Title**:
663_PMID33212011.txt_CC.xml,
Words: 162,
Tokens: 300\
Tag data:
Total: 2,
Unique: 1,
Max tags: 1,
Tagged words: 2 (1%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (0, 0, 0, 2)


