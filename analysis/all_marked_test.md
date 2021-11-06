---
title: Rough Analysis of all_marked_test.json
geometry: margin=2cm
---

# General Information

* Num. Entries: 59
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

* Average words: 196.5
* Maximum words: 302
* Minimum words: 105\
* Average tokens: 379.4
* Maximum tokens: 631
* Minimum tokens: 184\
* Entries with over 512 tokens: 8/59, 13.56%


## Tags

### Maximums

* Total tags: 79
* Unique tags: 28
* Max tags: 4
* Tagged words: 75
* Tagged words %: 28.32%
* Avg tags: 1.33
* MC words: 1

### Averages

* Total tags: 20.64
* Unique tags: 8.05
* Max tags: 1.51
* Tagged words: 19.42
* Tagged words %: 9.33%
* Avg tags: 1.05
* MC words: 0.05


## Links

### Maximums

* Total links: 88
* Unique links: 8
* Max links per tag, word: 4, 4
* Linked tags, words: 44, 43
* Linked % tags, words: 100.0%, 16.54%
* Avg links per tag, word: 3.67, 3.67

### Averages

* Total links: 7.47
* Unique links: 0.92
* Max links per tag, word: 0.58, 0.58
* Linked tags, words: 4.69, 4.49
* Linked % tags, words: 15.07%, 1.98%
* Avg links per tag, word: 0.41, 0.42


## Schema

* Maximums (B, I, E, S): 20, 32, 20, 20
* Averages (B, I, E, S): 5.83, 4.92, 5.83, 4.07


## Labels

* Label: Total, Maximum per entry, Average per entry

### Categories

* Perturbing_Action: 371, 31, 6.29
* Context: 920, 60, 15.59
* Effect: 774, 58, 13.12

### Description

* Knock Out: 56, 17, 0.95
* Conditional Knock Out: 14, 6, 0.24
* Knock In: 4, 4, 0.07
* Conditional Knock In: 0, 0, 0.0
* Knock Down: 95, 18, 1.61
* Plasmid Vector: 0, 0, 0.0
* Viral Vector: 0, 0, 0.0
* Pharmacological Inhibition: 80, 9, 1.36
* Decreased Expression Level: 53, 14, 0.9
* Increased Expression Level: 14, 6, 0.24
* Other: 55, 14, 0.93

### Experiment_Type

* Organism: 101, 13, 1.71
* Tumour: 23, 7, 0.39
* Cells: 170, 15, 2.88
* Cell Line: 23, 17, 0.39
* Transformed Cell Line: 93, 22, 1.58
* Primary Culture: 15, 7, 0.25
* Organoid Culture: 6, 6, 0.1
* Cell Transplantation: 0, 0, 0.0
* Xenotransplantation: 27, 12, 0.46
* Other: 0, 0, 0.0
* Not Stated: 2, 2, 0.03

### Species

* Human: 54, 16, 0.92
* Mouse: 58, 9, 0.98
* Rat: 5, 3, 0.08
* Fish: 3, 3, 0.05
* Fly: 6, 6, 0.1
* Yeast: 0, 0, 0.0
* Bacterium: 0, 0, 0.0
* Other: 5, 3, 0.08
* Not Stated: 329, 24, 5.58

### Phenotype

