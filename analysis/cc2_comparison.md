---
title: Rough Analysis of cc2_comparison.json
geometry: margin=2cm
---

# General Information

* Num. Entries: 50
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

* Average words: 208.9
* Maximum words: 286
* Minimum words: 11\
* Average tokens: 387.0
* Maximum tokens: 578
* Minimum tokens: 29\
* Entries with over 512 tokens: 4/50, 8.0%


## Tags

### Maximums

* Total tags: 66
* Unique tags: 35
* Max tags: 2
* Tagged words: 66
* Tagged words %: 25.19%
* Avg tags: 1.03
* MC words: 1

### Averages

* Total tags: 21.96
* Unique tags: 12.52
* Max tags: 0.94
* Tagged words: 21.94
* Tagged words %: 9.84%
* Avg tags: 0.92
* MC words: 0.02


## Links

### Maximums

* Total links: 52
* Unique links: 8
* Max links per tag, word: 4, 4
* Linked tags, words: 27, 27
* Linked % tags, words: 100.0%, 10.31%
* Avg links per tag, word: 2.54, 2.54

### Averages

* Total links: 5.46
* Unique links: 0.7
* Max links per tag, word: 0.5, 0.5
* Linked tags, words: 3.58, 3.58
* Linked % tags, words: 13.07%, 1.69%
* Avg links per tag, word: 0.41, 0.41


## Schema

* Maximums (B, I, E, S): 13, 18, 13, 22
* Averages (B, I, E, S): 4.86, 4.58, 4.86, 7.66


## Labels

* Label: Total, Maximum per entry, Average per entry

### Categories

* Perturbing_Action: 229, 35, 4.58
* Context: 474, 32, 9.48
* Effect: 172, 11, 3.44
* Phenotype: 223, 17, 4.46

### Perturbing_Action

* -: 0, 0, 0.0
* Gene Loss-Of-Function: 32, 14, 0.64
* Gene Gain-Of-Function: 21, 11, 0.42
* Rnai/Knockdown: 87, 32, 1.74
* Pharmacological Inhibition: 63, 9, 1.26
* Pharmacological Augmentation: 0, 0, 0.0
* Other: 26, 19, 0.52

### Context

* -: 2, 2, 0.04
* Patient: 2, 2, 0.04
* Organism: 33, 5, 0.66
* Tissue/Organ: 22, 7, 0.44
* Neoplasm: 15, 4, 0.3
* Graft: 0, 0, 0.0
* Xenograft: 5, 5, 0.1
* Cells: 263, 28, 5.26
* Transformed Cells: 96, 14, 1.92
* Organoid: 0, 0, 0.0
* In Vitro: 24, 6, 0.48
* In Vivo: 12, 2, 0.24

### Effect

* -: 0, 0, 0.0
* Positive: 97, 9, 1.94
* Negative: 58, 3, 1.16
* Regulates: 9, 2, 0.18
* Rescues: 0, 0, 0.0
* No Effect: 8, 4, 0.16

### Phenotype

* -: 0, 0, 0.0
* Adhesion: 0, 0, 0.0
* Apoptosis: 121, 8, 2.42
* Anoikis: 0, 0, 0.0
* Autophagy: 15, 5, 0.3
* Cell Cycle Arrest: 24, 7, 0.48
* Cell Death: 24, 12, 0.48
* Cell Growth: 4, 2, 0.08
* Cell Survival: 14, 7, 0.28
* Colony Formation: 2, 2, 0.04
* Differentiation: 0, 0, 0.0
* Entosis: 0, 0, 0.0
* Epithelial-Mesenchymal Transition: 0, 0, 0.0
* Ferroptosis: 0, 0, 0.0
* Invasion: 1, 1, 0.02
* Metastasis: 3, 3, 0.06
* Migration: 1, 1, 0.02
* Mitophagy: 0, 0, 0.0
* Necroptosis: 2, 2, 0.04
* Necrosis: 1, 1, 0.02
* Oncosis: 0, 0, 0.0
* Proliferation: 4, 1, 0.08
* Pyroptosis: 0, 0, 0.0
* Quiescence: 0, 0, 0.0
* Self-Renewal: 0, 0, 0.0
* Senescence: 0, 0, 0.0
* Transformation: 0, 0, 0.0
* Tumour Growth: 6, 4, 0.12
* Tumourigenesis: 1, 1, 0.02
* Tumour Initiation: 0, 0, 0.0
* Tumour Progression: 0, 0, 0.0
* Tumour Regression: 0, 0, 0.0


# Information on each entry

**Title**:
570_PMID29858716.txt.xml,
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
582_PMID30778709.txt.xml,
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
573_PMID30515612.txt.xml,
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
557_PMID32632545.txt.xml,
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
556_PMID29435687.txt.xml,
Words: 146,
Tokens: 283\
Tag data:
Total: 10,
Unique: 6,
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
Schema counts (B, I, E, S): (4, 0, 4, 2)

**Title**:
553_PMID29236198.txt.xml,
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
586_PMID31342239.txt.xml,
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
572_PMID30430397.txt.xml,
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
590_PMID26386572.txt.xml,
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
566_PMID30421279.txt.xml,
Words: 39,
Tokens: 68\
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
583_PMID32409930.txt.xml,
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
576_PMID30610505.txt.xml,
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
554_PMID31489517.txt.xml,
Words: 168,
Tokens: 288\
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
559_PMID30911960.txt.xml,
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
561_PMID32737651.txt.xml,
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
562_PMID31641960.txt.xml,
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
563_PMID29978434.txt.xml,
Words: 195,
Tokens: 302\
Tag data:
Total: 20,
Unique: 8,
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
Schema counts (B, I, E, S): (7, 5, 7, 1)

**Title**:
592_PMID30426280.txt.xml,
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
595_PMID30578463.txt.xml,
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
588_PMID26801321.txt.xml,
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
574_PMID25953318.txt.xml,
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
598_PMID25218423.txt.xml,
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
567_PMID27770267.txt.xml,
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
591_PMID32901335.txt.xml,
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
569_PMID28012059.txt.xml,
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
597_PMID30680481.txt.xml,
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
560_PMID32591959.txt.xml,
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
584_PMID32026186.txt.xml,
Words: 11,
Tokens: 29\
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
571_PMID31583496.txt.xml,
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
599_PMID32036474.txt.xml,
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
575_PMID28879567.txt.xml,
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
568_PMID32405891.txt.xml,
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
577_PMID31867678.txt.xml,
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
589_PMID31177396.txt.xml,
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
565_PMID31768842.txt.xml,
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
552_PMID29058102.txt.xml,
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
581_PMID32468177.txt.xml,
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
564_PMID30879166.txt.xml,
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
578_PMID31538267.txt.xml,
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
551_PMID31605257.txt.xml,
Words: 258,
Tokens: 412\
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
Schema counts (B, I, E, S): (3, 3, 3, 5)

**Title**:
558_PMID31691131.txt.xml,
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
587_PMID28176146.txt.xml,
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
600_PMID26467923.txt.xml,
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
555_PMID33230593.txt.xml,
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
594_PMID28168327.txt.xml,
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
580_PMID30084053.txt.xml,
Words: 215,
Tokens: 409\
Tag data:
Total: 15,
Unique: 9,
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
Schema counts (B, I, E, S): (4, 2, 4, 5)

**Title**:
585_PMID30879165.txt.xml,
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
593_PMID32583319.txt.xml,
Words: 19,
Tokens: 45\
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
579_PMID30788651.txt.xml,
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
596_PMID26456506.txt.xml,
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


