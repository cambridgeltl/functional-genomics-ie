---
title: Rough Analysis of v2_all_marked_train.json
geometry: margin=2cm
---

# General Information

* Num. Entries: 530
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

* Average words: 204.2
* Maximum words: 353
* Minimum words: 9\
* Average tokens: 383.8
* Maximum tokens: 700
* Minimum tokens: 11\
* Entries with over 512 tokens: 64/530, 12.08%


## Tags

### Maximums

* Total tags: 61
* Unique tags: 35
* Max tags: 2
* Tagged words: 61
* Tagged words %: 30.95%
* Avg tags: 1.06
* MC words: 2

### Averages

* Total tags: 17.61
* Unique tags: 9.08
* Max tags: 1.02
* Tagged words: 17.58
* Tagged words %: 8.58%
* Avg tags: 1.0
* MC words: 0.02


## Links

### Maximums

* Total links: 98
* Unique links: 11
* Max links per tag, word: 6, 6
* Linked tags, words: 51, 51
* Linked % tags, words: 100.0%, 18.96%
* Avg links per tag, word: 2.88, 2.88

### Averages

* Total links: 5.14
* Unique links: 0.65
* Max links per tag, word: 0.5, 0.5
* Linked tags, words: 3.69, 3.68
* Linked % tags, words: 14.93%, 1.75%
* Avg links per tag, word: 0.37, 0.37


## Schema

* Maximums (B, I, E, S): 17, 29, 17, 23
* Averages (B, I, E, S): 4.38, 4.15, 4.39, 4.69


## Labels

* Label: Total, Maximum per entry, Average per entry

### Categories

* Perturbing_Action: 3131, 48, 5.91
* Context: 3784, 32, 7.14
* Effect: 1002, 11, 1.89
* Phenotype: 1414, 17, 2.67

### Perturbing_Action

* -: 0, 0, 0.0
* Gene Loss-Of-Function: 1137, 24, 2.15
* Gene Gain-Of-Function: 477, 24, 0.9
* Rnai/Knockdown: 493, 20, 0.93
* Pharmacological Inhibition: 616, 20, 1.16
* Pharmacological Augmentation: 58, 15, 0.11
* Other: 350, 25, 0.66

### Context

* -: 2, 2, 0.0
* Patient: 18, 4, 0.03
* Organism: 404, 11, 0.76
* Tissue/Organ: 201, 15, 0.38
* Neoplasm: 363, 11, 0.68
* Graft: 0, 0, 0.0
* Xenograft: 155, 9, 0.29
* Cells: 1382, 28, 2.61
* Transformed Cells: 790, 17, 1.49
* Organoid: 38, 6, 0.07
* In Vitro: 209, 6, 0.39
* In Vivo: 222, 4, 0.42

### Effect

* -: 3, 3, 0.01
* Positive: 512, 9, 0.97
* Negative: 390, 6, 0.74
* Regulates: 28, 3, 0.05
* Rescues: 27, 4, 0.05
* No Effect: 42, 6, 0.08

### Phenotype

* -: 1, 1, 0.0
* Adhesion: 3, 2, 0.01
* Apoptosis: 228, 8, 0.43
* Anoikis: 0, 0, 0.0
* Autophagy: 180, 8, 0.34
* Cell Cycle Arrest: 61, 7, 0.12
* Cell Death: 137, 12, 0.26
* Cell Growth: 41, 6, 0.08
* Cell Survival: 34, 7, 0.06
* Colony Formation: 16, 4, 0.03
* Differentiation: 39, 3, 0.07
* Entosis: 0, 0, 0.0
* Epithelial-Mesenchymal Transition: 38, 6, 0.07
* Ferroptosis: 43, 8, 0.08
* Invasion: 31, 5, 0.06
* Metastasis: 80, 7, 0.15
* Migration: 39, 3, 0.07
* Mitophagy: 24, 5, 0.05
* Necroptosis: 18, 4, 0.03
* Necrosis: 11, 4, 0.02
* Oncosis: 10, 6, 0.02
* Proliferation: 101, 5, 0.19
* Pyroptosis: 9, 2, 0.02
* Quiescence: 4, 2, 0.01
* Self-Renewal: 10, 3, 0.02
* Senescence: 26, 4, 0.05
* Transformation: 7, 2, 0.01
* Tumour Growth: 115, 5, 0.22
* Tumourigenesis: 69, 6, 0.13
* Tumour Initiation: 10, 2, 0.02
* Tumour Progression: 12, 2, 0.02
* Tumour Regression: 17, 5, 0.03


# Information on each entry

