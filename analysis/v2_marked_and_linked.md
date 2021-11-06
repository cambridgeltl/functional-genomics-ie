---
title: Rough Analysis of v2_marked_and_linked.json
geometry: margin=2cm
---

# General Information

* Num. Entries: 175
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

* Average words: 213.6
* Maximum words: 324
* Minimum words: 109\
* Average tokens: 408.2
* Maximum tokens: 653
* Minimum tokens: 224\
* Entries with over 512 tokens: 34/175, 19.43%


## Tags

### Maximums

* Total tags: 66
* Unique tags: 35
* Max tags: 2
* Tagged words: 66
* Tagged words %: 31.16%
* Avg tags: 1.06
* MC words: 2

### Averages

* Total tags: 26.84
* Unique tags: 13.88
* Max tags: 1.05
* Tagged words: 26.78
* Tagged words %: 12.7%
* Avg tags: 1.0
* MC words: 0.05


## Links

### Maximums

* Total links: 98
* Unique links: 11
* Max links per tag, word: 6, 6
* Linked tags, words: 51, 51
* Linked % tags, words: 100.0%, 18.96%
* Avg links per tag, word: 2.88, 2.88

### Averages

* Total links: 17.91
* Unique links: 2.25
* Max links per tag, word: 1.73, 1.73
* Linked tags, words: 12.91, 12.89
* Linked % tags, words: 51.92%, 6.16%
* Avg links per tag, word: 1.29, 1.29


## Schema

* Maximums (B, I, E, S): 17, 29, 17, 22
* Averages (B, I, E, S): 6.57, 6.39, 6.57, 7.31


## Labels

* Label: Total, Maximum per entry, Average per entry

### Categories

* Perturbing_Action: 1950, 48, 11.14
* Context: 1519, 28, 8.68
* Effect: 537, 11, 3.07
* Phenotype: 691, 14, 3.95

### Perturbing_Action

* -: 0, 0, 0.0
* Gene Loss-Of-Function: 600, 24, 3.43
* Gene Gain-Of-Function: 306, 24, 1.75
* Rnai/Knockdown: 414, 32, 2.37
* Pharmacological Inhibition: 374, 20, 2.14
* Pharmacological Augmentation: 58, 15, 0.33
* Other: 198, 25, 1.13

### Context

* -: 0, 0, 0.0
* Patient: 4, 2, 0.02
* Organism: 184, 9, 1.05
* Tissue/Organ: 78, 15, 0.45
* Neoplasm: 98, 9, 0.56
* Graft: 0, 0, 0.0
* Xenograft: 73, 9, 0.42
* Cells: 550, 15, 3.14
* Transformed Cells: 338, 17, 1.93
* Organoid: 7, 4, 0.04
* In Vitro: 83, 4, 0.47
* In Vivo: 104, 4, 0.59

### Effect

* -: 3, 3, 0.02
* Positive: 249, 8, 1.42
* Negative: 222, 6, 1.27
* Regulates: 8, 1, 0.05
* Rescues: 21, 4, 0.12
* No Effect: 34, 6, 0.19

### Phenotype

* -: 1, 1, 0.01
* Adhesion: 0, 0, 0.0
* Apoptosis: 110, 6, 0.63
* Anoikis: 1, 1, 0.01
* Autophagy: 85, 8, 0.49
* Cell Cycle Arrest: 16, 6, 0.09
* Cell Death: 48, 6, 0.27
* Cell Growth: 20, 4, 0.11
* Cell Survival: 7, 2, 0.04
* Colony Formation: 10, 2, 0.06
* Differentiation: 21, 3, 0.12
* Entosis: 0, 0, 0.0
* Epithelial-Mesenchymal Transition: 16, 4, 0.09
* Ferroptosis: 29, 8, 0.17
* Invasion: 15, 3, 0.09
* Metastasis: 53, 8, 0.3
* Migration: 18, 2, 0.1
* Mitophagy: 4, 2, 0.02
* Necroptosis: 5, 2, 0.03
* Necrosis: 5, 3, 0.03
* Oncosis: 3, 3, 0.02
* Proliferation: 64, 4, 0.37
* Pyroptosis: 3, 2, 0.02
* Quiescence: 2, 2, 0.01
* Self-Renewal: 8, 3, 0.05
* Senescence: 23, 4, 0.13
* Transformation: 4, 2, 0.02
* Tumour Growth: 48, 5, 0.27
* Tumourigenesis: 50, 6, 0.29
* Tumour Initiation: 10, 4, 0.06
* Tumour Progression: 8, 2, 0.05
* Tumour Regression: 4, 4, 0.02