* Adhesion: 0, 0, 0.0
* Apoptosis: 83, 14, 1.41
* Anoikis: 0, 0, 0.0
* Autophagy: 88, 19, 1.49
* Cell Cycle Arrest: 12, 8, 0.2
* Cell Death: 17, 4, 0.29
* Cell Growth: 16, 8, 0.27
* Cell Survival: 15, 3, 0.25
* Colony Formation: 12, 9, 0.2
* Differentiation: 24, 8, 0.41
* Entosis: 0, 0, 0.0
* Epithelial-Mesenchymal Transition: 0, 0, 0.0
* Ferroptosis: 13, 7, 0.22
* Invasion: 6, 2, 0.1
* Metastasis: 20, 10, 0.34
* Migration: 6, 2, 0.1
* Mitophagy: 10, 7, 0.17
* Necroptosis: 5, 5, 0.08
* Necrosis: 2, 2, 0.03
* Netosis: 0, 0, 0.0
* Oncosis: 0, 0, 0.0
* Proliferation: 34, 10, 0.58
* Pyroptosis: 2, 2, 0.03
* Quiescence: 0, 0, 0.0
* Self-Renewal: 3, 3, 0.05
* Senescence: 0, 0, 0.0
* Transformation: 0, 0, 0.0
* Tumour Growth: 17, 6, 0.29
* Tumourigenesis: 2, 2, 0.03

### Activity

* Causes: 75, 12, 1.27
* Inhibits: 79, 14, 1.34
* Increases: 93, 13, 1.58
* Decreases: 91, 19, 1.54
* Regulates: 16, 8, 0.27
* No Effect: 8, 4, 0.14
* Not Stated: 25, 9, 0.42