**Title**:
390_PMID33082333.txt_CC2.xml,
Words: 191,
Tokens: 343\
Tag data:
Total: 25,
Unique: 11,
Max tags: 1,
Tagged words: 25 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 10,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (10 (40.0%), 10 (5.24%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (8, 6, 8, 3)

**Title**:
131_PMID32265223.txt_CC2.xml,
Words: 166,
Tokens: 366\
Tag data:
Total: 12,
Unique: 3,
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
Schema counts (B, I, E, S): (2, 7, 2, 1)

**Title**:
438_PMID31320749.txt_CC2.xml,
Words: 274,
Tokens: 536\
Tag data:
Total: 42,
Unique: 21,
Max tags: 1,
Tagged words: 42 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 41,
Unique: 6,
Max links (tag, word): (3, 3),
Linked (tags, words): (32 (76.19%), 32 (11.68%))\
Avg links (tag, word): (1.28, 1.28),
Schema counts (B, I, E, S): (10, 11, 10, 11)

**Title**:
318_PMID32978367.txt_CC2.xml,
Words: 232,
Tokens: 461\
Tag data:
Total: 50,
Unique: 27,
Max tags: 1,
Tagged words: 50 (22%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (12, 11, 12, 15)

**Title**:
630_PMID32931733.txt_1_CC2.xml,
Words: 161,
Tokens: 352\
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
216_PMID31467087.txt_CC2.xml,
Words: 207,
Tokens: 369\
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
Schema counts (B, I, E, S): (3, 7, 3, 2)

**Title**:
412_PMID30742091.txt_CC2.xml,
Words: 250,
Tokens: 468\
Tag data:
Total: 27,
Unique: 7,
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
Schema counts (B, I, E, S): (4, 16, 4, 3)

**Title**:
581_PMID32468177.txt_CC2.xml,
Words: 231,
Tokens: 427\
Tag data:
Total: 16,
Unique: 9,
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
Schema counts (B, I, E, S): (3, 4, 3, 6)

**Title**:
503_PMID29705943.txt_CC2.xml,
Words: 265,
Tokens: 509\
Tag data:
Total: 13,
Unique: 8,
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
Schema counts (B, I, E, S): (3, 2, 3, 5)

**Title**:
39_PMID30676840.txt_CC2.xml,
Words: 261,
Tokens: 468\
Tag data:
Total: 14,
Unique: 6,
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
Schema counts (B, I, E, S): (5, 3, 5, 1)

**Title**:
8_PMID30523761.txt_CC2.xml,
Words: 265,
Tokens: 510\
Tag data:
Total: 18,
Unique: 9,
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
Schema counts (B, I, E, S): (4, 5, 4, 5)

**Title**:
727_PMID30991027.txt_CC2.xml,
Words: 113,
Tokens: 222\
Tag data:
Total: 32,
Unique: 12,
Max tags: 2,
Tagged words: 31 (27%),
Avg tags: 1.03,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 14, 6, 6)

**Title**:
367_PMID33087696.txt_CC2.xml,
Words: 261,
Tokens: 463\
Tag data:
Total: 21,
Unique: 15,
Max tags: 1,
Tagged words: 21 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (23.81%), 5 (1.92%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 1, 5, 10)

**Title**:
188_PMID32561531.txt_CC2.xml,
Words: 180,
Tokens: 267\
Tag data:
Total: 14,
Unique: 6,
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
Schema counts (B, I, E, S): (5, 3, 5, 1)

**Title**:
452_PMID31209359.txt_CC2.xml,
Words: 155,
Tokens: 306\
Tag data:
Total: 5,
Unique: 5,
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
Schema counts (B, I, E, S): (0, 0, 0, 5)

**Title**:
133_PMID32828922.txt_CC2.xml,
Words: 247,
Tokens: 480\
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
435_PMID31097787.txt_CC2.xml,
Words: 170,
Tokens: 318\
Tag data:
Total: 28,
Unique: 15,
Max tags: 1,
Tagged words: 28 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 17,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (14 (50.0%), 14 (8.24%))\
Avg links (tag, word): (1.21, 1.21),
Schema counts (B, I, E, S): (5, 8, 5, 10)

**Title**:
34_PMID31286822.txt_CC2.xml,
Words: 264,
Tokens: 535\
Tag data:
Total: 14,
Unique: 8,
Max tags: 1,
Tagged words: 14 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (50.0%), 7 (2.65%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 3, 3, 5)

**Title**:
485_PMID32001780.txt_CC2.xml,
Words: 236,
Tokens: 406\
Tag data:
Total: 26,
Unique: 11,
Max tags: 1,
Tagged words: 26 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (34.62%), 9 (3.81%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (9, 6, 9, 2)

**Title**:
578_PMID31538267.txt_CC2.xml,
Words: 185,
Tokens: 350\
Tag data:
Total: 24,
Unique: 20,
Max tags: 1,
Tagged words: 24 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 1, 3, 17)

**Title**:
274_PMID30819820.txt_CC2.xml,
Words: 206,
Tokens: 432\
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
Schema counts (B, I, E, S): (1, 3, 1, 1)

**Title**:
15_PMID32249716.txt_CC2.xml,
Words: 240,
Tokens: 429\
Tag data:
Total: 26,
Unique: 17,
Max tags: 1,
Tagged words: 26 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 20,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (18 (69.23%), 18 (7.5%))\
Avg links (tag, word): (1.11, 1.11),
Schema counts (B, I, E, S): (5, 4, 5, 12)

**Title**:
528_PMID29777330.txt_CC2.xml,
Words: 353,
Tokens: 700\
Tag data:
Total: 16,
Unique: 9,
Max tags: 1,
Tagged words: 16 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 2, 5, 4)

**Title**:
115_PMID32661137.txt_CC2.xml,
Words: 222,
Tokens: 375\
Tag data:
Total: 49,
Unique: 15,
Max tags: 1,
Tagged words: 49 (22%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 24,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (24 (48.98%), 24 (10.81%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (14, 20, 14, 1)

**Title**:
748_PMID32243847.txt_CC2.xml,
Words: 133,
Tokens: 281\
Tag data:
Total: 19,
Unique: 10,
Max tags: 1,
Tagged words: 19 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 14,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (8 (42.11%), 8 (6.02%))\
Avg links (tag, word): (1.75, 1.75),
Schema counts (B, I, E, S): (4, 5, 4, 6)

**Title**:
797_PMID29249692.txt_CC2.xml,
Words: 126,
Tokens: 305\
Tag data:
Total: 20,
Unique: 13,
Max tags: 1,
Tagged words: 20 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (35.0%), 7 (5.56%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 1, 6, 7)

**Title**:
659_PMID33152263.txt_CC2.xml,
Words: 164,
Tokens: 265\
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
Schema counts (B, I, E, S): (1, 0, 1, 2)

**Title**:
227_PMID32943573.txt_CC2.xml,
Words: 271,
Tokens: 442\
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
Schema counts (B, I, E, S): (4, 7, 4, 5)

**Title**:
398_PMID33311488.txt_CC2.xml,
Words: 162,
Tokens: 292\
Tag data:
Total: 16,
Unique: 8,
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
Schema counts (B, I, E, S): (5, 3, 5, 3)

**Title**:
767_PMID30686770.txt_CC2.xml,
Words: 128,
Tokens: 261\
Tag data:
Total: 17,
Unique: 9,
Max tags: 1,
Tagged words: 17 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 10,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (10 (58.82%), 10 (7.81%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 2, 6, 3)

**Title**:
539_PMID31473844.txt_CC2.xml,
Words: 289,
Tokens: 553\
Tag data:
Total: 24,
Unique: 10,
Max tags: 1,
Tagged words: 24 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 11,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (11 (45.83%), 11 (3.81%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 10, 4, 6)

**Title**:
41_PMID30871407.txt_CC2.xml,
Words: 208,
Tokens: 463\
Tag data:
Total: 20,
Unique: 10,
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
Schema counts (B, I, E, S): (8, 2, 8, 2)

**Title**:
241_PMID32115408.txt_CC2.xml,
Words: 218,
Tokens: 429\
Tag data:
Total: 29,
Unique: 15,
Max tags: 1,
Tagged words: 29 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 7, 7, 8)

**Title**:
571_PMID31583496.txt_CC2.xml,
Words: 213,
Tokens: 399\
Tag data:
Total: 47,
Unique: 27,
Max tags: 1,
Tagged words: 47 (22%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 52,
Unique: 8,
Max links (tag, word): (4, 4),
Linked (tags, words): (21 (44.68%), 21 (9.86%))\
Avg links (tag, word): (2.48, 2.48),
Schema counts (B, I, E, S): (12, 8, 12, 15)

**Title**:
463_PMID31511651.txt_CC2.xml,
Words: 202,
Tokens: 370\
Tag data:
Total: 26,
Unique: 15,
Max tags: 1,
Tagged words: 26 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 27,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (16 (61.54%), 16 (7.92%))\
Avg links (tag, word): (1.69, 1.69),
Schema counts (B, I, E, S): (8, 3, 8, 7)

**Title**:
384_PMID32968045.txt_CC2.xml,
Words: 226,
Tokens: 366\
Tag data:
Total: 27,
Unique: 16,
Max tags: 1,
Tagged words: 27 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (25.93%), 7 (3.1%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (9, 2, 9, 7)

**Title**:
256_PMID30006480.txt_CC2.xml,
Words: 176,
Tokens: 332\
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
Schema counts (B, I, E, S): (1, 0, 1, 2)

**Title**:
154_PMID32747363.txt_CC2.xml,
Words: 249,
Tokens: 436\
Tag data:
Total: 25,
Unique: 13,
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
Schema counts (B, I, E, S): (7, 5, 7, 6)

**Title**:
383_PMID32963254.txt_CC2.xml,
Words: 157,
Tokens: 278\
Tag data:
Total: 11,
Unique: 6,
Max tags: 1,
Tagged words: 11 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (54.55%), 6 (3.82%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 1, 4, 2)

**Title**:
453_PMID30903102.txt_CC2.xml,
Words: 152,
Tokens: 250\
Tag data:
Total: 13,
Unique: 9,
Max tags: 1,
Tagged words: 13 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 0, 4, 5)

**Title**:
544_PMID32100210.txt_CC2.xml,
Words: 238,
Tokens: 416\
Tag data:
Total: 11,
Unique: 10,
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
Schema counts (B, I, E, S): (1, 0, 1, 9)

**Title**:
457_PMID30470795.txt_CC2.xml,
Words: 303,
Tokens: 692\
Tag data:
Total: 20,
Unique: 4,
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
Schema counts (B, I, E, S): (4, 12, 4, 0)

**Title**:
379_PMID33311447.txt_CC2.xml,
Words: 211,
Tokens: 357\
Tag data:
Total: 3,
Unique: 1,
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
Schema counts (B, I, E, S): (1, 1, 1, 0)

**Title**:
219_PMID29945888.txt_CC2.xml,
Words: 228,
Tokens: 397\
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
400_PMID33093470.txt_CC2.xml,
Words: 301,
Tokens: 598\
Tag data:
Total: 28,
Unique: 17,
Max tags: 1,
Tagged words: 28 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 18,
Unique: 3,
Max links (tag, word): (1, 1),
Linked (tags, words): (18 (64.29%), 18 (5.98%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 4, 7, 10)

**Title**:
592_PMID30426280.txt_CC2.xml,
Words: 148,
Tokens: 243\
Tag data:
Total: 11,
Unique: 5,
Max tags: 1,
Tagged words: 11 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 19,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (11 (100.0%), 11 (7.43%))\
Avg links (tag, word): (1.73, 1.73),
Schema counts (B, I, E, S): (3, 3, 3, 2)

**Title**:
102_PMID32054768.txt_CC2.xml,
Words: 234,
Tokens: 429\
Tag data:
Total: 46,
Unique: 16,
Max tags: 1,
Tagged words: 46 (20%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 54,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (40 (86.96%), 40 (17.09%))\
Avg links (tag, word): (1.35, 1.35),
Schema counts (B, I, E, S): (11, 19, 11, 5)

**Title**:
742_PMID32679107.txt_CC2.xml,
Words: 121,
Tokens: 224\
Tag data:
Total: 14,
Unique: 5,
Max tags: 1,
Tagged words: 14 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 25,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (14 (100.0%), 14 (11.57%))\
Avg links (tag, word): (1.79, 1.79),
Schema counts (B, I, E, S): (2, 7, 2, 3)

**Title**:
725_PMID31679823.txt_CC2.xml,
Words: 123,
Tokens: 233\
Tag data:
Total: 12,
Unique: 8,
Max tags: 1,
Tagged words: 12 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 16,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (9 (75.0%), 9 (7.32%))\
Avg links (tag, word): (1.78, 1.78),
Schema counts (B, I, E, S): (2, 2, 2, 6)

**Title**:
269_PMID32561546.txt_CC2.xml,
Words: 145,
Tokens: 207\
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
Schema counts (B, I, E, S): (2, 1, 2, 1)

**Title**:
161_PMID32816909.txt_CC2.xml,
Words: 253,
Tokens: 488\
Tag data:
Total: 39,
Unique: 14,
Max tags: 1,
Tagged words: 39 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 14,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (14 (35.9%), 14 (5.53%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (10, 15, 10, 4)

**Title**:
518_PMID32146618.txt_CC2.xml,
Words: 9,
Tokens: 11\
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
107_PMID31911550.txt_CC2.xml,
Words: 181,
Tokens: 331\
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
58_PMID31821607.txt_CC2.xml,
Words: 185,
Tokens: 357\
Tag data:
Total: 16,
Unique: 9,
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
Schema counts (B, I, E, S): (4, 3, 4, 5)

**Title**:
309_PMID33130824.txt_CC2.xml,
Words: 302,
Tokens: 572\
Tag data:
Total: 18,
Unique: 11,
Max tags: 1,
Tagged words: 18 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 26,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (17 (94.44%), 17 (5.63%))\
Avg links (tag, word): (1.53, 1.53),
Schema counts (B, I, E, S): (3, 4, 3, 8)

**Title**:
740_PMID31408619.txt_CC2.xml,
Words: 130,
Tokens: 236\
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
224_PMID30692208.txt_CC2.xml,
Words: 206,
Tokens: 380\
Tag data:
Total: 17,
Unique: 5,
Max tags: 1,
Tagged words: 17 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 26,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (17 (100.0%), 17 (8.25%))\
Avg links (tag, word): (1.53, 1.53),
Schema counts (B, I, E, S): (5, 7, 5, 0)

**Title**:
3_PMID31451060.txt_CC2.xml,
Words: 210,
Tokens: 398\
Tag data:
Total: 19,
Unique: 12,
Max tags: 1,
Tagged words: 19 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 12,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (10 (52.63%), 10 (4.76%))\
Avg links (tag, word): (1.2, 1.2),
Schema counts (B, I, E, S): (5, 2, 5, 7)

**Title**:
567_PMID27770267.txt_CC2.xml,
Words: 286,
Tokens: 479\
Tag data:
Total: 38,
Unique: 18,
Max tags: 1,
Tagged words: 38 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 12, 8, 10)

**Title**:
632_PMID33031745.txt_CC2.xml,
Words: 171,
Tokens: 334\
Tag data:
Total: 18,
Unique: 3,
Max tags: 1,
Tagged words: 18 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 13, 2, 1)

**Title**:
623_PMID33242418.txt_CC2.xml,
Words: 156,
Tokens: 243\
Tag data:
Total: 29,
Unique: 13,
Max tags: 1,
Tagged words: 29 (19%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 14,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (14 (48.28%), 14 (8.97%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (8, 8, 8, 5)

**Title**:
428_PMID31802034.txt_CC2.xml,
Words: 210,
Tokens: 435\
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
391_PMID32943609.txt_CC2.xml,
Words: 225,
Tokens: 413\
Tag data:
Total: 21,
Unique: 11,
Max tags: 1,
Tagged words: 21 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (38.1%), 8 (3.56%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 6, 4, 7)

**Title**:
252_PMID29674394.txt_CC2.xml,
Words: 227,
Tokens: 457\
Tag data:
Total: 4,
Unique: 4,
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
690_PMID33065030.txt_CC2.xml,
Words: 148,
Tokens: 298\
Tag data:
Total: 6,
Unique: 5,
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
Schema counts (B, I, E, S): (1, 0, 1, 4)

**Title**:
140_PMID33239431.txt_CC2.xml,
Words: 229,
Tokens: 431\
Tag data:
Total: 20,
Unique: 11,
Max tags: 1,
Tagged words: 20 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 12,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (9 (45.0%), 9 (3.93%))\
Avg links (tag, word): (1.33, 1.33),
Schema counts (B, I, E, S): (8, 1, 8, 3)

**Title**:
464_PMID31645676.txt_CC2.xml,
Words: 207,
Tokens: 382\
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
Schema counts (B, I, E, S): (3, 3, 3, 2)

**Title**:
240_PMID32241802.txt_CC2.xml,
Words: 138,
Tokens: 254\
Tag data:
Total: 12,
Unique: 5,
Max tags: 1,
Tagged words: 12 (9%),
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
49_PMID32160078.txt_CC2.xml,
Words: 263,
Tokens: 591\
Tag data:
Total: 8,
Unique: 8,
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
Schema counts (B, I, E, S): (0, 0, 0, 8)

**Title**:
762_PMID31821784.txt_CC2.xml,
Words: 141,
Tokens: 276\
Tag data:
Total: 28,
Unique: 10,
Max tags: 1,
Tagged words: 28 (20%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 13, 5, 5)

**Title**:
303_PMID33024077.txt_CC2.xml,
Words: 147,
Tokens: 242\
Tag data:
Total: 7,
Unique: 5,
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
Schema counts (B, I, E, S): (2, 0, 2, 3)

**Title**:
469_PMID32144381.txt_CC2.xml,
Words: 270,
Tokens: 535\
Tag data:
Total: 11,
Unique: 8,
Max tags: 1,
Tagged words: 11 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 0, 3, 5)

**Title**:
524_PMID32418060.txt_CC2.xml,
Words: 219,
Tokens: 382\
Tag data:
Total: 12,
Unique: 5,
Max tags: 1,
Tagged words: 12 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 10,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (10 (83.33%), 10 (4.57%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 3, 4, 1)

**Title**:
186_PMID32098780.txt_CC2.xml,
Words: 204,
Tokens: 385\
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
Schema counts (B, I, E, S): (4, 1, 4, 1)

**Title**:
44_PMID31818185.txt_CC2.xml,
Words: 249,
Tokens: 455\
Tag data:
Total: 31,
Unique: 17,
Max tags: 1,
Tagged words: 31 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (19.35%), 6 (2.41%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (8, 6, 8, 9)

**Title**:
432_PMID30683918.txt_CC2.xml,
Words: 257,
Tokens: 572\
Tag data:
Total: 29,
Unique: 14,
Max tags: 1,
Tagged words: 29 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (11, 4, 11, 3)

**Title**:
502_PMID28289909.txt_CC2.xml,
Words: 242,
Tokens: 489\
Tag data:
Total: 41,
Unique: 17,
Max tags: 1,
Tagged words: 41 (17%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (12, 12, 12, 5)

**Title**:
363_PMID33004801.txt_CC2.xml,
Words: 149,
Tokens: 323\
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
750_PMID32916126.txt_CC2.xml,
Words: 138,
Tokens: 235\
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
Schema counts (B, I, E, S): (2, 1, 2, 2)

**Title**:
462_PMID31767934.txt_CC2.xml,
Words: 179,
Tokens: 320\
Tag data:
Total: 18,
Unique: 7,
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
Schema counts (B, I, E, S): (5, 6, 5, 2)

**Title**:
97_PMID32403970.txt_CC2.xml,
Words: 210,
Tokens: 397\
Tag data:
Total: 16,
Unique: 10,
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
Schema counts (B, I, E, S): (4, 2, 4, 6)

**Title**:
165_PMID32303578.txt_CC2.xml,
Words: 269,
Tokens: 484\
Tag data:
Total: 27,
Unique: 15,
Max tags: 1,
Tagged words: 27 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 10,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (10 (37.04%), 10 (3.72%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (8, 4, 8, 7)

**Title**:
793_PMID31287991.txt_CC2.xml,
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
591_PMID32901335.txt_CC2.xml,
Words: 145,
Tokens: 265\
Tag data:
Total: 28,
Unique: 15,
Max tags: 1,
Tagged words: 28 (19%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 33,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (13 (46.43%), 13 (8.97%))\
Avg links (tag, word): (2.54, 2.54),
Schema counts (B, I, E, S): (4, 9, 4, 11)

**Title**:
454_PMID32704090.txt_CC2.xml,
Words: 324,
Tokens: 653\
Tag data:
Total: 12,
Unique: 6,
Max tags: 1,
Tagged words: 12 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (58.33%), 7 (2.16%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 1, 5, 1)

**Title**:
149_PMD33093168.txt_CC2.xml,
Words: 226,
Tokens: 399\
Tag data:
Total: 20,
Unique: 10,
Max tags: 1,
Tagged words: 20 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (35.0%), 7 (3.1%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 3, 7, 3)

**Title**:
116_PMID32193290.txt_CC2.xml,
Words: 159,
Tokens: 285\
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
Schema counts (B, I, E, S): (3, 4, 3, 4)

**Title**:
478_PMID32764647.txt_CC2.xml,
Words: 246,
Tokens: 443\
Tag data:
Total: 14,
Unique: 5,
Max tags: 1,
Tagged words: 14 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (42.86%), 6 (2.44%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 6, 3, 2)

**Title**:
751_PMID30205049.txt_CC2.xml,
Words: 128,
Tokens: 236\
Tag data:
Total: 9,
Unique: 6,
Max tags: 1,
Tagged words: 9 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (66.67%), 6 (4.69%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 0, 3, 3)

**Title**:
238_PMID31753913.txt_CC2.xml,
Words: 202,
Tokens: 359\
Tag data:
Total: 5,
Unique: 1,
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
Schema counts (B, I, E, S): (1, 3, 1, 0)

**Title**:
89_PMID32264736.txt_CC2.xml,
Words: 164,
Tokens: 345\
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
106_PMID32029550.txt_CC2.xml,
Words: 284,
Tokens: 486\
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
Schema counts (B, I, E, S): (4, 4, 4, 5)

**Title**:
423_PMID32203171.txt_CC2.xml,
Words: 180,
Tokens: 256\
Tag data:
Total: 12,
Unique: 8,
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
Schema counts (B, I, E, S): (4, 0, 4, 4)

**Title**:
325_PMID33303756.txt_CC2.xml,
Words: 266,
Tokens: 485\
Tag data:
Total: 18,
Unique: 6,
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
Schema counts (B, I, E, S): (4, 8, 4, 2)

**Title**:
422_PMID31819158.txt_CC2.xml,
Words: 251,
Tokens: 479\
Tag data:
Total: 7,
Unique: 2,
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
Schema counts (B, I, E, S): (1, 4, 1, 1)

**Title**:
93_PMID31517566.txt_CC2.xml,
Words: 258,
Tokens: 501\
Tag data:
Total: 6,
Unique: 3,
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
Schema counts (B, I, E, S): (1, 2, 1, 2)

**Title**:
513_PMID32627119.txt_CC2.xml,
Words: 264,
Tokens: 527\
Tag data:
Total: 14,
Unique: 12,
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
Schema counts (B, I, E, S): (2, 0, 2, 10)

**Title**:
235_PMID32217665.txt_CC2.xml,
Words: 166,
Tokens: 301\
Tag data:
Total: 16,
Unique: 8,
Max tags: 1,
Tagged words: 16 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 11,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (11 (68.75%), 11 (6.63%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 4, 4, 4)

**Title**:
263_PMID32381628.txt_CC2.xml,
Words: 165,
Tokens: 286\
Tag data:
Total: 15,
Unique: 5,
Max tags: 1,
Tagged words: 15 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 8, 2, 3)

**Title**:
488_PMID31907391.txt_CC2.xml,
Words: 206,
Tokens: 365\
Tag data:
Total: 36,
Unique: 14,
Max tags: 1,
Tagged words: 36 (17%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (12, 10, 12, 2)

**Title**:
598_PMID25218423.txt_CC2.xml,
Words: 220,
Tokens: 456\
Tag data:
Total: 29,
Unique: 21,
Max tags: 1,
Tagged words: 29 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 16,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (12 (41.38%), 12 (5.45%))\
Avg links (tag, word): (1.33, 1.33),
Schema counts (B, I, E, S): (6, 2, 6, 15)

**Title**:
484_PMID32346137.txt_1_CC2.xml,
Words: 188,
Tokens: 387\
Tag data:
Total: 28,
Unique: 17,
Max tags: 1,
Tagged words: 28 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 17,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (17 (60.71%), 17 (9.04%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 4, 7, 10)

**Title**:
357_PMID32908134.txt_CC2.xml,
Words: 200,
Tokens: 409\
Tag data:
Total: 13,
Unique: 10,
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
Schema counts (B, I, E, S): (3, 0, 3, 7)

**Title**:
45_PMID30686098.txt_CC2.xml,
Words: 238,
Tokens: 534\
Tag data:
Total: 11,
Unique: 6,
Max tags: 1,
Tagged words: 11 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (63.64%), 7 (2.94%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 1, 4, 2)

**Title**:
301_PMID33116120.txt_CC2.xml,
Words: 282,
Tokens: 588\
Tag data:
Total: 16,
Unique: 10,
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
Schema counts (B, I, E, S): (4, 2, 4, 6)

**Title**:
552_PMID29058102.txt_CC2.xml,
Words: 201,
Tokens: 393\
Tag data:
Total: 7,
Unique: 3,
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
Schema counts (B, I, E, S): (3, 1, 3, 0)

**Title**:
300_PMID32912900.txt_CC2.xml,
Words: 155,
Tokens: 237\
Tag data:
Total: 21,
Unique: 7,
Max tags: 1,
Tagged words: 21 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 7, 7, 0)

**Title**:
35_PMID30894058.txt_CC2.xml,
Words: 253,
Tokens: 543\
Tag data:
Total: 37,
Unique: 17,
Max tags: 1,
Tagged words: 37 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (16.22%), 6 (2.37%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (9, 11, 9, 8)

**Title**:
199_PMID32265225.txt_CC2.xml,
Words: 290,
Tokens: 548\
Tag data:
Total: 28,
Unique: 11,
Max tags: 1,
Tagged words: 28 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 15,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (15 (53.57%), 15 (5.17%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (8, 9, 8, 3)

**Title**:
195_PMID32605998.txt_CC2.xml,
Words: 205,
Tokens: 345\
Tag data:
Total: 7,
Unique: 5,
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
Schema counts (B, I, E, S): (2, 0, 2, 3)

**Title**:
257_PMID28465358.txt_CC2.xml,
Words: 182,
Tokens: 332\
Tag data:
Total: 13,
Unique: 9,
Max tags: 1,
Tagged words: 13 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (38.46%), 5 (2.75%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 1, 3, 6)

**Title**:
261_PMID30692209.txt_CC2.xml,
Words: 166,
Tokens: 271\
Tag data:
Total: 22,
Unique: 11,
Max tags: 1,
Tagged words: 22 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 5, 6, 5)

**Title**:
96_PMID30669930.txt_CC2.xml,
Words: 183,
Tokens: 354\
Tag data:
Total: 12,
Unique: 6,
Max tags: 1,
Tagged words: 12 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (58.33%), 7 (3.83%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 2, 4, 2)

**Title**:
547_PMID31359205.txt_1_CC2.xml,
Words: 150,
Tokens: 279\
Tag data:
Total: 15,
Unique: 10,
Max tags: 1,
Tagged words: 15 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (1, 4, 1, 9)

**Title**:
258_PMID29773557.txt_CC2.xml,
Words: 107,
Tokens: 217\
Tag data:
Total: 14,
Unique: 2,
Max tags: 1,
Tagged words: 14 (13%),
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
579_PMID30788651.txt_CC2.xml,
Words: 255,
Tokens: 463\
Tag data:
Total: 19,
Unique: 12,
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
Schema counts (B, I, E, S): (5, 2, 5, 7)

**Title**:
350_PMID33257690.txt_CC2.xml,
Words: 310,
Tokens: 581\
Tag data:
Total: 33,
Unique: 12,
Max tags: 1,
Tagged words: 33 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 12, 9, 3)

**Title**:
448_PMID31024074.txt_CC2.xml,
Words: 208,
Tokens: 406\
Tag data:
Total: 54,
Unique: 31,
Max tags: 1,
Tagged words: 54 (26%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 27,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (24 (44.44%), 24 (11.54%))\
Avg links (tag, word): (1.12, 1.12),
Schema counts (B, I, E, S): (12, 11, 12, 19)

**Title**:
597_PMID30680481.txt_CC2.xml,
Words: 255,
Tokens: 524\
Tag data:
Total: 19,
Unique: 13,
Max tags: 1,
Tagged words: 19 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (36.84%), 7 (2.75%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 1, 5, 8)

**Title**:
505_PMID32737652.txt_CC2.xml,
Words: 156,
Tokens: 264\
Tag data:
Total: 8,
Unique: 7,
Max tags: 1,
Tagged words: 8 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (62.5%), 5 (3.21%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (1, 0, 1, 6)

**Title**:
733_PMID29731394.txt_CC2.xml,
Words: 126,
Tokens: 238\
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
163_PMID33115807.txt_CC2.xml,
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
734_PMID32860742.txt_CC2.xml,
Words: 150,
Tokens: 282\
Tag data:
Total: 19,
Unique: 9,
Max tags: 1,
Tagged words: 19 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 4,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (4 (21.05%), 4 (2.67%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 7, 3, 6)

**Title**:
588_PMID26801321.txt_CC2.xml,
Words: 224,
Tokens: 398\
Tag data:
Total: 10,
Unique: 9,
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
Schema counts (B, I, E, S): (1, 0, 1, 8)

**Title**:
693_PMID32991842.txt_CC2.xml,
Words: 161,
Tokens: 262\
Tag data:
Total: 26,
Unique: 4,
Max tags: 1,
Tagged words: 26 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 19, 3, 1)

**Title**:
19_PMID31177901.txt_CC2.xml,
Words: 232,
Tokens: 453\
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
Schema counts (B, I, E, S): (4, 0, 4, 6)

**Title**:
576_PMID30610505.txt_CC2.xml,
Words: 251,
Tokens: 478\
Tag data:
Total: 23,
Unique: 10,
Max tags: 1,
Tagged words: 23 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 5, 8, 2)

**Title**:
14_PMID30909789.txt_CC2.xml,
Words: 200,
Tokens: 497\
Tag data:
Total: 6,
Unique: 5,
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
Schema counts (B, I, E, S): (1, 0, 1, 4)

**Title**:
312_PMID33012781.txt_CC2.xml,
Words: 268,
Tokens: 504\
Tag data:
Total: 35,
Unique: 23,
Max tags: 1,
Tagged words: 35 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 64,
Unique: 10,
Max links (tag, word): (4, 4),
Linked (tags, words): (32 (91.43%), 32 (11.94%))\
Avg links (tag, word): (2.0, 2.0),
Schema counts (B, I, E, S): (10, 2, 10, 13)

**Title**:
75_PMID31241013.txt_CC2.xml,
Words: 131,
Tokens: 298\
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
424_PMID29786072.txt_CC2.xml,
Words: 245,
Tokens: 549\
Tag data:
Total: 30,
Unique: 10,
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
Schema counts (B, I, E, S): (8, 12, 8, 2)

**Title**:
337_PMID33154352.txt_CC2.xml,
Words: 173,
Tokens: 439\
Tag data:
Total: 47,
Unique: 30,
Max tags: 1,
Tagged words: 47 (27%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (14.89%), 7 (4.05%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (14, 3, 14, 16)

**Title**:
649_PMID32916131.txt_CC2.xml,
Words: 151,
Tokens: 266\
Tag data:
Total: 11,
Unique: 8,
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
Schema counts (B, I, E, S): (2, 1, 2, 6)

**Title**:
526_PMID30949883.txt_CC2.xml,
Words: 222,
Tokens: 366\
Tag data:
Total: 8,
Unique: 7,
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
586_PMID31342239.txt_CC2.xml,
Words: 209,
Tokens: 397\
Tag data:
Total: 33,
Unique: 18,
Max tags: 1,
Tagged words: 33 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (24.24%), 8 (3.83%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 8, 7, 11)

**Title**:
461_PMID31570856.txt_CC2.xml,
Words: 194,
Tokens: 447\
Tag data:
Total: 14,
Unique: 8,
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
Schema counts (B, I, E, S): (4, 2, 4, 4)

**Title**:
160_PMID32366480.txt_CC2.xml,
Words: 240,
Tokens: 424\
Tag data:
Total: 12,
Unique: 4,
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
Schema counts (B, I, E, S): (4, 4, 4, 0)

**Title**:
465_PMID31515511.txt_CC2.xml,
Words: 162,
Tokens: 358\
Tag data:
Total: 18,
Unique: 12,
Max tags: 1,
Tagged words: 18 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 3, 3, 9)

**Title**:
10_PMID30898012.txt_CC2.xml,
Words: 239,
Tokens: 436\
Tag data:
Total: 41,
Unique: 13,
Max tags: 1,
Tagged words: 41 (17%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 34,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (21 (51.22%), 21 (8.79%))\
Avg links (tag, word): (1.62, 1.62),
Schema counts (B, I, E, S): (6, 22, 6, 7)

**Title**:
175_PMID32350067.txt_CC2.xml,
Words: 213,
Tokens: 377\
Tag data:
Total: 23,
Unique: 10,
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
735_PMID30905761.txt_CC2.xml,
Words: 130,
Tokens: 255\
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
Schema counts (B, I, E, S): (3, 2, 3, 0)

**Title**:
520_PMID32338336.txt_CC2.xml,
Words: 246,
Tokens: 446\
Tag data:
Total: 11,
Unique: 7,
Max tags: 1,
Tagged words: 11 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 0, 4, 3)

**Title**:
155_PMID33372040.txt_CC2.xml,
Words: 222,
Tokens: 376\
Tag data:
Total: 41,
Unique: 18,
Max tags: 1,
Tagged words: 41 (18%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 19,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (11 (26.83%), 11 (4.95%))\
Avg links (tag, word): (1.73, 1.73),
Schema counts (B, I, E, S): (13, 10, 13, 5)

**Title**:
441_PMID31819147.txt_CC2.xml,
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
51_PMID31007149.txt_CC2.xml,
Words: 267,
Tokens: 568\
Tag data:
Total: 47,
Unique: 18,
Max tags: 1,
Tagged words: 47 (18%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 69,
Unique: 6,
Max links (tag, word): (4, 4),
Linked (tags, words): (24 (51.06%), 24 (8.99%))\
Avg links (tag, word): (2.88, 2.88),
Schema counts (B, I, E, S): (6, 23, 6, 12)

**Title**:
515_PMID32761307.txt_CC2.xml,
Words: 226,
Tokens: 370\
Tag data:
Total: 25,
Unique: 13,
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
Schema counts (B, I, E, S): (8, 4, 8, 5)

**Title**:
440_PMID31337872.txt_CC2.xml,
Words: 259,
Tokens: 534\
Tag data:
Total: 11,
Unique: 5,
Max tags: 1,
Tagged words: 11 (4%),
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
392_PMID33060569.txt_CC2.xml,
Words: 212,
Tokens: 420\
Tag data:
Total: 37,
Unique: 25,
Max tags: 1,
Tagged words: 37 (17%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 15,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (7 (18.92%), 7 (3.3%))\
Avg links (tag, word): (2.14, 2.14),
Schema counts (B, I, E, S): (9, 3, 9, 16)

**Title**:
88_PMID30957640.txt_CC2.xml,
Words: 245,
Tokens: 510\
Tag data:
Total: 8,
Unique: 8,
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
Schema counts (B, I, E, S): (0, 0, 0, 8)

**Title**:
226_PMID33303641.txt_CC2.xml,
Words: 152,
Tokens: 276\
Tag data:
Total: 40,
Unique: 22,
Max tags: 1,
Tagged words: 40 (26%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 39,
Unique: 6,
Max links (tag, word): (5, 5),
Linked (tags, words): (22 (55.0%), 22 (14.47%))\
Avg links (tag, word): (1.77, 1.77),
Schema counts (B, I, E, S): (7, 11, 7, 15)

**Title**:
119_PMID33023950.txt_CC2.xml,
Words: 231,
Tokens: 417\
Tag data:
Total: 28,
Unique: 14,
Max tags: 1,
Tagged words: 28 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 41,
Unique: 4,
Max links (tag, word): (4, 4),
Linked (tags, words): (17 (60.71%), 17 (7.36%))\
Avg links (tag, word): (2.41, 2.41),
Schema counts (B, I, E, S): (7, 7, 7, 7)

**Title**:
558_PMID31691131.txt_CC2.xml,
Words: 167,
Tokens: 294\
Tag data:
Total: 19,
Unique: 12,
Max tags: 1,
Tagged words: 19 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (31.58%), 6 (3.59%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 1, 6, 6)

**Title**:
22_PMID30909785.txt_CC2.xml,
Words: 250,
Tokens: 391\
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
Schema counts (B, I, E, S): (1, 0, 1, 2)

**Title**:
696_PMID32888430.txt_CC2.xml,
Words: 172,
Tokens: 337\
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
433_PMID31127201.txt_CC2.xml,
Words: 185,
Tokens: 374\
Tag data:
Total: 6,
Unique: 4,
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
Schema counts (B, I, E, S): (2, 0, 2, 2)

**Title**:
381_PMID33024087.txt_CC2.xml,
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
139_PMID32179514.txt_CC2.xml,
Words: 211,
Tokens: 354\
Tag data:
Total: 18,
Unique: 11,
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
Schema counts (B, I, E, S): (7, 0, 7, 4)

**Title**:
197_PMID32586982.txt_CC2.xml,
Words: 235,
Tokens: 423\
Tag data:
Total: 26,
Unique: 11,
Max tags: 1,
Tagged words: 26 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (10, 5, 10, 1)

**Title**:
475_PMID33139930.txt_CC2.xml,
Words: 218,
Tokens: 387\
Tag data:
Total: 13,
Unique: 7,
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
Schema counts (B, I, E, S): (6, 0, 6, 1)

**Title**:
311_PMID33268765.txt_CC2.xml,
Words: 223,
Tokens: 424\
Tag data:
Total: 22,
Unique: 13,
Max tags: 1,
Tagged words: 22 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (22.73%), 5 (2.24%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 2, 7, 6)

**Title**:
534_PMID30767087.txt_CC2.xml,
Words: 258,
Tokens: 451\
Tag data:
Total: 31,
Unique: 16,
Max tags: 1,
Tagged words: 31 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 7, 8, 8)

**Title**:
152_PMID33055221.txt_CC2.xml,
Words: 200,
Tokens: 373\
Tag data:
Total: 23,
Unique: 10,
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
Schema counts (B, I, E, S): (7, 6, 7, 3)

**Title**:
595_PMID30578463.txt_CC2.xml,
Words: 262,
Tokens: 543\
Tag data:
Total: 42,
Unique: 24,
Max tags: 1,
Tagged words: 42 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (11, 7, 11, 13)

**Title**:
522_PMID30680482.txt_CC2.xml,
Words: 193,
Tokens: 447\
Tag data:
Total: 31,
Unique: 16,
Max tags: 1,
Tagged words: 31 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (16.13%), 5 (2.59%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 10, 5, 11)

**Title**:
447_PMID31434979.txt_CC2.xml,
Words: 185,
Tokens: 390\
Tag data:
Total: 19,
Unique: 14,
Max tags: 1,
Tagged words: 19 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 3, 2, 12)

**Title**:
414_PMID31367011.txt_CC2.xml,
Words: 163,
Tokens: 343\
Tag data:
Total: 11,
Unique: 11,
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
Schema counts (B, I, E, S): (0, 0, 0, 11)

**Title**:
677_PMID33007268.txt_CC2.xml,
Words: 151,
Tokens: 233\
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
538_PMID32418059.txt_CC2.xml,
Words: 252,
Tokens: 551\
Tag data:
Total: 38,
Unique: 21,
Max tags: 1,
Tagged words: 38 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (10, 7, 10, 11)

**Title**:
514_PMID31993850.txt_CC2.xml,
Words: 254,
Tokens: 540\
Tag data:
Total: 22,
Unique: 19,
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
Schema counts (B, I, E, S): (3, 0, 3, 16)

**Title**:
570_PMID29858716.txt_CC2.xml,
Words: 266,
Tokens: 423\
Tag data:
Total: 26,
Unique: 15,
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
Schema counts (B, I, E, S): (8, 3, 8, 7)

**Title**:
408_PMID30787392.txt_CC2.xml,
Words: 191,
Tokens: 406\
Tag data:
Total: 7,
Unique: 6,
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
Schema counts (B, I, E, S): (1, 0, 1, 5)

**Title**:
228_PMID28698299.txt_CC2.xml,
Words: 229,
Tokens: 400\
Tag data:
Total: 21,
Unique: 16,
Max tags: 1,
Tagged words: 21 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (28.57%), 6 (2.62%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 1, 4, 12)

**Title**:
479_PMID31659279.txt_CC2.xml,
Words: 250,
Tokens: 471\
Tag data:
Total: 29,
Unique: 17,
Max tags: 1,
Tagged words: 29 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 38,
Unique: 4,
Max links (tag, word): (4, 4),
Linked (tags, words): (14 (48.28%), 14 (5.6%))\
Avg links (tag, word): (2.71, 2.71),
Schema counts (B, I, E, S): (5, 7, 5, 12)

**Title**:
327_PMID33203874.txt_CC2.xml,
Words: 235,
Tokens: 426\
Tag data:
Total: 10,
Unique: 7,
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
Schema counts (B, I, E, S): (2, 1, 2, 5)

**Title**:
429_PMID33037394.txt_CC2.xml,
Words: 212,
Tokens: 402\
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
607_PMID33248023.txt_CC2.xml,
Words: 157,
Tokens: 290\
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
Schema counts (B, I, E, S): (3, 1, 3, 3)

**Title**:
220_PMID31221665.txt_CC2.xml,
Words: 196,
Tokens: 368\
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
486_PMID31802036.txt_CC2.xml,
Words: 283,
Tokens: 489\
Tag data:
Total: 15,
Unique: 9,
Max tags: 1,
Tagged words: 15 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 13,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (8 (53.33%), 8 (2.83%))\
Avg links (tag, word): (1.62, 1.62),
Schema counts (B, I, E, S): (5, 1, 5, 4)

**Title**:
516_PMID32638182.txt_CC2.xml,
Words: 232,
Tokens: 492\
Tag data:
Total: 3,
Unique: 3,
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
Schema counts (B, I, E, S): (0, 0, 0, 3)

**Title**:
781_PMID30889383.txt_CC2.xml,
Words: 131,
Tokens: 241\
Tag data:
Total: 12,
Unique: 4,
Max tags: 1,
Tagged words: 12 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 4, 4, 0)

**Title**:
449_PMID30442948.txt_CC2.xml,
Words: 243,
Tokens: 427\
Tag data:
Total: 14,
Unique: 11,
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
Schema counts (B, I, E, S): (3, 0, 3, 8)

**Title**:
38_PMID31679456.txt_CC2.xml,
Words: 256,
Tokens: 486\
Tag data:
Total: 55,
Unique: 27,
Max tags: 2,
Tagged words: 53 (21%),
Avg tags: 1.04,
MC words: 0\
Link data:
Total: 33,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (21 (38.18%), 21 (8.2%))\
Avg links (tag, word): (1.57, 1.57),
Schema counts (B, I, E, S): (7, 21, 7, 20)

**Title**:
629_PMID33064988.txt_CC2.xml,
Words: 156,
Tokens: 272\
Tag data:
Total: 13,
Unique: 7,
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
Schema counts (B, I, E, S): (4, 2, 4, 3)

**Title**:
253_PMID31558567.txt_CC2.xml,
Words: 206,
Tokens: 378\
Tag data:
Total: 23,
Unique: 10,
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
Schema counts (B, I, E, S): (6, 7, 6, 4)

**Title**:
788_PMID32516591.txt_CC2.xml,
Words: 123,
Tokens: 219\
Tag data:
Total: 14,
Unique: 4,
Max tags: 1,
Tagged words: 14 (11%),
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
480_PMID31827236.txt_CC2.xml,
Words: 232,
Tokens: 494\
Tag data:
Total: 16,
Unique: 9,
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
Schema counts (B, I, E, S): (5, 2, 5, 4)

**Title**:
2_PMID30335591.txt_CC2.xml,
Words: 174,
Tokens: 421\
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
Schema counts (B, I, E, S): (1, 0, 1, 2)

**Title**:
795_PMID28810147.txt_CC2.xml,
Words: 132,
Tokens: 275\
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
Schema counts (B, I, E, S): (2, 1, 2, 2)

**Title**:
244_PMID31727771.txt_CC2.xml,
Words: 215,
Tokens: 433\
Tag data:
Total: 27,
Unique: 8,
Max tags: 1,
Tagged words: 27 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 17, 2, 6)

**Title**:
121_PMID32217695.txt_CC2.xml,
Words: 214,
Tokens: 445\
Tag data:
Total: 11,
Unique: 7,
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
Schema counts (B, I, E, S): (3, 1, 3, 4)

**Title**:
82_PMID30304977.txt_CC2.xml,
Words: 252,
Tokens: 440\
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
Schema counts (B, I, E, S): (3, 6, 3, 1)

**Title**:
335_PMID32980857.txt_CC2.xml,
Words: 305,
Tokens: 588\
Tag data:
Total: 25,
Unique: 15,
Max tags: 1,
Tagged words: 25 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 3, 7, 8)

**Title**:
364_PMID3320108.txt_CC2.xml,
Words: 214,
Tokens: 354\
Tag data:
Total: 6,
Unique: 4,
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
Schema counts (B, I, E, S): (2, 0, 2, 2)

**Title**:
619_PMID32937105.txt_CC2.xml,
Words: 156,
Tokens: 265\
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
Schema counts (B, I, E, S): (3, 4, 3, 3)

**Title**:
9_PMID31441382.txt_CC2.xml,
Words: 261,
Tokens: 607\
Tag data:
Total: 38,
Unique: 28,
Max tags: 1,
Tagged words: 38 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 24,
Unique: 4,
Max links (tag, word): (4, 4),
Linked (tags, words): (10 (26.32%), 10 (3.83%))\
Avg links (tag, word): (2.4, 2.4),
Schema counts (B, I, E, S): (7, 3, 7, 21)

**Title**:
495_PMID32814877.txt_CC2.xml,
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
792_PMID32220301.txt_CC2.xml,
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
366_PMID33127884.txt_CC2.xml,
Words: 230,
Tokens: 403\
Tag data:
Total: 14,
Unique: 8,
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
Schema counts (B, I, E, S): (3, 3, 3, 5)

**Title**:
328_PMID33097691.txt_CC2.xml,
Words: 301,
Tokens: 591\
Tag data:
Total: 13,
Unique: 8,
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
Schema counts (B, I, E, S): (4, 1, 4, 4)

**Title**:
113_PMID32029551.txt_CC2.xml,
Words: 223,
Tokens: 437\
Tag data:
Total: 13,
Unique: 7,
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
Schema counts (B, I, E, S): (3, 3, 3, 4)

**Title**:
500_PMID30442947.txt_CC2.xml,
Words: 167,
Tokens: 309\
Tag data:
Total: 10,
Unique: 7,
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
Schema counts (B, I, E, S): (2, 1, 2, 5)

**Title**:
456_PMID30683914.txt_CC2.xml,
Words: 173,
Tokens: 323\
Tag data:
Total: 40,
Unique: 19,
Max tags: 1,
Tagged words: 40 (23%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 38,
Unique: 4,
Max links (tag, word): (3, 3),
Linked (tags, words): (26 (65.0%), 26 (15.03%))\
Avg links (tag, word): (1.46, 1.46),
Schema counts (B, I, E, S): (10, 11, 10, 9)

**Title**:
287_PMID32381626.txt_CC2.xml,
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
624_PMID32778225.txt_CC2.xml,
Words: 135,
Tokens: 282\
Tag data:
Total: 11,
Unique: 8,
Max tags: 1,
Tagged words: 11 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 0, 4, 3)

**Title**:
468_PMID31844253.txt_CC2.xml,
Words: 282,
Tokens: 451\
Tag data:
Total: 23,
Unique: 12,
Max tags: 1,
Tagged words: 23 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 12,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (12 (52.17%), 12 (4.26%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 5, 6, 6)

**Title**:
18_PMID31931659.txt_CC2.xml,
Words: 247,
Tokens: 534\
Tag data:
Total: 40,
Unique: 24,
Max tags: 1,
Tagged words: 40 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 26,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (19 (47.5%), 19 (7.69%))\
Avg links (tag, word): (1.37, 1.37),
Schema counts (B, I, E, S): (6, 10, 6, 18)

**Title**:
599_PMID32036474.txt_CC2.xml,
Words: 266,
Tokens: 538\
Tag data:
Total: 36,
Unique: 18,
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
Schema counts (B, I, E, S): (10, 8, 10, 8)

**Title**:
772_PMID32049046.txt_CC2.xml,
Words: 131,
Tokens: 270\
Tag data:
Total: 7,
Unique: 4,
Max tags: 1,
Tagged words: 7 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (100.0%), 7 (5.34%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (2, 1, 2, 2)

**Title**:
799_PMID32589943.txt_CC2.xml,
Words: 130,
Tokens: 240\
Tag data:
Total: 13,
Unique: 7,
Max tags: 1,
Tagged words: 13 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (69.23%), 9 (6.92%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (2, 4, 2, 5)

**Title**:
421_PMID30341421.txt_CC2.xml,
Words: 211,
Tokens: 382\
Tag data:
Total: 21,
Unique: 10,
Max tags: 1,
Tagged words: 21 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 12,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (12 (57.14%), 12 (5.69%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 6, 5, 5)

**Title**:
550_PMID31654241.txt_CC2.xml,
Words: 293,
Tokens: 548\
Tag data:
Total: 47,
Unique: 19,
Max tags: 1,
Tagged words: 47 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 15,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (12 (25.53%), 12 (4.1%))\
Avg links (tag, word): (1.25, 1.25),
Schema counts (B, I, E, S): (9, 19, 9, 10)

**Title**:
420_PMID31748695.txt_CC2.xml,
Words: 199,
Tokens: 374\
Tag data:
Total: 16,
Unique: 8,
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
Schema counts (B, I, E, S): (4, 4, 4, 4)

**Title**:
296_PMID31171700.txt_CC2.xml,
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
738_PMID32619406.txt_CC2.xml,
Words: 123,
Tokens: 251\
Tag data:
Total: 17,
Unique: 7,
Max tags: 1,
Tagged words: 17 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (35.29%), 6 (4.88%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 6, 4, 3)

**Title**:
562_PMID31641960.txt_CC2.xml,
Words: 236,
Tokens: 456\
Tag data:
Total: 25,
Unique: 6,
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
Schema counts (B, I, E, S): (4, 15, 4, 2)

**Title**:
569_PMID28012059.txt_CC2.xml,
Words: 205,
Tokens: 402\
Tag data:
Total: 38,
Unique: 20,
Max tags: 1,
Tagged words: 38 (19%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 9, 9, 11)

**Title**:
590_PMID26386572.txt_CC2.xml,
Words: 220,
Tokens: 428\
Tag data:
Total: 13,
Unique: 11,
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
Schema counts (B, I, E, S): (2, 0, 2, 9)

**Title**:
16_PMID31232177.txt_CC2.xml,
Words: 210,
Tokens: 420\
Tag data:
Total: 32,
Unique: 16,
Max tags: 1,
Tagged words: 32 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 35,
Unique: 5,
Max links (tag, word): (4, 4),
Linked (tags, words): (21 (65.62%), 21 (10.0%))\
Avg links (tag, word): (1.67, 1.67),
Schema counts (B, I, E, S): (6, 10, 6, 10)

**Title**:
320_PMID33106477.txt_CC2.xml,
Words: 214,
Tokens: 409\
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
Schema counts (B, I, E, S): (1, 0, 1, 2)

**Title**:
506_PMID30710195.txt_CC2.xml,
Words: 255,
Tokens: 547\
Tag data:
Total: 21,
Unique: 15,
Max tags: 2,
Tagged words: 20 (8%),
Avg tags: 1.05,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 2, 4, 11)

**Title**:
431_PMID31591470.txt_CC2.xml,
Words: 195,
Tokens: 353\
Tag data:
Total: 24,
Unique: 8,
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
Schema counts (B, I, E, S): (6, 10, 6, 2)

**Title**:
295_PMID31221664.txt_CC2.xml,
Words: 220,
Tokens: 367\
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
419_PMID30850732.txt_CC2.xml,
Words: 226,
Tokens: 401\
Tag data:
Total: 22,
Unique: 9,
Max tags: 1,
Tagged words: 22 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 26,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (16 (72.73%), 16 (7.08%))\
Avg links (tag, word): (1.62, 1.62),
Schema counts (B, I, E, S): (7, 6, 7, 2)

**Title**:
507_PMID30877409.txt_CC2.xml,
Words: 196,
Tokens: 396\
Tag data:
Total: 18,
Unique: 17,
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
Schema counts (B, I, E, S): (1, 0, 1, 16)

**Title**:
605_PMID32795413.txt_CC2.xml,
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
450_PMID30042494.txt_CC2.xml,
Words: 152,
Tokens: 273\
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
267_PMID32675324.txt_CC2.xml,
Words: 203,
Tokens: 352\
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
Schema counts (B, I, E, S): (4, 0, 4, 1)

**Title**:
331_PMID33040078.txt_CC2.xml,
Words: 304,
Tokens: 546\
Tag data:
Total: 59,
Unique: 25,
Max tags: 1,
Tagged words: 59 (19%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 98,
Unique: 11,
Max links (tag, word): (6, 6),
Linked (tags, words): (39 (66.1%), 39 (12.83%))\
Avg links (tag, word): (2.51, 2.51),
Schema counts (B, I, E, S): (17, 17, 17, 8)

**Title**:
585_PMID30879165.txt_CC2.xml,
Words: 94,
Tokens: 149\
Tag data:
Total: 10,
Unique: 4,
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
427_PMID30349076.txt_CC2.xml,
Words: 207,
Tokens: 415\
Tag data:
Total: 15,
Unique: 12,
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
Schema counts (B, I, E, S): (3, 0, 3, 9)

**Title**:
326_PMID33293527.txt_CC2.xml,
Words: 221,
Tokens: 394\
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
Schema counts (B, I, E, S): (4, 1, 4, 1)

**Title**:
125_PMIDS32213542.txt_CC2.xml,
Words: 217,
Tokens: 397\
Tag data:
Total: 18,
Unique: 10,
Max tags: 1,
Tagged words: 18 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 21,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (16 (88.89%), 16 (7.37%))\
Avg links (tag, word): (1.31, 1.31),
Schema counts (B, I, E, S): (6, 2, 6, 4)

**Title**:
31_PMID31066324.txt_CC2.xml,
Words: 260,
Tokens: 487\
Tag data:
Total: 32,
Unique: 16,
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
Schema counts (B, I, E, S): (6, 10, 6, 10)

**Title**:
609_PMID32783918.txt_CC2.xml,
Words: 157,
Tokens: 324\
Tag data:
Total: 15,
Unique: 9,
Max tags: 1,
Tagged words: 15 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 2, 4, 5)

**Title**:
111_PMID32816857.txt_CC2.xml,
Words: 224,
Tokens: 407\
Tag data:
Total: 6,
Unique: 1,
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
Schema counts (B, I, E, S): (1, 4, 1, 0)

**Title**:
91_PMID31538542.txt_CC2.xml,
Words: 232,
Tokens: 422\
Tag data:
Total: 17,
Unique: 10,
Max tags: 1,
Tagged words: 17 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 2, 5, 5)

**Title**:
487_PMID32661288.txt_CC2.xml,
Words: 305,
Tokens: 531\
Tag data:
Total: 10,
Unique: 5,
Max tags: 1,
Tagged words: 10 (3%),
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
179_PMID32732220.txt_CC2.xml,
Words: 259,
Tokens: 541\
Tag data:
Total: 5,
Unique: 4,
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
217_PMID31857346.txt_CC2.xml,
Words: 166,
Tokens: 316\
Tag data:
Total: 9,
Unique: 4,
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
Schema counts (B, I, E, S): (3, 2, 3, 1)

**Title**:
83_PMID30741592.txt_CC2.xml,
Words: 263,
Tokens: 436\
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
347_PMID33414384.txt_CC2.xml,
Words: 260,
Tokens: 481\
Tag data:
Total: 15,
Unique: 5,
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
Schema counts (B, I, E, S): (4, 6, 4, 1)

**Title**:
196_PMID32213544.txt_CC2.xml,
Words: 196,
Tokens: 392\
Tag data:
Total: 15,
Unique: 8,
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
Schema counts (B, I, E, S): (4, 3, 4, 4)

**Title**:
101_PMID32788173.txt_CC2.xml,
Words: 177,
Tokens: 346\
Tag data:
Total: 17,
Unique: 11,
Max tags: 1,
Tagged words: 17 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 47,
Unique: 7,
Max links (tag, word): (6, 6),
Linked (tags, words): (17 (100.0%), 17 (9.6%))\
Avg links (tag, word): (2.76, 2.76),
Schema counts (B, I, E, S): (5, 1, 5, 6)

**Title**:
498_PMID31819159.txt_CC2.xml,
Words: 245,
Tokens: 485\
Tag data:
Total: 7,
Unique: 3,
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
Schema counts (B, I, E, S): (2, 2, 2, 1)

**Title**:
180_PMID32816912.txt_CC2.xml,
Words: 256,
Tokens: 454\
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
Schema counts (B, I, E, S): (2, 4, 2, 2)

**Title**:
181_PMID32179512.txt_CC2.xml,
Words: 227,
Tokens: 393\
Tag data:
Total: 17,
Unique: 7,
Max tags: 1,
Tagged words: 17 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 6, 4, 3)

**Title**:
104_PMID32605995.txt_CC2.xml,
Words: 204,
Tokens: 355\
Tag data:
Total: 20,
Unique: 7,
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
Schema counts (B, I, E, S): (7, 6, 7, 0)

**Title**:
211_PMID31416966.txt_CC2.xml,
Words: 243,
Tokens: 424\
Tag data:
Total: 19,
Unique: 8,
Max tags: 1,
Tagged words: 19 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 6, 5, 3)

**Title**:
476_PMID29459771.txt_CC2.xml,
Words: 256,
Tokens: 455\
Tag data:
Total: 24,
Unique: 15,
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
Schema counts (B, I, E, S): (7, 2, 7, 8)

**Title**:
785_PMID33357452.txt_CC2.xml,
Words: 171,
Tokens: 348\
Tag data:
Total: 12,
Unique: 7,
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
451_PMID31296961.txt_CC2.xml,
Words: 175,
Tokens: 343\
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
Schema counts (B, I, E, S): (2, 0, 2, 1)

**Title**:
711_PMID32888432.txt_CC2.xml,
Words: 141,
Tokens: 235\
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
Schema counts (B, I, E, S): (1, 2, 1, 2)

**Title**:
288_PMID30366907.txt_CC2.xml,
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
72_PMID31238788.txt_CC2.xml,
Words: 178,
Tokens: 368\
Tag data:
Total: 28,
Unique: 17,
Max tags: 1,
Tagged words: 28 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 15,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (14 (50.0%), 14 (7.87%))\
Avg links (tag, word): (1.07, 1.07),
Schema counts (B, I, E, S): (8, 3, 8, 9)

**Title**:
540_PMID31243498.txt_CC2.xml,
Words: 211,
Tokens: 401\
Tag data:
Total: 39,
Unique: 29,
Max tags: 1,
Tagged words: 39 (18%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 4, 6, 23)

**Title**:
721_PMID31588020.txt_CC2.xml,
Words: 139,
Tokens: 247\
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
Schema counts (B, I, E, S): (1, 2, 1, 1)

**Title**:
146_PMID32193285.txt_CC2.xml,
Words: 215,
Tokens: 422\
Tag data:
Total: 42,
Unique: 14,
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
Schema counts (B, I, E, S): (9, 19, 9, 5)

**Title**:
780_PMID32559497.txt_CC2.xml,
Words: 132,
Tokens: 245\
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
329_PMID32895268.txt_CC2.xml,
Words: 229,
Tokens: 496\
Tag data:
Total: 9,
Unique: 6,
Max tags: 1,
Tagged words: 9 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 24,
Unique: 4,
Max links (tag, word): (4, 4),
Linked (tags, words): (9 (100.0%), 9 (3.93%))\
Avg links (tag, word): (2.67, 2.67),
Schema counts (B, I, E, S): (3, 0, 3, 3)

**Title**:
242_PMID29563184.txt_CC2.xml,
Words: 231,
Tokens: 432\
Tag data:
Total: 21,
Unique: 10,
Max tags: 1,
Tagged words: 21 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 4, 7, 3)

**Title**:
564_PMID30879166.txt_CC2.xml,
Words: 235,
Tokens: 450\
Tag data:
Total: 32,
Unique: 11,
Max tags: 1,
Tagged words: 32 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (21.88%), 7 (2.98%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 16, 5, 6)

**Title**:
330_PMID33203867.txt_CC2.xml,
Words: 225,
Tokens: 383\
Tag data:
Total: 24,
Unique: 14,
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
Schema counts (B, I, E, S): (5, 5, 5, 9)

**Title**:
519_PMID31485878.txt_CC2.xml,
Words: 187,
Tokens: 333\
Tag data:
Total: 20,
Unique: 11,
Max tags: 1,
Tagged words: 20 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 6, 3, 8)

**Title**:
754_PMID31185211.txt_CC2.xml,
Words: 129,
Tokens: 273\
Tag data:
Total: 21,
Unique: 12,
Max tags: 1,
Tagged words: 21 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (33.33%), 7 (5.43%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 2, 7, 5)

**Title**:
455_PMID31114027.txt_CC2.xml,
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
205_PMID32079653.txt_CC2.xml,
Words: 197,
Tokens: 321\
Tag data:
Total: 17,
Unique: 4,
Max tags: 1,
Tagged words: 17 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 9, 4, 0)

**Title**:
272_PMID30842217.txt_CC2.xml,
Words: 151,
Tokens: 257\
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
Schema counts (B, I, E, S): (1, 2, 1, 2)

**Title**:
517_PMID33068199.txt_CC2.xml,
Words: 166,
Tokens: 351\
Tag data:
Total: 9,
Unique: 9,
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
Schema counts (B, I, E, S): (0, 0, 0, 9)

**Title**:
358_PMID33257655.txt_CC2.xml,
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
266_PMID32912902.txt_CC2.xml,
Words: 214,
Tokens: 348\
Tag data:
Total: 21,
Unique: 6,
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
Schema counts (B, I, E, S): (6, 9, 6, 0)

**Title**:
354_PMID33159047.txt_CC2.xml,
Words: 296,
Tokens: 539\
Tag data:
Total: 46,
Unique: 15,
Max tags: 1,
Tagged words: 46 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 29,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (17 (36.96%), 17 (5.74%))\
Avg links (tag, word): (1.71, 1.71),
Schema counts (B, I, E, S): (11, 20, 11, 4)

**Title**:
192_PMID32107211.txt_CC2.xml,
Words: 231,
Tokens: 432\
Tag data:
Total: 7,
Unique: 3,
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
Schema counts (B, I, E, S): (2, 2, 2, 1)

**Title**:
319_PMID33268783.txt_CC2.xml,
Words: 207,
Tokens: 433\
Tag data:
Total: 21,
Unique: 8,
Max tags: 1,
Tagged words: 21 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 21,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (11 (52.38%), 11 (5.31%))\
Avg links (tag, word): (1.91, 1.91),
Schema counts (B, I, E, S): (5, 8, 5, 3)

**Title**:
187_PMID32393661.txt_CC2.xml,
Words: 211,
Tokens: 384\
Tag data:
Total: 9,
Unique: 6,
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
313_PMID33099572.txt_CC2.xml,
Words: 140,
Tokens: 284\
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
527_PMID31321634.txt_CC2.xml,
Words: 211,
Tokens: 440\
Tag data:
Total: 56,
Unique: 25,
Max tags: 1,
Tagged words: 56 (27%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 51,
Unique: 5,
Max links (tag, word): (2, 2),
Linked (tags, words): (40 (71.43%), 40 (18.96%))\
Avg links (tag, word): (1.27, 1.27),
Schema counts (B, I, E, S): (13, 18, 13, 12)

**Title**:
496_PMID32737443.txt_CC2.xml,
Words: 186,
Tokens: 355\
Tag data:
Total: 14,
Unique: 10,
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
Schema counts (B, I, E, S): (4, 0, 4, 6)

**Title**:
52_PMID31920157.txt_CC2.xml,
Words: 220,
Tokens: 347\
Tag data:
Total: 6,
Unique: 6,
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
Schema counts (B, I, E, S): (0, 0, 0, 6)

**Title**:
565_PMID31768842.txt_CC2.xml,
Words: 225,
Tokens: 424\
Tag data:
Total: 16,
Unique: 11,
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
Schema counts (B, I, E, S): (1, 4, 1, 10)

**Title**:
739_PMID31056398.txt_CC2.xml,
Words: 114,
Tokens: 194\
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
Schema counts (B, I, E, S): (2, 0, 2, 0)

**Title**:
766_PMID31031016.txt_CC2.xml,
Words: 142,
Tokens: 295\
Tag data:
Total: 8,
Unique: 5,
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
Schema counts (B, I, E, S): (3, 0, 3, 2)

**Title**:
483_PMID31831874.txt_CC2.xml,
Words: 222,
Tokens: 397\
Tag data:
Total: 20,
Unique: 12,
Max tags: 1,
Tagged words: 20 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (40.0%), 8 (3.6%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 2, 6, 6)

**Title**:
736_PMID30799057.txt_CC2.xml,
Words: 129,
Tokens: 230\
Tag data:
Total: 14,
Unique: 3,
Max tags: 1,
Tagged words: 14 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 8, 3, 0)

**Title**:
148_PMID32690724.txt_CC2.xml,
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
206_PMID32883681.txt_CC2.xml,
Words: 151,
Tokens: 319\
Tag data:
Total: 4,
Unique: 4,
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
Schema counts (B, I, E, S): (0, 0, 0, 4)

**Title**:
305_PMID32951003.txt_CC2.xml,
Words: 230,
Tokens: 453\
Tag data:
Total: 18,
Unique: 12,
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
Schema counts (B, I, E, S): (5, 1, 5, 7)

**Title**:
444_PMID32231246.txt_CC2.xml,
Words: 237,
Tokens: 447\
Tag data:
Total: 25,
Unique: 14,
Max tags: 1,
Tagged words: 25 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (20.0%), 5 (2.11%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 7, 4, 10)

**Title**:
323_PMID32913185.txt_CC2.xml,
Words: 186,
Tokens: 323\
Tag data:
Total: 20,
Unique: 10,
Max tags: 1,
Tagged words: 20 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 15,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (15 (75.0%), 15 (8.06%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 3, 7, 3)

**Title**:
375_PMID33462182.txt_CC2.xml,
Words: 309,
Tokens: 592\
Tag data:
Total: 28,
Unique: 24,
Max tags: 2,
Tagged words: 27 (9%),
Avg tags: 1.04,
MC words: 1\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 1, 3, 21)

**Title**:
490_PMID31740790.txt_CC2.xml,
Words: 177,
Tokens: 343\
Tag data:
Total: 26,
Unique: 17,
Max tags: 1,
Tagged words: 26 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 0, 9, 8)

**Title**:
36_PMID30653446.txt_CC2.xml,
Words: 260,
Tokens: 548\
Tag data:
Total: 34,
Unique: 15,
Max tags: 2,
Tagged words: 33 (13%),
Avg tags: 1.03,
MC words: 1\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (12, 7, 12, 3)

**Title**:
27_PMID31208283.txt_CC2.xml,
Words: 262,
Tokens: 476\
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
Schema counts (B, I, E, S): (2, 4, 2, 1)

**Title**:
439_PMID31065106.txt_CC2.xml,
Words: 177,
Tokens: 298\
Tag data:
Total: 24,
Unique: 6,
Max tags: 1,
Tagged words: 24 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 13, 5, 1)

**Title**:
123_PMID32606006.txt_CC2.xml,
Words: 171,
Tokens: 329\
Tag data:
Total: 11,
Unique: 7,
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
Schema counts (B, I, E, S): (3, 1, 3, 4)

**Title**:
573_PMID30515612.txt_CC2.xml,
Words: 225,
Tokens: 381\
Tag data:
Total: 36,
Unique: 21,
Max tags: 1,
Tagged words: 36 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 39,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (17 (47.22%), 17 (7.56%))\
Avg links (tag, word): (2.29, 2.29),
Schema counts (B, I, E, S): (6, 9, 6, 15)

**Title**:
127_PMID32651256.txt_CC2.xml,
Words: 220,
Tokens: 365\
Tag data:
Total: 17,
Unique: 10,
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
Schema counts (B, I, E, S): (5, 2, 5, 5)

**Title**:
208_PMID32001512.txt_CC2.xml,
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
286_PMID30842215.txt_CC2.xml,
Words: 218,
Tokens: 351\
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
Schema counts (B, I, E, S): (3, 0, 3, 2)

**Title**:
54_PMID31373534.txt_CC2.xml,
Words: 233,
Tokens: 448\
Tag data:
Total: 29,
Unique: 18,
Max tags: 1,
Tagged words: 29 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 24,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (21 (72.41%), 21 (9.01%))\
Avg links (tag, word): (1.14, 1.14),
Schema counts (B, I, E, S): (5, 6, 5, 13)

**Title**:
684_PMID32730808.txt_CC2.xml,
Words: 163,
Tokens: 312\
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
497_PMID33398092.txt_CC2.xml,
Words: 211,
Tokens: 402\
Tag data:
Total: 23,
Unique: 11,
Max tags: 1,
Tagged words: 23 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (21.74%), 5 (2.37%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 7, 5, 6)

**Title**:
184_PMID32928921.txt_CC2.xml,
Words: 242,
Tokens: 463\
Tag data:
Total: 23,
Unique: 11,
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
Schema counts (B, I, E, S): (5, 7, 5, 6)

**Title**:
633_PMID33125892.txt_CC2.xml,
Words: 154,
Tokens: 283\
Tag data:
Total: 10,
Unique: 7,
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
Schema counts (B, I, E, S): (3, 0, 3, 4)

**Title**:
289_PMID30692206.txt_CC2.xml,
Words: 174,
Tokens: 353\
Tag data:
Total: 21,
Unique: 9,
Max tags: 1,
Tagged words: 21 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 11,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (11 (52.38%), 11 (6.32%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 8, 4, 5)

**Title**:
474_PMID29666477.txt_CC2.xml,
Words: 209,
Tokens: 383\
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
Schema counts (B, I, E, S): (1, 0, 1, 2)

**Title**:
703_PMID31883968.txt_CC2.xml,
Words: 126,
Tokens: 223\
Tag data:
Total: 16,
Unique: 5,
Max tags: 1,
Tagged words: 16 (13%),
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
172_PMID33239425.txt_CC2.xml,
Words: 220,
Tokens: 317\
Tag data:
Total: 8,
Unique: 6,
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
292_PMID28546513.txt_CC2.xml,
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
136_PMID32156776.txt_CC2.xml,
Words: 225,
Tokens: 336\
Tag data:
Total: 11,
Unique: 8,
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
Schema counts (B, I, E, S): (3, 0, 3, 5)

**Title**:
389_PMID33239613.txt_CC2.xml,
Words: 241,
Tokens: 428\
Tag data:
Total: 11,
Unique: 8,
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
Schema counts (B, I, E, S): (3, 0, 3, 5)

**Title**:
405_PMID31804607.txt_CC2.xml,
Words: 198,
Tokens: 422\
Tag data:
Total: 25,
Unique: 12,
Max tags: 1,
Tagged words: 25 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 22,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (18 (72.0%), 18 (9.09%))\
Avg links (tag, word): (1.22, 1.22),
Schema counts (B, I, E, S): (7, 6, 7, 5)

**Title**:
28_PMID30786811.txt_CC2.xml,
Words: 261,
Tokens: 473\
Tag data:
Total: 14,
Unique: 8,
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
Schema counts (B, I, E, S): (4, 2, 4, 4)

**Title**:
758_PMID30423296.txt_CC2.xml,
Words: 132,
Tokens: 271\
Tag data:
Total: 16,
Unique: 8,
Max tags: 1,
Tagged words: 16 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (50.0%), 8 (6.06%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 3, 5, 3)

**Title**:
731_PMID29622463.txt_CC2.xml,
Words: 117,
Tokens: 202\
Tag data:
Total: 5,
Unique: 4,
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
246_PMID32139423.txt_CC2.xml,
Words: 151,
Tokens: 276\
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
349_PMID33093455.txt_CC2.xml,
Words: 243,
Tokens: 573\
Tag data:
Total: 17,
Unique: 10,
Max tags: 1,
Tagged words: 17 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 3, 4, 6)

**Title**:
761_PMID31543463.txt_CC2.xml,
Words: 129,
Tokens: 229\
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
473_PMID33082514.txt_CC2.xml,
Words: 169,
Tokens: 283\
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
134_PMID32641409.txt_CC2.xml,
Words: 223,
Tokens: 448\
Tag data:
Total: 22,
Unique: 15,
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
Schema counts (B, I, E, S): (5, 2, 5, 10)

**Title**:
643_PMID33099771.txt_CC2.xml,
Words: 155,
Tokens: 261\
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
209_PMID30692202.txt_CC2.xml,
Words: 173,
Tokens: 308\
Tag data:
Total: 5,
Unique: 1,
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
Schema counts (B, I, E, S): (1, 3, 1, 0)

**Title**:
361_PMID32943619.txt_CC2.xml,
Words: 233,
Tokens: 397\
Tag data:
Total: 15,
Unique: 10,
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
Schema counts (B, I, E, S): (4, 1, 4, 6)

**Title**:
661_PMID33157039.txt_CC2.xml,
Words: 156,
Tokens: 249\
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
728_PMID32183950.txt_CC2.xml,
Words: 126,
Tokens: 274\
Tag data:
Total: 39,
Unique: 20,
Max tags: 1,
Tagged words: 39 (31%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 32,
Unique: 4,
Max links (tag, word): (4, 4),
Linked (tags, words): (16 (41.03%), 16 (12.7%))\
Avg links (tag, word): (2.0, 2.0),
Schema counts (B, I, E, S): (11, 8, 11, 9)

**Title**:
499_PMID30478383.txt_CC2.xml,
Words: 270,
Tokens: 536\
Tag data:
Total: 38,
Unique: 22,
Max tags: 1,
Tagged words: 38 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 12,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (12 (31.58%), 12 (4.44%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (10, 6, 10, 12)

**Title**:
43_PMID31204559.txt_CC2.xml,
Words: 186,
Tokens: 320\
Tag data:
Total: 29,
Unique: 19,
Max tags: 1,
Tagged words: 29 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 14,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (14 (48.28%), 14 (7.53%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 3, 7, 12)

**Title**:
368_PMID33093476.txt_CC2.xml,
Words: 190,
Tokens: 317\
Tag data:
Total: 22,
Unique: 13,
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
Schema counts (B, I, E, S): (6, 3, 6, 7)

**Title**:
746_PMID33385331.txt_CC2.xml,
Words: 154,
Tokens: 301\
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
Schema counts (B, I, E, S): (4, 2, 4, 0)

**Title**:
33_PMID31223056.txt_CC2.xml,
Words: 250,
Tokens: 515\
Tag data:
Total: 24,
Unique: 15,
Max tags: 1,
Tagged words: 24 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (20.83%), 5 (2.0%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 5, 4, 11)

**Title**:
744_PMID31474569.txt_CC2.xml,
Words: 136,
Tokens: 319\
Tag data:
Total: 8,
Unique: 5,
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
Schema counts (B, I, E, S): (3, 0, 3, 2)

**Title**:
697_PMID33125897.txt_CC2.xml,
Words: 153,
Tokens: 205\
Tag data:
Total: 15,
Unique: 5,
Max tags: 1,
Tagged words: 15 (10%),
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
128_PMID32193288.txt_CC2.xml,
Words: 199,
Tokens: 391\
Tag data:
Total: 10,
Unique: 5,
Max tags: 1,
Tagged words: 10 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 14,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (10 (100.0%), 10 (5.03%))\
Avg links (tag, word): (1.4, 1.4),
Schema counts (B, I, E, S): (3, 2, 3, 2)

**Title**:
30_PMID30681394.txt_CC2.xml,
Words: 163,
Tokens: 352\
Tag data:
Total: 5,
Unique: 4,
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
202_PMID32001510.txt_CC2.xml,
Words: 216,
Tokens: 409\
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
678_PMID32931734.txt_CC2.xml,
Words: 162,
Tokens: 325\
Tag data:
Total: 15,
Unique: 5,
Max tags: 1,
Tagged words: 15 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 8, 2, 3)

**Title**:
370_PMID33277461.txt_CC2.xml,
Words: 264,
Tokens: 589\
Tag data:
Total: 51,
Unique: 25,
Max tags: 2,
Tagged words: 50 (19%),
Avg tags: 1.02,
MC words: 1\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (17.65%), 9 (3.41%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (12, 14, 12, 13)

**Title**:
409_PMID31209362.txt_CC2.xml,
Words: 155,
Tokens: 274\
Tag data:
Total: 16,
Unique: 8,
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
Schema counts (B, I, E, S): (5, 3, 5, 3)

**Title**:
278_PMID32763910.txt_CC2.xml,
Words: 210,
Tokens: 358\
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
Schema counts (B, I, E, S): (3, 4, 3, 1)

**Title**:
393_PMID33067426.txt_CC2.xml,
Words: 232,
Tokens: 386\
Tag data:
Total: 26,
Unique: 13,
Max tags: 1,
Tagged words: 26 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 7, 6, 7)

**Title**:
749_PMID31935372.txt_CC2.xml,
Words: 126,
Tokens: 262\
Tag data:
Total: 5,
Unique: 5,
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
Schema counts (B, I, E, S): (0, 0, 0, 5)

**Title**:
377_PMID32929059.txt_CC2.xml,
Words: 270,
Tokens: 533\
Tag data:
Total: 18,
Unique: 9,
Max tags: 1,
Tagged words: 18 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 18,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (10 (55.56%), 10 (3.7%))\
Avg links (tag, word): (1.8, 1.8),
Schema counts (B, I, E, S): (6, 3, 6, 3)

**Title**:
112_PMID33051252.txt_CC2.xml,
Words: 238,
Tokens: 414\
Tag data:
Total: 25,
Unique: 15,
Max tags: 1,
Tagged words: 25 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 70,
Unique: 9,
Max links (tag, word): (6, 6),
Linked (tags, words): (25 (100.0%), 25 (10.5%))\
Avg links (tag, word): (2.8, 2.8),
Schema counts (B, I, E, S): (6, 4, 6, 9)

**Title**:
494_PMID30659235.txt_CC2.xml,
Words: 222,
Tokens: 414\
Tag data:
Total: 46,
Unique: 18,
Max tags: 1,
Tagged words: 46 (21%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 20,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (20 (43.48%), 20 (9.01%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (13, 15, 13, 5)

**Title**:
794_PMID30753824.txt_CC2.xml,
Words: 137,
Tokens: 285\
Tag data:
Total: 23,
Unique: 10,
Max tags: 1,
Tagged words: 23 (17%),
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
344_PMID33060560.txt_CC2.xml,
Words: 229,
Tokens: 466\
Tag data:
Total: 29,
Unique: 14,
Max tags: 1,
Tagged words: 29 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 10,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (10 (34.48%), 10 (4.37%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (10, 5, 10, 4)

**Title**:
178_PMID32999000.txt_CC2.xml,
Words: 228,
Tokens: 404\
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
Schema counts (B, I, E, S): (5, 3, 5, 1)

**Title**:
42_PMID31276435.txt_CC2.xml,
Words: 184,
Tokens: 368\
Tag data:
Total: 12,
Unique: 7,
Max tags: 1,
Tagged words: 12 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (41.67%), 5 (2.72%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 1, 4, 3)

**Title**:
553_PMID29236198.txt_CC2.xml,
Words: 263,
Tokens: 444\
Tag data:
Total: 18,
Unique: 12,
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
Schema counts (B, I, E, S): (2, 4, 2, 10)

**Title**:
65_PMID30898011.txt_CC2.xml,
Words: 206,
Tokens: 412\
Tag data:
Total: 13,
Unique: 10,
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
Schema counts (B, I, E, S): (2, 1, 2, 8)

**Title**:
98_PMID31432739.txt_CC2.xml,
Words: 229,
Tokens: 481\
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
62_PMID31234698.txt_CC2.xml,
Words: 147,
Tokens: 256\
Tag data:
Total: 13,
Unique: 5,
Max tags: 1,
Tagged words: 13 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 5, 3, 2)

**Title**:
71_PMID32521192.txt_CC2.xml,
Words: 197,
Tokens: 372\
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
Schema counts (B, I, E, S): (2, 1, 2, 1)

**Title**:
387_PMID33056980.txt_CC2.xml,
Words: 209,
Tokens: 373\
Tag data:
Total: 19,
Unique: 11,
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
Schema counts (B, I, E, S): (4, 4, 4, 7)

**Title**:
411_PMID30692641.txt_CC2.xml,
Words: 228,
Tokens: 414\
Tag data:
Total: 23,
Unique: 11,
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
Schema counts (B, I, E, S): (7, 5, 7, 4)

**Title**:
277_PMID31296559.txt_CC2.xml,
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
47_PMID32003282.txt_CC2.xml,
Words: 207,
Tokens: 414\
Tag data:
Total: 19,
Unique: 5,
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
Schema counts (B, I, E, S): (3, 11, 3, 2)

**Title**:
471_PMID31160717.txt_CC2.xml,
Words: 219,
Tokens: 473\
Tag data:
Total: 15,
Unique: 8,
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
Schema counts (B, I, E, S): (5, 2, 5, 3)

**Title**:
4_PMID32186434.txt_CC2.xml,
Words: 155,
Tokens: 271\
Tag data:
Total: 20,
Unique: 9,
Max tags: 1,
Tagged words: 20 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 6, 5, 4)

**Title**:
568_PMID32405891.txt_CC2.xml,
Words: 262,
Tokens: 469\
Tag data:
Total: 35,
Unique: 15,
Max tags: 1,
Tagged words: 35 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (20.0%), 7 (2.67%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (8, 12, 8, 7)

**Title**:
763_PMID33157048.txt_CC2.xml,
Words: 159,
Tokens: 311\
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
442_PMID31209361.txt_CC2.xml,
Words: 274,
Tokens: 594\
Tag data:
Total: 24,
Unique: 15,
Max tags: 1,
Tagged words: 24 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 23,
Unique: 4,
Max links (tag, word): (4, 4),
Linked (tags, words): (14 (58.33%), 14 (5.11%))\
Avg links (tag, word): (1.64, 1.64),
Schema counts (B, I, E, S): (8, 1, 8, 7)

**Title**:
233_PMID31395741.txt_CC2.xml,
Words: 260,
Tokens: 534\
Tag data:
Total: 28,
Unique: 8,
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
Schema counts (B, I, E, S): (7, 13, 7, 1)

**Title**:
23_PMID30208757.txt_CC2.xml,
Words: 170,
Tokens: 320\
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
722_PMID30645973.txt_CC2.xml,
Words: 122,
Tokens: 203\
Tag data:
Total: 17,
Unique: 7,
Max tags: 1,
Tagged words: 17 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 6, 4, 3)

**Title**:
81_PMID30654731.txt_CC2.xml,
Words: 208,
Tokens: 355\
Tag data:
Total: 19,
Unique: 8,
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
Schema counts (B, I, E, S): (5, 6, 5, 3)

**Title**:
615_PMID33278357.txt_CC2.xml,
Words: 168,
Tokens: 333\
Tag data:
Total: 8,
Unique: 6,
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
Schema counts (B, I, E, S): (2, 0, 2, 4)

**Title**:
768_PMID32619407.txt_CC2.xml,
Words: 122,
Tokens: 247\
Tag data:
Total: 18,
Unique: 6,
Max tags: 1,
Tagged words: 18 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 7, 5, 1)

**Title**:
779_PMID32109375.txt_CC2.xml,
Words: 134,
Tokens: 271\
Tag data:
Total: 19,
Unique: 10,
Max tags: 1,
Tagged words: 19 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 20,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (12 (63.16%), 12 (8.96%))\
Avg links (tag, word): (1.67, 1.67),
Schema counts (B, I, E, S): (6, 3, 6, 4)

**Title**:
443_PMID30042493.txt_CC2.xml,
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
676_PMID32795415.txt_CC2.xml,
Words: 148,
Tokens: 314\
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
Schema counts (B, I, E, S): (4, 6, 4, 3)

**Title**:
68_PMID32186433.txt_CC2.xml,
Words: 259,
Tokens: 536\
Tag data:
Total: 14,
Unique: 11,
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
Schema counts (B, I, E, S): (1, 2, 1, 10)

**Title**:
26_PMID31362587.txt_CC2.xml,
Words: 225,
Tokens: 507\
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
Schema counts (B, I, E, S): (4, 7, 4, 5)

**Title**:
416_PMID31097789.txt_CC2.xml,
Words: 251,
Tokens: 498\
Tag data:
Total: 8,
Unique: 5,
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
Schema counts (B, I, E, S): (2, 1, 2, 3)

**Title**:
215_PMID31048544.txt_CC2.xml,
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
348_PMID33024074.txt_CC2.xml,
Words: 283,
Tokens: 519\
Tag data:
Total: 18,
Unique: 8,
Max tags: 1,
Tagged words: 18 (6%),
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
279_PMID32217664.txt_CC2.xml,
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
69_PMID30773986.txt_CC2.xml,
Words: 174,
Tokens: 326\
Tag data:
Total: 5,
Unique: 4,
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
446_PMID32152555.txt_CC2.xml,
Words: 257,
Tokens: 505\
Tag data:
Total: 21,
Unique: 8,
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
Schema counts (B, I, E, S): (4, 10, 4, 3)

**Title**:
281_PMID31371435.txt_CC2.xml,
Words: 168,
Tokens: 329\
Tag data:
Total: 13,
Unique: 2,
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
Schema counts (B, I, E, S): (2, 9, 2, 0)

**Title**:
352_PMID33122623.txt_CC2.xml,
Words: 262,
Tokens: 472\
Tag data:
Total: 38,
Unique: 22,
Max tags: 2,
Tagged words: 36 (14%),
Avg tags: 1.06,
MC words: 2\
Link data:
Total: 30,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (21 (55.26%), 21 (8.02%))\
Avg links (tag, word): (1.43, 1.43),
Schema counts (B, I, E, S): (11, 5, 11, 11)

**Title**:
504_PMID31175486.txt_CC2.xml,
Words: 260,
Tokens: 568\
Tag data:
Total: 37,
Unique: 19,
Max tags: 1,
Tagged words: 37 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 12,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (12 (32.43%), 12 (4.62%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (10, 8, 10, 9)

**Title**:
403_PMID31273299.txt_CC2.xml,
Words: 165,
Tokens: 303\
Tag data:
Total: 3,
Unique: 3,
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
Schema counts (B, I, E, S): (0, 0, 0, 3)

**Title**:
394_PMID33093458.txt_CC2.xml,
Words: 300,
Tokens: 593\
Tag data:
Total: 28,
Unique: 19,
Max tags: 1,
Tagged words: 28 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 1, 8, 11)

**Title**:
90_PMID31983283.txt_CC2.xml,
Words: 243,
Tokens: 480\
Tag data:
Total: 3,
Unique: 3,
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
Schema counts (B, I, E, S): (0, 0, 0, 3)

**Title**:
255_PMID32354837.txt_CC2.xml,
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
572_PMID30430397.txt_CC2.xml,
Words: 215,
Tokens: 408\
Tag data:
Total: 22,
Unique: 18,
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
Schema counts (B, I, E, S): (3, 1, 3, 15)

**Title**:
157_PMID32132110.txt_CC2.xml,
Words: 242,
Tokens: 374\
Tag data:
Total: 25,
Unique: 8,
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
Schema counts (B, I, E, S): (6, 11, 6, 2)

**Title**:
650_PMID32659862.txt_CC2.xml,
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
720_PMID32679108.txt_CC2.xml,
Words: 122,
Tokens: 215\
Tag data:
Total: 12,
Unique: 7,
Max tags: 1,
Tagged words: 12 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 2, 3, 4)

**Title**:
25_PMID31203721.txt_CC2.xml,
Words: 209,
Tokens: 396\
Tag data:
Total: 31,
Unique: 10,
Max tags: 1,
Tagged words: 31 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (9, 12, 9, 1)

**Title**:
204_PMID28143833.txt_CC2.xml,
Words: 205,
Tokens: 301\
Tag data:
Total: 13,
Unique: 8,
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
Schema counts (B, I, E, S): (4, 1, 4, 4)

**Title**:
285_PMID29891559.txt_CC2.xml,
Words: 188,
Tokens: 345\
Tag data:
Total: 35,
Unique: 15,
Max tags: 1,
Tagged words: 35 (19%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (22.86%), 8 (4.26%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (13, 7, 13, 2)

**Title**:
87_PMID32160082.txt_CC2.xml,
Words: 258,
Tokens: 538\
Tag data:
Total: 61,
Unique: 23,
Max tags: 1,
Tagged words: 61 (24%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (13.11%), 8 (3.1%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (10, 28, 10, 13)

**Title**:
800_PMID31631026.txt_CC2.xml,
Words: 129,
Tokens: 281\
Tag data:
Total: 17,
Unique: 10,
Max tags: 1,
Tagged words: 17 (13%),
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
57_PMID30982460.txt_CC2.xml,
Words: 159,
Tokens: 317\
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
336_PMID32943605.txt_CC2.xml,
Words: 246,
Tokens: 465\
Tag data:
Total: 11,
Unique: 8,
Max tags: 1,
Tagged words: 11 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 1, 2, 6)

**Title**:
472_PMID31222041.txt_CC2.xml,
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
404_PMID32203170.txt_CC2.xml,
Words: 254,
Tokens: 557\
Tag data:
Total: 30,
Unique: 22,
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
Schema counts (B, I, E, S): (4, 4, 4, 18)

**Title**:
589_PMID31177396.txt_CC2.xml,
Words: 201,
Tokens: 336\
Tag data:
Total: 12,
Unique: 8,
Max tags: 1,
Tagged words: 12 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (58.33%), 7 (3.48%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 1, 3, 5)

**Title**:
156_PMID32816905.txt_CC2.xml,
Words: 249,
Tokens: 437\
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
Schema counts (B, I, E, S): (3, 3, 3, 1)

**Title**:
95_PMID31983282.txt_CC2.xml,
Words: 191,
Tokens: 389\
Tag data:
Total: 15,
Unique: 4,
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
Schema counts (B, I, E, S): (2, 9, 2, 2)

**Title**:
594_PMID28168327.txt_CC2.xml,
Words: 207,
Tokens: 369\
Tag data:
Total: 24,
Unique: 13,
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
Schema counts (B, I, E, S): (6, 5, 6, 7)

**Title**:
108_PMID33184108.txt_CC2.xml,
Words: 215,
Tokens: 349\
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
Schema counts (B, I, E, S): (2, 1, 2, 3)

**Title**:
80_PMID31238825.txt_CC2.xml,
Words: 210,
Tokens: 404\
Tag data:
Total: 19,
Unique: 9,
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
Schema counts (B, I, E, S): (4, 6, 4, 5)

**Title**:
317_PMID33188203.txt_CC2.xml,
Words: 117,
Tokens: 226\
Tag data:
Total: 7,
Unique: 3,
Max tags: 1,
Tagged words: 7 (6%),
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
73_PMID30444165.txt_CC2.xml,
Words: 260,
Tokens: 518\
Tag data:
Total: 43,
Unique: 24,
Max tags: 1,
Tagged words: 43 (17%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 39,
Unique: 5,
Max links (tag, word): (2, 2),
Linked (tags, words): (33 (76.74%), 33 (12.69%))\
Avg links (tag, word): (1.18, 1.18),
Schema counts (B, I, E, S): (8, 11, 8, 16)

**Title**:
395_PMID33243998.txt_CC2.xml,
Words: 237,
Tokens: 443\
Tag data:
Total: 45,
Unique: 16,
Max tags: 1,
Tagged words: 45 (19%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (11, 18, 11, 5)

**Title**:
726_PMID31668947.txt_CC2.xml,
Words: 124,
Tokens: 243\
Tag data:
Total: 18,
Unique: 3,
Max tags: 1,
Tagged words: 18 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 12, 3, 0)

**Title**:
574_PMID25953318.txt_CC2.xml,
Words: 249,
Tokens: 498\
Tag data:
Total: 25,
Unique: 18,
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
Schema counts (B, I, E, S): (2, 5, 2, 16)

**Title**:
410_PMID31285543.txt_CC2.xml,
Words: 153,
Tokens: 278\
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
77_PMID30806153.txt_CC2.xml,
Words: 190,
Tokens: 422\
Tag data:
Total: 15,
Unique: 9,
Max tags: 1,
Tagged words: 15 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (53.33%), 8 (4.21%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (2, 4, 2, 7)

**Title**:
759_PMID30423294.txt_CC2.xml,
Words: 131,
Tokens: 215\
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
333_PMID32938906.txt_CC2.xml,
Words: 180,
Tokens: 374\
Tag data:
Total: 18,
Unique: 10,
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
542_PMID31894447.txt_CC2.xml,
Words: 223,
Tokens: 386\
Tag data:
Total: 23,
Unique: 15,
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
Schema counts (B, I, E, S): (2, 6, 2, 13)

**Title**:
276_PMID31879538.txt_CC2.xml,
Words: 182,
Tokens: 322\
Tag data:
Total: 23,
Unique: 12,
Max tags: 1,
Tagged words: 23 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 21,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (15 (65.22%), 15 (8.24%))\
Avg links (tag, word): (1.4, 1.4),
Schema counts (B, I, E, S): (6, 5, 6, 6)

**Title**:
144_PMID33023943.txt_CC2.xml,
Words: 177,
Tokens: 273\
Tag data:
Total: 22,
Unique: 6,
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
Schema counts (B, I, E, S): (5, 11, 5, 1)

**Title**:
21_PMID31184563.txt_CC2.xml,
Words: 223,
Tokens: 407\
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
Schema counts (B, I, E, S): (5, 3, 5, 2)

**Title**:
67_PMID30661440.txt_CC2.xml,
Words: 225,
Tokens: 409\
Tag data:
Total: 17,
Unique: 12,
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
Schema counts (B, I, E, S): (4, 1, 4, 8)

**Title**:
162_PMID32737118.txt_CC2.xml,
Words: 236,
Tokens: 412\
Tag data:
Total: 16,
Unique: 11,
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
Schema counts (B, I, E, S): (5, 0, 5, 6)

**Title**:
382_PMID33188167.txt_CC2.xml,
Words: 269,
Tokens: 421\
Tag data:
Total: 20,
Unique: 6,
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
Schema counts (B, I, E, S): (6, 8, 6, 0)

**Title**:
555_PMID33230593.txt_CC2.xml,
Words: 230,
Tokens: 468\
Tag data:
Total: 18,
Unique: 15,
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
Schema counts (B, I, E, S): (3, 0, 3, 12)

**Title**:
110_PMID32127356.txt_CC2.xml,
Words: 291,
Tokens: 528\
Tag data:
Total: 10,
Unique: 6,
Max tags: 1,
Tagged words: 10 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (3, 1, 3, 3)

**Title**:
521_PMID31227933.txt_CC2.xml,
Words: 264,
Tokens: 533\
Tag data:
Total: 12,
Unique: 10,
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
Schema counts (B, I, E, S): (2, 0, 2, 8)

**Title**:
529_PMID31111379.txt_CC2.xml,
Words: 262,
Tokens: 631\
Tag data:
Total: 34,
Unique: 25,
Max tags: 1,
Tagged words: 34 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 4, 5, 20)

**Title**:
338_PMID33110074.txt_CC2.xml,
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
92_PMID_30894052.txt_CC2.xml,
Words: 161,
Tokens: 312\
Tag data:
Total: 25,
Unique: 14,
Max tags: 1,
Tagged words: 25 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 6, 5, 9)

**Title**:
640_PMID32783915.txt_CC2.xml,
Words: 162,
Tokens: 273\
Tag data:
Total: 12,
Unique: 6,
Max tags: 1,
Tagged words: 12 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (66.67%), 8 (4.94%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 2, 4, 2)

**Title**:
530_PMID30796611.txt_CC2.xml,
Words: 219,
Tokens: 349\
Tag data:
Total: 58,
Unique: 33,
Max tags: 2,
Tagged words: 57 (26%),
Avg tags: 1.02,
MC words: 1\
Link data:
Total: 26,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (20 (34.48%), 20 (9.13%))\
Avg links (tag, word): (1.3, 1.3),
Schema counts (B, I, E, S): (16, 9, 16, 17)

**Title**:
718_PMID31185212.txt_CC2.xml,
Words: 137,
Tokens: 285\
Tag data:
Total: 22,
Unique: 10,
Max tags: 1,
Tagged words: 22 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (31.82%), 7 (5.11%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 6, 6, 4)

**Title**:
40_PMID31920150.txt_CC2.xml,
Words: 165,
Tokens: 314\
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
413_PMID33097833.txt_CC2.xml,
Words: 236,
Tokens: 450\
Tag data:
Total: 26,
Unique: 12,
Max tags: 1,
Tagged words: 26 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 9, 5, 7)

**Title**:
298_PMID31058545.txt_CC2.xml,
Words: 172,
Tokens: 358\
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
174_PMID33239430.txt_CC2.xml,
Words: 131,
Tokens: 226\
Tag data:
Total: 16,
Unique: 8,
Max tags: 1,
Tagged words: 16 (12%),
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
343_PMID33099578.txt_CC2.xml,
Words: 212,
Tokens: 358\
Tag data:
Total: 15,
Unique: 8,
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
249_PMID32115406.txt_CC2.xml,
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
386_PMID33311446.txt_CC2.xml,
Words: 155,
Tokens: 304\
Tag data:
Total: 6,
Unique: 4,
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
218_PMID32439635.txt_CC2.xml,
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
Schema counts (B, I, E, S): (1, 0, 1, 0)

**Title**:
434_PMID33208891.txt_CC2.xml,
Words: 302,
Tokens: 515\
Tag data:
Total: 31,
Unique: 16,
Max tags: 1,
Tagged words: 31 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (16.13%), 5 (1.66%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (10, 5, 10, 6)

**Title**:
602_PMID33301708.txt_CC2.xml,
Words: 151,
Tokens: 260\
Tag data:
Total: 19,
Unique: 11,
Max tags: 1,
Tagged words: 19 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 0, 8, 3)

**Title**:
341_PMID33097685.txt_CC2.xml,
Words: 225,
Tokens: 404\
Tag data:
Total: 24,
Unique: 14,
Max tags: 2,
Tagged words: 23 (10%),
Avg tags: 1.04,
MC words: 1\
Link data:
Total: 36,
Unique: 5,
Max links (tag, word): (3, 3),
Linked (tags, words): (21 (87.5%), 20 (8.89%))\
Avg links (tag, word): (1.71, 1.8),
Schema counts (B, I, E, S): (9, 1, 9, 5)

**Title**:
559_PMID30911960.txt_CC2.xml,
Words: 219,
Tokens: 409\
Tag data:
Total: 13,
Unique: 9,
Max tags: 1,
Tagged words: 13 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (61.54%), 8 (3.65%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (1, 3, 1, 8)

**Title**:
557_PMID32632545.txt_CC2.xml,
Words: 184,
Tokens: 377\
Tag data:
Total: 12,
Unique: 8,
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
Schema counts (B, I, E, S): (2, 2, 2, 6)

**Title**:
737_PMID31526760.txt_CC2.xml,
Words: 119,
Tokens: 228\
Tag data:
Total: 13,
Unique: 8,
Max tags: 1,
Tagged words: 13 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 2, 4, 3)

**Title**:
430_PMID29317762.txt_CC2.xml,
Words: 239,
Tokens: 438\
Tag data:
Total: 40,
Unique: 24,
Max tags: 1,
Tagged words: 40 (17%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 50,
Unique: 7,
Max links (tag, word): (4, 4),
Linked (tags, words): (35 (87.5%), 35 (14.64%))\
Avg links (tag, word): (1.43, 1.43),
Schema counts (B, I, E, S): (11, 5, 11, 13)

**Title**:
777_PMID30537512.txt_CC2.xml,
Words: 140,
Tokens: 242\
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
142_PMID33277366.txt_CC2.xml,
Words: 185,
Tokens: 326\
Tag data:
Total: 9,
Unique: 5,
Max tags: 1,
Tagged words: 9 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (88.89%), 8 (4.32%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 1, 3, 2)

**Title**:
577_PMID31867678.txt_CC2.xml,
Words: 240,
Tokens: 388\
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
Schema counts (B, I, E, S): (1, 1, 1, 2)

**Title**:
365_PMID33110058.txt_CC2.xml,
Words: 187,
Tokens: 297\
Tag data:
Total: 26,
Unique: 11,
Max tags: 1,
Tagged words: 26 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 14,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (14 (53.85%), 14 (7.49%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 8, 7, 4)

**Title**:
132_PMID32366477.txt_CC2.xml,
Words: 183,
Tokens: 314\
Tag data:
Total: 31,
Unique: 14,
Max tags: 1,
Tagged words: 31 (17%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 9, 8, 6)

**Title**:
177_PMID33229341.txt_CC2.xml,
Words: 216,
Tokens: 436\
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
459_PMID33100324.txt_CC2.xml,
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
50_PMID31868081.txt_CC2.xml,
Words: 255,
Tokens: 457\
Tag data:
Total: 11,
Unique: 6,
Max tags: 1,
Tagged words: 11 (4%),
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
388_PMID33318476.txt_CC2.xml,
Words: 187,
Tokens: 309\
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
Schema counts (B, I, E, S): (1, 0, 1, 2)

**Title**:
425_PMID32814880.txt_CC2.xml,
Words: 272,
Tokens: 507\
Tag data:
Total: 54,
Unique: 15,
Max tags: 1,
Tagged words: 54 (20%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 59,
Unique: 5,
Max links (tag, word): (3, 3),
Linked (tags, words): (51 (94.44%), 51 (18.75%))\
Avg links (tag, word): (1.16, 1.16),
Schema counts (B, I, E, S): (10, 29, 10, 5)

**Title**:
583_PMID32409930.txt_CC2.xml,
Words: 208,
Tokens: 327\
Tag data:
Total: 18,
Unique: 14,
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
Schema counts (B, I, E, S): (4, 0, 4, 10)

**Title**:
436_PMID30903103.txt_CC2.xml,
Words: 260,
Tokens: 529\
Tag data:
Total: 27,
Unique: 8,
Max tags: 1,
Tagged words: 27 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 13, 6, 2)

**Title**:
159_PMID32973082.txt_CC2.xml,
Words: 277,
Tokens: 661\
Tag data:
Total: 27,
Unique: 7,
Max tags: 1,
Tagged words: 27 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 13, 7, 0)

**Title**:
284_PMID32354836.txt_CC2.xml,
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
653_PMID33142117.txt_CC2.xml,
Words: 153,
Tokens: 289\
Tag data:
Total: 14,
Unique: 9,
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
Schema counts (B, I, E, S): (5, 0, 5, 4)

**Title**:
789_PMID29805077.txt_CC2.xml,
Words: 132,
Tokens: 280\
Tag data:
Total: 6,
Unique: 4,
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
776_PMID33186519.txt_CC2.xml,
Words: 160,
Tokens: 283\
Tag data:
Total: 20,
Unique: 13,
Max tags: 1,
Tagged words: 20 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (25.0%), 5 (3.12%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 1, 6, 7)

**Title**:
482_PMID31367013.txt_CC2.xml,
Words: 212,
Tokens: 459\
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
445_PMID31988495.txt_CC2.xml,
Words: 241,
Tokens: 397\
Tag data:
Total: 16,
Unique: 6,
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
Schema counts (B, I, E, S): (5, 5, 5, 1)

**Title**:
561_PMID32737651.txt_CC2.xml,
Words: 249,
Tokens: 458\
Tag data:
Total: 40,
Unique: 19,
Max tags: 2,
Tagged words: 39 (16%),
Avg tags: 1.03,
MC words: 1\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (13, 8, 13, 6)

**Title**:
191_PMID32156781.txt_CC2.xml,
Words: 257,
Tokens: 435\
Tag data:
Total: 13,
Unique: 7,
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
Schema counts (B, I, E, S): (5, 1, 5, 2)

**Title**:
491_PMID31101885.txt_CC2.xml,
Words: 155,
Tokens: 248\
Tag data:
Total: 27,
Unique: 11,
Max tags: 1,
Tagged words: 27 (17%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 10,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (10 (37.04%), 10 (6.45%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (10, 6, 10, 1)

**Title**:
688_PMID32822574.txt_CC2.xml,
Words: 159,
Tokens: 279\
Tag data:
Total: 12,
Unique: 5,
Max tags: 1,
Tagged words: 12 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (2, 5, 2, 3)

**Title**:
109_PMID32217697.txt_CC2.xml,
Words: 213,
Tokens: 429\
Tag data:
Total: 16,
Unique: 9,
Max tags: 1,
Tagged words: 16 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 21,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (11 (68.75%), 11 (5.16%))\
Avg links (tag, word): (1.91, 1.91),
Schema counts (B, I, E, S): (6, 1, 6, 3)

**Title**:
164_PMID32019869.txt_CC2.xml,
Words: 192,
Tokens: 302\
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
470_PMID31332295.txt_CC2.xml,
Words: 158,
Tokens: 259\
Tag data:
Total: 16,
Unique: 10,
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
Schema counts (B, I, E, S): (6, 0, 6, 4)

**Title**:
283_PMID32273287.txt_CC2.xml,
Words: 218,
Tokens: 379\
Tag data:
Total: 13,
Unique: 6,
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
Schema counts (B, I, E, S): (5, 2, 5, 1)

**Title**:
308_PMID33097690.txt_CC2.xml,
Words: 302,
Tokens: 572\
Tag data:
Total: 14,
Unique: 10,
Max tags: 1,
Tagged words: 14 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 16,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (13 (92.86%), 13 (4.3%))\
Avg links (tag, word): (1.23, 1.23),
Schema counts (B, I, E, S): (2, 2, 2, 8)

**Title**:
651_PMID33333024.txt_CC2.xml,
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
120_PMID32122909.txt_CC2.xml,
Words: 288,
Tokens: 599\
Tag data:
Total: 17,
Unique: 9,
Max tags: 1,
Tagged words: 17 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (52.94%), 9 (3.12%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 4, 4, 5)

**Title**:
100_PMID31462126.txt_CC2.xml,
Words: 141,
Tokens: 277\
Tag data:
Total: 35,
Unique: 20,
Max tags: 1,
Tagged words: 35 (25%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 14,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (8 (22.86%), 8 (5.67%))\
Avg links (tag, word): (1.75, 1.75),
Schema counts (B, I, E, S): (7, 8, 7, 13)

**Title**:
66_PMID31512556.txt_CC2.xml,
Words: 184,
Tokens: 404\
Tag data:
Total: 17,
Unique: 12,
Max tags: 1,
Tagged words: 17 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 1, 4, 8)

**Title**:
560_PMID32591959.txt_CC2.xml,
Words: 196,
Tokens: 351\
Tag data:
Total: 16,
Unique: 8,
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
Schema counts (B, I, E, S): (5, 3, 5, 3)

**Title**:
307_PMID33144579.txt_CC2.xml,
Words: 209,
Tokens: 393\
Tag data:
Total: 38,
Unique: 25,
Max tags: 1,
Tagged words: 38 (18%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 7, 6, 19)

**Title**:
765_PMID32470390.txt_CC2.xml,
Words: 133,
Tokens: 254\
Tag data:
Total: 8,
Unique: 5,
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
Schema counts (B, I, E, S): (2, 1, 2, 3)

**Title**:
168_PMID32900774.txt_CC2.xml,
Words: 218,
Tokens: 354\
Tag data:
Total: 22,
Unique: 12,
Max tags: 1,
Tagged words: 22 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 15,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (15 (68.18%), 15 (6.88%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 4, 6, 6)

**Title**:
167_PMID33293428.txt_CC2.xml,
Words: 214,
Tokens: 446\
Tag data:
Total: 14,
Unique: 8,
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
Schema counts (B, I, E, S): (2, 4, 2, 6)

**Title**:
511_PMID31974865.txt_CC2.xml,
Words: 232,
Tokens: 446\
Tag data:
Total: 18,
Unique: 5,
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
Schema counts (B, I, E, S): (4, 9, 4, 1)

**Title**:
332_PMID33100331.txt_CC2.xml,
Words: 166,
Tokens: 348\
Tag data:
Total: 6,
Unique: 4,
Max tags: 1,
Tagged words: 6 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (100.0%), 6 (3.61%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (2, 0, 2, 2)

**Title**:
396_PMID33257682.txt_CC2.xml,
Words: 264,
Tokens: 436\
Tag data:
Total: 18,
Unique: 8,
Max tags: 1,
Tagged words: 18 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (27.78%), 5 (1.89%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 6, 4, 4)

**Title**:
489_PMID33277577.txt_CC2.xml,
Words: 278,
Tokens: 528\
Tag data:
Total: 17,
Unique: 7,
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
Schema counts (B, I, E, S): (4, 6, 4, 3)

**Title**:
124_PMID32665355.txt_CC2.xml,
Words: 235,
Tokens: 437\
Tag data:
Total: 36,
Unique: 17,
Max tags: 1,
Tagged words: 36 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 30,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (25 (69.44%), 25 (10.64%))\
Avg links (tag, word): (1.2, 1.2),
Schema counts (B, I, E, S): (9, 10, 9, 8)

**Title**:
648_PMID33147444.txt_CC2.xml,
Words: 176,
Tokens: 349\
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
769_PMID29533781.txt_CC2.xml,
Words: 128,
Tokens: 255\
Tag data:
Total: 14,
Unique: 9,
Max tags: 1,
Tagged words: 14 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 0, 5, 4)

**Title**:
151_PMID32341035.txt_CC2.xml,
Words: 229,
Tokens: 385\
Tag data:
Total: 16,
Unique: 10,
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
Schema counts (B, I, E, S): (5, 1, 5, 5)

**Title**:
582_PMID30778709.txt_CC2.xml,
Words: 256,
Tokens: 501\
Tag data:
Total: 17,
Unique: 11,
Max tags: 1,
Tagged words: 17 (7%),
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
719_PMID28697342.txt_CC2.xml,
Words: 131,
Tokens: 274\
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
713_PMID29657128.txt_CC2.xml,
Words: 132,
Tokens: 227\
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
342_PMID33082328.txt_CC2.xml,
Words: 209,
Tokens: 433\
Tag data:
Total: 24,
Unique: 13,
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
Schema counts (B, I, E, S): (9, 2, 9, 4)

**Title**:
268_PMID32561545.txt_CC2.xml,
Words: 192,
Tokens: 291\
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
362_PMID33051435.txt_CC2.xml,
Words: 202,
Tokens: 386\
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
Schema counts (B, I, E, S): (5, 6, 5, 4)

**Title**:
334_PMID33056982.txt_CC2.xml,
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
293_PMID31123067.txt_CC2.xml,
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
231_PMID30692207.txt_CC2.xml,
Words: 173,
Tokens: 345\
Tag data:
Total: 15,
Unique: 7,
Max tags: 1,
Tagged words: 15 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (46.67%), 7 (4.05%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 3, 5, 2)

**Title**:
203_PMID31831627.txt_CC2.xml,
Words: 201,
Tokens: 349\
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
Schema counts (B, I, E, S): (6, 4, 6, 1)

**Title**:
314_PMID32968054.txt_CC2.xml,
Words: 214,
Tokens: 372\
Tag data:
Total: 17,
Unique: 12,
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
Schema counts (B, I, E, S): (5, 0, 5, 7)

**Title**:
372_PMID33130818.txt_CC2.xml,
Words: 266,
Tokens: 537\
Tag data:
Total: 27,
Unique: 14,
Max tags: 1,
Tagged words: 27 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 13,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (13 (48.15%), 13 (4.89%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 6, 7, 7)

**Title**:
376_PMID33139721.txt_CC2.xml,
Words: 273,
Tokens: 468\
Tag data:
Total: 19,
Unique: 6,
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
Schema counts (B, I, E, S): (5, 8, 5, 1)

**Title**:
610_PMID32645325.txt_CC2.xml,
Words: 145,
Tokens: 290\
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
587_PMID28176146.txt_CC2.xml,
Words: 248,
Tokens: 419\
Tag data:
Total: 27,
Unique: 13,
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
Schema counts (B, I, E, S): (6, 8, 6, 7)

**Title**:
53_PMID30774023.txt_CC2.xml,
Words: 207,
Tokens: 400\
Tag data:
Total: 25,
Unique: 13,
Max tags: 1,
Tagged words: 25 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 12,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (12 (48.0%), 12 (5.8%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 9, 3, 10)

**Title**:
351_PMID33097698.txt_CC2.xml,
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
129_PMID33483372.txt_CC2.xml,
Words: 218,
Tokens: 346\
Tag data:
Total: 28,
Unique: 16,
Max tags: 1,
Tagged words: 28 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (11, 1, 11, 5)

**Title**:
141_PMID32046982.txt_CC2.xml,
Words: 238,
Tokens: 360\
Tag data:
Total: 12,
Unique: 4,
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
Schema counts (B, I, E, S): (4, 4, 4, 0)

**Title**:
7_PMID31679460.txt_CC2.xml,
Words: 255,
Tokens: 598\
Tag data:
Total: 53,
Unique: 35,
Max tags: 2,
Tagged words: 52 (20%),
Avg tags: 1.02,
MC words: 1\
Link data:
Total: 17,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (15 (28.3%), 14 (5.49%))\
Avg links (tag, word): (1.13, 1.21),
Schema counts (B, I, E, S): (16, 2, 16, 19)

**Title**:
355_PMID33184290.txt_CC2.xml,
Words: 206,
Tokens: 343\
Tag data:
Total: 37,
Unique: 10,
Max tags: 1,
Tagged words: 37 (18%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 15,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (15 (40.54%), 15 (7.28%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 22, 5, 5)

**Title**:
531_PMID30610504.txt_CC2.xml,
Words: 263,
Tokens: 517\
Tag data:
Total: 24,
Unique: 14,
Max tags: 1,
Tagged words: 24 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 14,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (14 (58.33%), 14 (5.32%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 3, 7, 7)

**Title**:
138_PMID32127357.txt_CC2.xml,
Words: 217,
Tokens: 314\
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
407_PMID31114026.txt_CC2.xml,
Words: 195,
Tokens: 351\
Tag data:
Total: 30,
Unique: 17,
Max tags: 2,
Tagged words: 29 (15%),
Avg tags: 1.03,
MC words: 1\
Link data:
Total: 23,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (17 (56.67%), 16 (8.21%))\
Avg links (tag, word): (1.35, 1.44),
Schema counts (B, I, E, S): (8, 5, 8, 9)

**Title**:
536_PMID28856570.txt_CC2.xml,
Words: 192,
Tokens: 283\
Tag data:
Total: 19,
Unique: 13,
Max tags: 1,
Tagged words: 19 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (26.32%), 5 (2.6%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 1, 5, 8)

**Title**:
5_PMID30870073.txt_CC2.xml,
Words: 242,
Tokens: 491\
Tag data:
Total: 14,
Unique: 6,
Max tags: 1,
Tagged words: 14 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (35.71%), 5 (2.07%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 5, 3, 3)

**Title**:
399_PMID33203836.txt_CC2.xml,
Words: 198,
Tokens: 311\
Tag data:
Total: 25,
Unique: 17,
Max tags: 1,
Tagged words: 25 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 2, 6, 11)

**Title**:
59_PMID31876243.txt_CC2.xml,
Words: 201,
Tokens: 313\
Tag data:
Total: 17,
Unique: 9,
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
Schema counts (B, I, E, S): (1, 7, 1, 8)

**Title**:
189_PMID32094301.txt_CC2.xml,
Words: 251,
Tokens: 462\
Tag data:
Total: 26,
Unique: 7,
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
Schema counts (B, I, E, S): (6, 13, 6, 1)

**Title**:
262_PMID31488578.txt_CC2.xml,
Words: 177,
Tokens: 312\
Tag data:
Total: 13,
Unique: 8,
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
Schema counts (B, I, E, S): (3, 2, 3, 5)

**Title**:
316_PMID33009373.txt_1_CC2.xml,
Words: 241,
Tokens: 449\
Tag data:
Total: 28,
Unique: 15,
Max tags: 1,
Tagged words: 28 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 15,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (15 (53.57%), 15 (6.22%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (9, 4, 9, 6)

**Title**:
481_PMID31570854.txt_CC2.xml,
Words: 195,
Tokens: 382\
Tag data:
Total: 19,
Unique: 10,
Max tags: 1,
Tagged words: 19 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 16,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (10 (52.63%), 10 (5.13%))\
Avg links (tag, word): (1.6, 1.6),
Schema counts (B, I, E, S): (5, 4, 5, 5)

**Title**:
245_PMID30463905.txt_CC2.xml,
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
185_PMID32680921.txt_CC2.xml,
Words: 160,
Tokens: 317\
Tag data:
Total: 16,
Unique: 7,
Max tags: 1,
Tagged words: 16 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 12,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (12 (75.0%), 12 (7.5%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 6, 3, 4)

**Title**:
537_PMID29236199.txt_CC2.xml,
Words: 243,
Tokens: 441\
Tag data:
Total: 13,
Unique: 7,
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
Schema counts (B, I, E, S): (2, 4, 2, 5)

**Title**:
273_PMID31171699.txt_CC2.xml,
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
397_PMID33239622.txt_CC2.xml,
Words: 196,
Tokens: 327\
Tag data:
Total: 23,
Unique: 13,
Max tags: 1,
Tagged words: 23 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 14,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (9 (39.13%), 9 (4.59%))\
Avg links (tag, word): (1.56, 1.56),
Schema counts (B, I, E, S): (8, 2, 9, 4)

**Title**:
56_PMID32267786.txt_CC2.xml,
Words: 110,
Tokens: 200\
Tag data:
Total: 15,
Unique: 10,
Max tags: 1,
Tagged words: 15 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 1, 4, 6)

**Title**:
704_PMID32531268.txt_CC2.xml,
Words: 125,
Tokens: 225\
Tag data:
Total: 17,
Unique: 8,
Max tags: 1,
Tagged words: 17 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (52.94%), 9 (7.2%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 4, 5, 3)

**Title**:
657_PMID32621799.txt_CC2.xml,
Words: 159,
Tokens: 253\
Tag data:
Total: 13,
Unique: 9,
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
Schema counts (B, I, E, S): (2, 2, 2, 7)

**Title**:
70_PMID31448672.txt_CC2.xml,
Words: 179,
Tokens: 365\
Tag data:
Total: 22,
Unique: 10,
Max tags: 1,
Tagged words: 22 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (31.82%), 7 (3.91%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 6, 6, 4)