# Information on each entry

**Title**:
166_PMID32060146.txt_CC2.xml,
Words: 269,
Tokens: 431\
Tag data:
Total: 24,
Unique: 10,
Max tags: 1,
Tagged words: 24 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 29,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (22 (91.67%), 22 (8.18%))\
Avg links (tag, word): (1.32, 1.32),
Schema counts (B, I, E, S): (7, 7, 7, 3)

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
143_PMID330223944.txt_CC2.xml,
Words: 183,
Tokens: 300\
Tag data:
Total: 8,
Unique: 4,
Max tags: 1,
Tagged words: 8 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (100.0%), 8 (4.37%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 1, 3, 1)

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
706_PMID31935369.txt_CC2.xml,
Words: 127,
Tokens: 255\
Tag data:
Total: 25,
Unique: 12,
Max tags: 1,
Tagged words: 25 (20%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 18,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (14 (56.0%), 14 (11.02%))\
Avg links (tag, word): (1.29, 1.29),
Schema counts (B, I, E, S): (5, 8, 5, 7)

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
575_PMID28879567.txt_CC2.xml,
Words: 196,
Tokens: 452\
Tag data:
Total: 30,
Unique: 21,
Max tags: 1,
Tagged words: 30 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 14,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (14 (46.67%), 14 (7.14%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 4, 5, 16)

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
417_PMID31320750.txt_CC2.xml,
Words: 273,
Tokens: 487\
Tag data:
Total: 29,
Unique: 18,
Max tags: 1,
Tagged words: 29 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 15,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (15 (51.72%), 15 (5.49%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 4, 7, 11)

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
64_PMID31775562.txt_CC2.xml,
Words: 215,
Tokens: 424\
Tag data:
Total: 51,
Unique: 27,
Max tags: 2,
Tagged words: 50 (23%),
Avg tags: 1.02,
MC words: 1\
Link data:
Total: 19,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (19 (37.25%), 19 (8.84%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (9, 15, 9, 18)

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
32_PMID30290714.txt_CC2.xml,
Words: 255,
Tokens: 462\
Tag data:
Total: 26,
Unique: 17,
Max tags: 1,
Tagged words: 26 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 13,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (9 (34.62%), 9 (3.53%))\
Avg links (tag, word): (1.44, 1.44),
Schema counts (B, I, E, S): (8, 1, 8, 9)

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
752_PMID31257072.txt_CC2.xml,
Words: 136,
Tokens: 282\
Tag data:
Total: 16,
Unique: 6,
Max tags: 1,
Tagged words: 16 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (43.75%), 7 (5.15%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 6, 4, 2)

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
207_PMID31488580.txt_CC2.xml,
Words: 109,
Tokens: 229\
Tag data:
Total: 21,
Unique: 9,
Max tags: 1,
Tagged words: 21 (19%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 16,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (16 (76.19%), 16 (14.68%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 6, 6, 3)

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
346_PMID33431801.txt_CC2.xml,
Words: 269,
Tokens: 593\
Tag data:
Total: 22,
Unique: 15,
Max tags: 1,
Tagged words: 22 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 4,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (4 (18.18%), 4 (1.49%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (2, 5, 2, 13)

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
596_PMID26456506.txt_CC2.xml,
Words: 262,
Tokens: 578\
Tag data:
Total: 66,
Unique: 35,
Max tags: 1,
Tagged words: 66 (25%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 36,
Unique: 5,
Max links (tag, word): (2, 2),
Linked (tags, words): (27 (40.91%), 27 (10.31%))\
Avg links (tag, word): (1.33, 1.33),
Schema counts (B, I, E, S): (13, 18, 13, 22)

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
84_PMID32075509.txt_CC2.xml,
Words: 265,
Tokens: 463\
Tag data:
Total: 42,
Unique: 17,
Max tags: 1,
Tagged words: 42 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 20,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (12 (28.57%), 12 (4.53%))\
Avg links (tag, word): (1.67, 1.67),
Schema counts (B, I, E, S): (8, 17, 8, 9)

**Title**:
114_PMID32312833.txt_CC2.xml,
Words: 176,
Tokens: 367\
Tag data:
Total: 12,
Unique: 8,
Max tags: 1,
Tagged words: 12 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 14,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (8 (66.67%), 8 (4.55%))\
Avg links (tag, word): (1.75, 1.75),
Schema counts (B, I, E, S): (3, 1, 3, 5)

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
360_PMID33257688.txt_CC2.xml,
Words: 199,
Tokens: 387\
Tag data:
Total: 62,
Unique: 30,
Max tags: 1,
Tagged words: 62 (31%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 65,
Unique: 7,
Max links (tag, word): (5, 5),
Linked (tags, words): (27 (43.55%), 27 (13.57%))\
Avg links (tag, word): (2.41, 2.41),
Schema counts (B, I, E, S): (17, 15, 17, 13)

**Title**:
194_PMID32699135.txt_CC2.xml,
Words: 196,
Tokens: 312\
Tag data:
Total: 6,
Unique: 4,
Max tags: 1,
Tagged words: 6 (3%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (100.0%), 6 (3.06%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (2, 0, 2, 2)

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
310_PMID32934217.txt_CC2.xml,
Words: 262,
Tokens: 452\
Tag data:
Total: 19,
Unique: 13,
Max tags: 1,
Tagged words: 19 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (31.58%), 6 (2.29%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 2, 4, 9)

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
304_PMID32999283.txt_CC2.xml,
Words: 160,
Tokens: 439\
Tag data:
Total: 26,
Unique: 13,
Max tags: 1,
Tagged words: 26 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (26.92%), 7 (4.38%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (9, 4, 9, 4)

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
86_PMID31865844.txt_CC2.xml,
Words: 182,
Tokens: 290\
Tag data:
Total: 21,
Unique: 7,
Max tags: 1,
Tagged words: 21 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 41,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (17 (80.95%), 17 (9.34%))\
Avg links (tag, word): (2.41, 2.41),
Schema counts (B, I, E, S): (5, 9, 5, 2)

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
458_PMID32999468.txt_CC2.xml,
Words: 253,
Tokens: 527\
Tag data:
Total: 42,
Unique: 23,
Max tags: 1,
Tagged words: 42 (17%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 19,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (19 (45.24%), 19 (7.51%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 12, 7, 16)

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
549_PMID32564202.txt_CC2.xml,
Words: 248,
Tokens: 506\
Tag data:
Total: 13,
Unique: 10,
Max tags: 1,
Tagged words: 13 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 9,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (6 (46.15%), 6 (2.42%))\
Avg links (tag, word): (1.5, 1.5),
Schema counts (B, I, E, S): (3, 0, 3, 7)

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
600_PMID26467923.txt_CC2.xml,
Words: 283,
Tokens: 504\
Tag data:
Total: 44,
Unique: 22,
Max tags: 1,
Tagged words: 44 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 14,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (14 (31.82%), 14 (4.95%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (12, 10, 12, 10)

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
24_PMID30859901.txt_CC2.xml,
Words: 260,
Tokens: 605\
Tag data:
Total: 36,
Unique: 21,
Max tags: 1,
Tagged words: 36 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 22,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (19 (52.78%), 19 (7.31%))\
Avg links (tag, word): (1.16, 1.16),
Schema counts (B, I, E, S): (5, 10, 5, 16)

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
147_PMID31941699.txt_CC2.xml,
Words: 180,
Tokens: 295\
Tag data:
Total: 32,
Unique: 12,
Max tags: 1,
Tagged words: 32 (18%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (21.88%), 7 (3.89%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 15, 5, 7)

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


