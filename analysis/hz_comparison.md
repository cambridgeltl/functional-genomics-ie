---
title: Rough Analysis of hz_comparison.json
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

* Total tags: 41
* Unique tags: 23
* Max tags: 2
* Tagged words: 41
* Tagged words %: 19.62%
* Avg tags: 1.05
* MC words: 0

### Averages

* Total tags: 16.18
* Unique tags: 9.46
* Max tags: 0.94
* Tagged words: 16.14
* Tagged words %: 7.31%
* Avg tags: 0.92
* MC words: 0.0


## Links

### Maximums

* Total links: 14
* Unique links: 2
* Max links per tag, word: 1, 1
* Linked tags, words: 14, 14
* Linked % tags, words: 52.94%, 6.7%
* Avg links per tag, word: 1.0, 1.0

### Averages

* Total links: 1.28
* Unique links: 0.2
* Max links per tag, word: 0.18, 0.18
* Linked tags, words: 1.28, 1.28
* Linked % tags, words: 5.59%, 0.62%
* Avg links per tag, word: 0.18, 0.18


## Schema

* Maximums (B, I, E, S): 13, 13, 13, 22
* Averages (B, I, E, S): 3.78, 2.94, 3.78, 5.68


## Labels

* Label: Total, Maximum per entry, Average per entry

### Categories

* Perturbing_Action: 170, 15, 3.4
* Context: 353, 27, 7.06
* Effect: 124, 10, 2.48
* Phenotype: 162, 13, 3.24

### Perturbing_Action

* -: 15, 12, 0.3
* Gene Loss-Of-Function: 21, 10, 0.42
* Gene Gain-Of-Function: 15, 4, 0.3
* Rnai/Knockdown: 50, 12, 1.0
* Pharmacological Inhibition: 64, 10, 1.28
* Pharmacological Augmentation: 0, 0, 0.0
* Other: 5, 3, 0.1

### Context

* -: 16, 13, 0.32
* Patient: 3, 3, 0.06
* Organism: 19, 5, 0.38
* Tissue/Organ: 20, 7, 0.4
* Neoplasm: 4, 4, 0.08
* Graft: 0, 0, 0.0
* Xenograft: 0, 0, 0.0
* Cells: 194, 24, 3.88
* Transformed Cells: 69, 9, 1.38
* Organoid: 0, 0, 0.0
* In Vitro: 16, 4, 0.32
* In Vivo: 12, 4, 0.24

### Effect

* -: 8, 4, 0.16
* Positive: 70, 5, 1.4
* Negative: 36, 3, 0.72
* Regulates: 3, 2, 0.06
* Rescues: 3, 2, 0.06
* No Effect: 4, 4, 0.08

### Phenotype

* -: 6, 4, 0.12
* Adhesion: 0, 0, 0.0
* Apoptosis: 80, 5, 1.6
* Anoikis: 0, 0, 0.0
* Autophagy: 10, 4, 0.2
* Cell Cycle Arrest: 16, 4, 0.32
* Cell Death: 21, 8, 0.42
* Cell Growth: 2, 2, 0.04
* Cell Survival: 10, 4, 0.2
* Colony Formation: 0, 0, 0.0
* Differentiation: 0, 0, 0.0
* Entosis: 0, 0, 0.0
* Epithelial-Mesenchymal Transition: 0, 0, 0.0
* Ferroptosis: 0, 0, 0.0
* Invasion: 1, 1, 0.02
* Metastasis: 1, 1, 0.02
* Migration: 1, 1, 0.02
* Mitophagy: 0, 0, 0.0
* Necroptosis: 0, 0, 0.0
* Necrosis: 1, 1, 0.02
* Oncosis: 0, 0, 0.0
* Proliferation: 6, 2, 0.12
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
562_PMID31641960.txt.xml,
Words: 236,
Tokens: 456\
Tag data:
Total: 5,
Unique: 5,
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
Schema counts (B, I, E, S): (0, 0, 0, 5)

**Title**:
568_PMID32405891.txt.xml,
Words: 262,
Tokens: 469\
Tag data:
Total: 27,
Unique: 10,
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
Schema counts (B, I, E, S): (6, 11, 6, 4)