# Information on each entry

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
242_PMID29563184.txt_CC.xml,
Words: 231,
Tokens: 432\
Tag data:
Total: 23,
Unique: 9,
Max tags: 1,
Tagged words: 23 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (39.13%), 9 (3.9%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (8, 6, 8, 1)

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
337_PMID33154352.txt_CC.xml,
Words: 173,
Tokens: 439\
Tag data:
Total: 50,
Unique: 23,
Max tags: 4,
Tagged words: 47 (27%),
Avg tags: 1.06,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (14.0%), 7 (4.05%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (15, 4, 15, 16)

**Title**:
114_PMID32312833.txt_CC.xml,
Words: 176,
Tokens: 367\
Tag data:
Total: 24,
Unique: 9,
Max tags: 2,
Tagged words: 22 (12%),
Avg tags: 1.09,
MC words: 0\
Link data:
Total: 58,
Unique: 6,
Max links (tag, word): (4, 4),
Linked (tags, words): (24 (100.0%), 22 (12.5%))\
Avg links (tag, word): (2.42, 2.64),
Schema counts (B, I, E, S): (5, 6, 5, 8)

**Title**:
51_PMID31007149.txt_CC.xml,
Words: 267,
Tokens: 568\
Tag data:
Total: 79,
Unique: 23,
Max tags: 2,
Tagged words: 75 (28%),
Avg tags: 1.05,
MC words: 0\
Link data:
Total: 88,
Unique: 8,
Max links (tag, word): (4, 4),
Linked (tags, words): (24 (30.38%), 24 (8.99%))\
Avg links (tag, word): (3.67, 3.67),
Schema counts (B, I, E, S): (19, 32, 19, 9)

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
24_PMID30859901.txt_CC.xml,
Words: 260,
Tokens: 605\
Tag data:
Total: 46,
Unique: 23,
Max tags: 2,
Tagged words: 43 (17%),
Avg tags: 1.07,
MC words: 0\
Link data:
Total: 65,
Unique: 8,
Max links (tag, word): (4, 4),
Linked (tags, words): (36 (78.26%), 33 (12.69%))\
Avg links (tag, word): (1.81, 1.97),
Schema counts (B, I, E, S): (8, 10, 8, 20)

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
73_PMID30444165.txt_CC.xml,
Words: 260,
Tokens: 518\
Tag data:
Total: 65,
Unique: 28,
Max tags: 2,
Tagged words: 60 (23%),
Avg tags: 1.08,
MC words: 1\
Link data:
Total: 54,
Unique: 8,
Max links (tag, word): (2, 2),
Linked (tags, words): (44 (67.69%), 43 (16.54%))\
Avg links (tag, word): (1.23, 1.26),
Schema counts (B, I, E, S): (20, 12, 20, 13)

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
42_PMID31276435.txt_CC.xml,
Words: 184,
Tokens: 368\
Tag data:
Total: 20,
Unique: 8,
Max tags: 1,
Tagged words: 20 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 16,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (16 (80.0%), 16 (8.7%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 5, 7, 1)

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
397_PMID33239622.txt_CC.xml,
Words: 196,
Tokens: 327\
Tag data:
Total: 24,
Unique: 9,
Max tags: 2,
Tagged words: 22 (11%),
Avg tags: 1.09,
MC words: 0\
Link data:
Total: 14,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (10 (41.67%), 9 (4.59%))\
Avg links (tag, word): (1.4, 1.56),
Schema counts (B, I, E, S): (8, 2, 8, 6)

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
395_PMID33243998.txt_CC.xml,
Words: 237,
Tokens: 443\
Tag data:
Total: 58,
Unique: 17,
Max tags: 3,
Tagged words: 49 (21%),
Avg tags: 1.18,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (15.52%), 9 (3.8%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (15, 21, 15, 7)

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
308_PMID33097690.txt_CC.xml,
Words: 302,
Tokens: 572\
Tag data:
Total: 34,
Unique: 16,
Max tags: 2,
Tagged words: 33 (11%),
Avg tags: 1.03,
MC words: 0\
Link data:
Total: 28,
Unique: 6,
Max links (tag, word): (4, 4),
Linked (tags, words): (19 (55.88%), 18 (5.96%))\
Avg links (tag, word): (1.47, 1.56),
Schema counts (B, I, E, S): (5, 9, 5, 15)

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
370_PMID33277461.txt_CC.xml,
Words: 264,
Tokens: 589\
Tag data:
Total: 67,
Unique: 24,
Max tags: 2,
Tagged words: 66 (25%),
Avg tags: 1.02,
MC words: 1\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (13.43%), 9 (3.41%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (19, 21, 19, 8)

**Title**:
530_PMID30796611.txt_CC.xml,
Words: 219,
Tokens: 349\
Tag data:
Total: 41,
Unique: 18,
Max tags: 2,
Tagged words: 38 (17%),
Avg tags: 1.08,
MC words: 1\
Link data:
Total: 13,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (13 (31.71%), 13 (5.94%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (17, 5, 17, 2)

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
224_PMID30692208.txt_CC.xml,
Words: 206,
Tokens: 380\
Tag data:
Total: 25,
Unique: 4,
Max tags: 2,
Tagged words: 21 (10%),
Avg tags: 1.19,
MC words: 0\
Link data:
Total: 31,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (25 (100.0%), 21 (10.19%))\
Avg links (tag, word): (1.24, 1.48),
Schema counts (B, I, E, S): (6, 12, 6, 1)

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
84_PMID32075509.txt_CC.xml,
Words: 265,
Tokens: 463\
Tag data:
Total: 37,
Unique: 13,
Max tags: 1,
Tagged words: 37 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 20,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (12 (32.43%), 12 (4.53%))\
Avg links (tag, word): (1.67, 1.67),
Schema counts (B, I, E, S): (11, 12, 11, 3)

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
93_PMID31517566.txt_CC.xml,
Words: 258,
Tokens: 501\
Tag data:
Total: 11,
Unique: 5,
Max tags: 1,
Tagged words: 11 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (72.73%), 8 (3.1%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 3, 3, 2)

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
789_PMID29805077.txt_CC.xml,
Words: 132,
Tokens: 280\
Tag data:
Total: 6,
Unique: 3,
Max tags: 1,
Tagged words: 6 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (100.0%), 6 (4.55%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (2, 0, 2, 2)

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
522_PMID30680482.txt_CC.xml,
Words: 193,
Tokens: 447\
Tag data:
Total: 37,
Unique: 11,
Max tags: 2,
Tagged words: 33 (17%),
Avg tags: 1.12,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (16.22%), 6 (3.11%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (10, 10, 10, 7)


