---
title: Rough Analysis of v2_all_marked.json
geometry: margin=2cm
---

# General Information

* Num. Entries: 234
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

* Average words: 208.4
* Maximum words: 291
* Minimum words: 105\
* Average tokens: 387.7
* Maximum tokens: 661
* Minimum tokens: 184\
* Entries with over 512 tokens: 20/234, 8.55%


## Tags

### Maximums

* Total tags: 61
* Unique tags: 35
* Max tags: 2
* Tagged words: 61
* Tagged words %: 26.32%
* Avg tags: 1.04
* MC words: 1

### Averages

* Total tags: 16.52
* Unique tags: 8.08
* Max tags: 1.0
* Tagged words: 16.5
* Tagged words %: 7.87%
* Avg tags: 0.98
* MC words: 0.01


## Links

### Maximums

* Total links: 70
* Unique links: 9
* Max links per tag, word: 6, 6
* Linked tags, words: 40, 40
* Linked % tags, words: 100.0%, 17.09%
* Avg links per tag, word: 2.88, 2.88

### Averages

* Total links: 5.26
* Unique links: 0.63
* Max links per tag, word: 0.51, 0.51
* Linked tags, words: 3.73, 3.72
* Linked % tags, words: 15.23%, 1.74%
* Avg links per tag, word: 0.37, 0.37


## Schema

* Maximums (B, I, E, S): 16, 28, 16, 21
* Averages (B, I, E, S): 4.1, 4.34, 4.1, 3.97


## Labels

* Label: Total, Maximum per entry, Average per entry

### Categories

* Perturbing_Action: 1571, 48, 6.71
* Context: 1388, 28, 5.93
* Effect: 386, 11, 1.65
* Phenotype: 520, 12, 2.22

### Perturbing_Action

* Gene Loss-Of-Function: 622, 18, 2.66
* Gene Gain-Of-Function: 220, 24, 0.94
* Rnai/Knockdown: 212, 20, 0.91
* Pharmacological Inhibition: 263, 20, 1.12
* Pharmacological Augmentation: 66, 15, 0.28
* Other: 188, 15, 0.8

### Context

* Patient: 4, 3, 0.02
* Organism: 185, 9, 0.79
* Tissue/Organ: 69, 5, 0.29
* Neoplasm: 157, 11, 0.67
* Graft: 0, 0, 0.0
* Xenograft: 50, 7, 0.21
* Cells: 402, 15, 1.72
* Transformed Cells: 314, 14, 1.34
* Organoid: 25, 6, 0.11
* In Vitro: 80, 4, 0.34
* In Vivo: 102, 4, 0.44

### Effect

* Positive: 179, 5, 0.76
* Negative: 161, 6, 0.69
* Regulates: 6, 2, 0.03
* Rescues: 14, 4, 0.06
* No Effect: 26, 5, 0.11

### Phenotype

* Adhesion: 1, 1, 0.0
* Apoptosis: 23, 3, 0.1
* Anoikis: 1, 1, 0.0
* Autophagy: 125, 5, 0.53
* Cell Cycle Arrest: 10, 4, 0.04
* Cell Death: 14, 2, 0.06
* Cell Growth: 15, 4, 0.06
* Cell Survival: 6, 2, 0.03
* Colony Formation: 4, 2, 0.02
* Differentiation: 19, 2, 0.08
* Entosis: 0, 0, 0.0
* Epithelial-Mesenchymal Transition: 10, 4, 0.04
* Ferroptosis: 17, 8, 0.07
* Invasion: 7, 2, 0.03
* Metastasis: 56, 8, 0.24
* Migration: 14, 2, 0.06
* Mitophagy: 10, 2, 0.04
* Necroptosis: 0, 0, 0.0
* Necrosis: 3, 1, 0.01
* Oncosis: 0, 0, 0.0
* Proliferation: 38, 3, 0.16
* Pyroptosis: 0, 0, 0.0
* Quiescence: 2, 2, 0.01
* Self-Renewal: 6, 3, 0.03
* Senescence: 18, 4, 0.08
* Transformation: 7, 2, 0.03
* Tumour Growth: 50, 5, 0.21
* Tumourigenesis: 37, 6, 0.16
* Tumour Initiation: 6, 4, 0.03
* Tumour Progression: 6, 2, 0.03
* Tumour Regression: 15, 5, 0.06


# Information on each entry

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
254_PMID32217666.txt_CC2.xml,
Words: 204,
Tokens: 302\
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
250_PMID30842218.txt_CC2.xml,
Words: 160,
Tokens: 262\
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
247_PMID30366904.txt_CC2.xml,
Words: 114,
Tokens: 237\
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
251_PMID30842218.txt_CC2.xml,
Words: 160,
Tokens: 262\
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
248_PMID32217667.txt_CC2.xml,
Words: 199,
Tokens: 324\
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
201_PMID32079652.txt_CC2.xml,
Words: 231,
Tokens: 443\
Tag data:
Total: 15,
Unique: 7,
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
Schema counts (B, I, E, S): (3, 5, 3, 4)

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
243_PMID32943575.txt_CC2.xml,
Words: 105,
Tokens: 184\
Tag data:
Total: 6,
Unique: 5,
Max tags: 1,
Tagged words: 6 (6%),
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
55_PMID31177911.txt_CC2.xml,
Words: 187,
Tokens: 356\
Tag data:
Total: 19,
Unique: 16,
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
Schema counts (B, I, E, S): (2, 1, 2, 14)

**Title**:
297_PMID31919188.txt_CC2.xml,
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
200_PMID32522824.txt_CC2.xml,
Words: 250,
Tokens: 470\
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
Schema counts (B, I, E, S): (6, 4, 6, 1)

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
6_PMID30966861.txt_CC2.xml,
Words: 215,
Tokens: 429\
Tag data:
Total: 10,
Unique: 6,
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
Schema counts (B, I, E, S): (2, 2, 2, 4)

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
239_PMID32193353.txt_CC2.xml,
Words: 218,
Tokens: 382\
Tag data:
Total: 27,
Unique: 15,
Max tags: 1,
Tagged words: 27 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (8, 4, 8, 7)

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
118_PMID32816860.txt_CC2.xml,
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
Schema counts (B, I, E, S): (2, 0, 2, 1)

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
137_PMID32816913.txt_CC2.xml,
Words: 191,
Tokens: 356\
Tag data:
Total: 7,
Unique: 2,
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
Schema counts (B, I, E, S): (2, 3, 2, 0)

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
198_PMID32238357.txt_CC2.xml,
Words: 252,
Tokens: 472\
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
150_PMID32107212.txt_CC2.xml,
Words: 150,
Tokens: 290\
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
Schema counts (B, I, E, S): (1, 5, 1, 1)

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