**Title**:
555_PMID33230593.txt.xml,
Words: 230,
Tokens: 468\
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
579_PMID30788651.txt.xml,
Words: 255,
Tokens: 463\
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
589_PMID31177396.txt.xml,
Words: 201,
Tokens: 336\
Tag data:
Total: 17,
Unique: 8,
Max tags: 1,
Tagged words: 17 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (41.18%), 7 (3.48%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 4, 5, 3)

**Title**:
598_PMID25218423.txt.xml,
Words: 220,
Tokens: 456\
Tag data:
Total: 17,
Unique: 14,
Max tags: 1,
Tagged words: 17 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (29.41%), 5 (2.27%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (2, 1, 2, 12)

**Title**:
597_PMID30680481.txt.xml,
Words: 255,
Tokens: 524\
Tag data:
Total: 16,
Unique: 7,
Max tags: 1,
Tagged words: 16 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (43.75%), 7 (2.75%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 4, 5, 2)

**Title**:
552_PMID29058102.txt.xml,
Words: 201,
Tokens: 393\
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
572_PMID30430397.txt.xml,
Words: 215,
Tokens: 408\
Tag data:
Total: 24,
Unique: 16,
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
Schema counts (B, I, E, S): (4, 4, 4, 12)

**Title**:
565_PMID31768842.txt.xml,
Words: 225,
Tokens: 424\
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
Schema counts (B, I, E, S): (1, 4, 1, 7)

**Title**:
570_PMID29858716.txt.xml,
Words: 266,
Tokens: 423\
Tag data:
Total: 20,
Unique: 14,
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
Schema counts (B, I, E, S): (6, 0, 6, 8)

**Title**:
563_PMID29978434.txt.xml,
Words: 195,
Tokens: 302\
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
Schema counts (B, I, E, S): (4, 0, 4, 3)

**Title**:
599_PMID32036474.txt.xml,
Words: 266,
Tokens: 538\
Tag data:
Total: 27,
Unique: 17,
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
Schema counts (B, I, E, S): (9, 1, 9, 8)

**Title**:
569_PMID28012059.txt.xml,
Words: 205,
Tokens: 402\
Tag data:
Total: 24,
Unique: 10,
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
Schema counts (B, I, E, S): (7, 7, 7, 3)

**Title**:
551_PMID31605257.txt.xml,
Words: 258,
Tokens: 412\
Tag data:
Total: 9,
Unique: 4,
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
574_PMID25953318.txt.xml,
Words: 249,
Tokens: 498\
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
Schema counts (B, I, E, S): (3, 6, 3, 3)

**Title**:
571_PMID31583496.txt.xml,
Words: 213,
Tokens: 399\
Tag data:
Total: 33,
Unique: 18,
Max tags: 1,
Tagged words: 33 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (18.18%), 6 (2.82%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (9, 6, 9, 9)

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
594_PMID28168327.txt.xml,
Words: 207,
Tokens: 369\
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
Schema counts (B, I, E, S): (3, 3, 3, 3)

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
559_PMID30911960.txt.xml,
Words: 219,
Tokens: 409\
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
Schema counts (B, I, E, S): (1, 2, 1, 10)

**Title**:
581_PMID32468177.txt.xml,
Words: 231,
Tokens: 427\
Tag data:
Total: 17,
Unique: 9,
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
Schema counts (B, I, E, S): (4, 4, 4, 5)

**Title**:
591_PMID32901335.txt.xml,
Words: 145,
Tokens: 265\
Tag data:
Total: 22,
Unique: 12,
Max tags: 1,
Tagged words: 22 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (4, 6, 4, 8)

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
590_PMID26386572.txt.xml,
Words: 220,
Tokens: 428\
Tag data:
Total: 7,
Unique: 6,
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
Schema counts (B, I, E, S): (1, 0, 1, 5)

**Title**:
560_PMID32591959.txt.xml,
Words: 196,
Tokens: 351\
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
Schema counts (B, I, E, S): (4, 0, 4, 3)

**Title**:
577_PMID31867678.txt.xml,
Words: 240,
Tokens: 388\
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
575_PMID28879567.txt.xml,
Words: 196,
Tokens: 452\
Tag data:
Total: 21,
Unique: 14,
Max tags: 1,
Tagged words: 21 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (28.57%), 6 (3.06%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 4, 3, 11)

**Title**:
580_PMID30084053.txt.xml,
Words: 215,
Tokens: 409\
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
Schema counts (B, I, E, S): (4, 4, 4, 5)

**Title**:
587_PMID28176146.txt.xml,
Words: 248,
Tokens: 419\
Tag data:
Total: 13,
Unique: 9,
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
Schema counts (B, I, E, S): (2, 2, 2, 7)

**Title**:
595_PMID30578463.txt.xml,
Words: 262,
Tokens: 543\
Tag data:
Total: 41,
Unique: 21,
Max tags: 2,
Tagged words: 39 (15%),
Avg tags: 1.05,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (13, 7, 13, 8)

**Title**:
600_PMID26467923.txt.xml,
Words: 283,
Tokens: 504\
Tag data:
Total: 36,
Unique: 20,
Max tags: 1,
Tagged words: 36 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (16.67%), 6 (2.12%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (10, 6, 10, 10)

**Title**:
554_PMID31489517.txt.xml,
Words: 168,
Tokens: 288\
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
553_PMID29236198.txt.xml,
Words: 263,
Tokens: 444\
Tag data:
Total: 15,
Unique: 11,
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
Schema counts (B, I, E, S): (2, 2, 2, 9)

**Title**:
578_PMID31538267.txt.xml,
Words: 185,
Tokens: 350\
Tag data:
Total: 16,
Unique: 13,
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
Schema counts (B, I, E, S): (2, 1, 2, 11)

**Title**:
582_PMID30778709.txt.xml,
Words: 256,
Tokens: 501\
Tag data:
Total: 10,
Unique: 8,
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
Schema counts (B, I, E, S): (2, 0, 2, 6)

**Title**:
583_PMID32409930.txt.xml,
Words: 208,
Tokens: 327\
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
Schema counts (B, I, E, S): (4, 0, 4, 3)

**Title**:
561_PMID32737651.txt.xml,
Words: 249,
Tokens: 458\
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
Schema counts (B, I, E, S): (9, 5, 9, 4)

**Title**:
567_PMID27770267.txt.xml,
Words: 286,
Tokens: 479\
Tag data:
Total: 24,
Unique: 12,
Max tags: 1,
Tagged words: 24 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (6, 6, 6, 6)

**Title**:
588_PMID26801321.txt.xml,
Words: 224,
Tokens: 398\
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
564_PMID30879166.txt.xml,
Words: 235,
Tokens: 450\
Tag data:
Total: 26,
Unique: 10,
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
Schema counts (B, I, E, S): (4, 12, 4, 6)

**Title**:
556_PMID29435687.txt.xml,
Words: 146,
Tokens: 283\
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
Schema counts (B, I, E, S): (4, 0, 4, 1)

**Title**:
585_PMID30879165.txt.xml,
Words: 94,
Tokens: 149\
Tag data:
Total: 5,
Unique: 3,
Max tags: 1,
Tagged words: 5 (5%),
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
586_PMID31342239.txt.xml,
Words: 209,
Tokens: 397\
Tag data:
Total: 41,
Unique: 19,
Max tags: 1,
Tagged words: 41 (20%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 14,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (14 (34.15%), 14 (6.7%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (9, 13, 9, 10)

**Title**:
557_PMID32632545.txt.xml,
Words: 184,
Tokens: 377\
Tag data:
Total: 16,
Unique: 11,
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
Schema counts (B, I, E, S): (3, 2, 3, 8)

**Title**:
558_PMID31691131.txt.xml,
Words: 167,
Tokens: 294\
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
596_PMID26456506.txt.xml,
Words: 262,
Tokens: 578\
Tag data:
Total: 27,
Unique: 23,
Max tags: 1,
Tagged words: 27 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 4,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (4 (14.81%), 4 (1.53%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (1, 3, 1, 22)

**Title**:
573_PMID30515612.txt.xml,
Words: 225,
Tokens: 381\
Tag data:
Total: 31,
Unique: 22,
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
Schema counts (B, I, E, S): (6, 3, 6, 16)

**Title**:
592_PMID30426280.txt.xml,
Words: 148,
Tokens: 243\
Tag data:
Total: 17,
Unique: 7,
Max tags: 1,
Tagged words: 17 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (52.94%), 9 (6.08%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 5, 5, 2)

**Title**:
576_PMID30610505.txt.xml,
Words: 251,
Tokens: 478\
Tag data:
Total: 20,
Unique: 9,
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
Schema counts (B, I, E, S): (7, 4, 7, 2)


