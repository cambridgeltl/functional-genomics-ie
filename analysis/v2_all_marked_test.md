---
title: Rough Analysis of v2_all_marked_test.json
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

* Average words: 203.8
* Maximum words: 327
* Minimum words: 105\
* Average tokens: 386.4
* Maximum tokens: 703
* Minimum tokens: 184\
* Entries with over 512 tokens: 7/59, 11.86%


## Tags

### Maximums

* Total tags: 66
* Unique tags: 35
* Max tags: 2
* Tagged words: 66
* Tagged words %: 31.16%
* Avg tags: 1.02
* MC words: 1

### Averages

* Total tags: 19.1
* Unique tags: 10.07
* Max tags: 1.02
* Tagged words: 19.08
* Tagged words %: 9.29%
* Avg tags: 1.0
* MC words: 0.02


## Links

### Maximums

* Total links: 65
* Unique links: 7
* Max links per tag, word: 5, 5
* Linked tags, words: 27, 27
* Linked % tags, words: 100.0%, 14.68%
* Avg links per tag, word: 2.41, 2.41

### Averages

* Total links: 6.93
* Unique links: 0.86
* Max links per tag, word: 0.64, 0.64
* Linked tags, words: 5.14, 5.14
* Linked % tags, words: 19.88%, 2.51%
* Avg links per tag, word: 0.5, 0.5


## Schema

* Maximums (B, I, E, S): 17, 18, 17, 22
* Averages (B, I, E, S): 4.8, 4.24, 4.8, 5.27


## Labels

* Label: Total, Maximum per entry, Average per entry

### Categories

* Perturbing_Action: 411, 35, 6.97
* Context: 415, 27, 7.03
* Effect: 137, 9, 2.32
* Phenotype: 164, 11, 2.78

### Perturbing_Action

* -: 0, 0, 0.0
* Gene Loss-Of-Function: 110, 18, 1.86
* Gene Gain-Of-Function: 62, 12, 1.05
* Rnai/Knockdown: 100, 32, 1.69
* Pharmacological Inhibition: 77, 11, 1.31
* Pharmacological Augmentation: 11, 8, 0.19
* Other: 51, 12, 0.86

### Context

* -: 0, 0, 0.0
* Patient: 6, 3, 0.1
* Organism: 65, 8, 1.1
* Tissue/Organ: 14, 4, 0.24
* Neoplasm: 24, 7, 0.41
* Graft: 0, 0, 0.0
* Xenograft: 13, 6, 0.22
* Cells: 154, 15, 2.61
* Transformed Cells: 70, 13, 1.19
* Organoid: 7, 4, 0.12
* In Vitro: 31, 6, 0.53
* In Vivo: 31, 4, 0.53

### Effect

* -: 0, 0, 0.0
* Positive: 68, 5, 1.15
* Negative: 54, 4, 0.92
* Regulates: 1, 1, 0.02
* Rescues: 3, 2, 0.05
* No Effect: 11, 5, 0.19

### Phenotype

* -: 0, 0, 0.0
* Adhesion: 0, 0, 0.0
* Apoptosis: 33, 6, 0.56
* Anoikis: 1, 1, 0.02
* Autophagy: 20, 5, 0.34
* Cell Cycle Arrest: 2, 2, 0.03
* Cell Death: 14, 6, 0.24
* Cell Growth: 6, 2, 0.1
* Cell Survival: 4, 2, 0.07
* Colony Formation: 0, 0, 0.0
* Differentiation: 2, 2, 0.03
* Entosis: 0, 0, 0.0
* Epithelial-Mesenchymal Transition: 5, 5, 0.08
* Ferroptosis: 18, 5, 0.31
* Invasion: 1, 1, 0.02
* Metastasis: 16, 8, 0.27
* Migration: 6, 2, 0.1
* Mitophagy: 2, 2, 0.03
* Necroptosis: 0, 0, 0.0
* Necrosis: 0, 0, 0.0
* Oncosis: 0, 0, 0.0
* Proliferation: 6, 2, 0.1
* Pyroptosis: 2, 1, 0.03
* Quiescence: 0, 0, 0.0
* Self-Renewal: 3, 3, 0.05
* Senescence: 5, 3, 0.08
* Transformation: 0, 0, 0.0
* Tumour Growth: 8, 4, 0.14
* Tumourigenesis: 0, 0, 0.0
* Tumour Initiation: 4, 4, 0.07
* Tumour Progression: 0, 0, 0.0
* Tumour Regression: 6, 2, 0.1


# Information on each entry

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
760_PMID32516590.txt_CC2.xml,
Words: 112,
Tokens: 209\
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
556_PMID29435687.txt_CC2.xml,
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
618_PMID33147445.txt_CC2.xml,
Words: 152,
Tokens: 246\
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
374_PMID33106471.txt.xml,
Words: 262,
Tokens: 533\
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
Schema counts (B, I, E, S): (6, 0, 6, 6)

**Title**:
339_PMID33288741.txt_CC2.xml,
Words: 157,
Tokens: 267\
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
660_PMID33002410.txt_CC2.xml,
Words: 163,
Tokens: 296\
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
580_PMID30084053.txt_CC2.xml,
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
359_PMID33116116.txt_CC2.xml,
Words: 207,
Tokens: 393\
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
Schema counts (B, I, E, S): (7, 0, 7, 1)

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
402_PMID30737476.txt_CC2.xml,
Words: 263,
Tokens: 483\
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
Schema counts (B, I, E, S): (6, 3, 6, 3)

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
723_PMID31715132.txt_CC2.xml,
Words: 126,
Tokens: 221\
Tag data:
Total: 25,
Unique: 10,
Max tags: 1,
Tagged words: 25 (20%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (5, 10, 5, 5)

**Title**:
493_PMID32139900.txt_CC2.xml,
Words: 248,
Tokens: 494\
Tag data:
Total: 12,
Unique: 6,
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
Schema counts (B, I, E, S): (4, 2, 4, 2)

**Title**:
627_PMID33308478.txt_CC2.xml,
Words: 166,
Tokens: 265\
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
371_PMID33323928.txt_CC2.xml,
Words: 218,
Tokens: 423\
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
Schema counts (B, I, E, S): (6, 0, 6, 2)

**Title**:
467_PMID29786075.txt_CC2.xml,
Words: 230,
Tokens: 394\
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
Schema counts (B, I, E, S): (2, 5, 2, 1)

**Title**:
551_PMID31605257.txt_CC2.xml,
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
541_PMID29936643.txt_CC2.xml,
Words: 327,
Tokens: 703\
Tag data:
Total: 14,
Unique: 9,
Max tags: 1,
Tagged words: 14 (4%),
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
373_PMID33436548.txt_CC2.xml,
Words: 262,
Tokens: 533\
Tag data:
Total: 20,
Unique: 12,
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
Schema counts (B, I, E, S): (7, 1, 7, 5)

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
322_PMID33051453.txt_CC2.xml,
Words: 262,
Tokens: 466\
Tag data:
Total: 29,
Unique: 11,
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
Schema counts (B, I, E, S): (9, 9, 9, 2)

**Title**:
743_PMID29533786.txt_CC2.xml,
Words: 128,
Tokens: 261\
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
406_PMID30568238.txt_CC2.xml,
Words: 164,
Tokens: 295\
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
Schema counts (B, I, E, S): (1, 2, 1, 7)

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
682_PMID33333020.txt_CC2.xml,
Words: 154,
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
724_PMID30753825.txt_CC2.xml,
Words: 138,
Tokens: 242\
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
321_PMID33188176.txt_CC2.xml,
Words: 179,
Tokens: 411\
Tag data:
Total: 21,
Unique: 11,
Max tags: 1,
Tagged words: 21 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 0,
Unique: 0,
Max links (tag, word): (0, 0),
Linked (tags, words): (0 (0.0%), 0 (0%))\
Avg links (tag, word): (0, 0),
Schema counts (B, I, E, S): (7, 3, 7, 4)

**Title**:
563_PMID29978434.txt_CC2.xml,
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
477_PMID32094512.txt_CC2.xml,
Words: 191,
Tokens: 368\
Tag data:
Total: 14,
Unique: 7,
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
Schema counts (B, I, E, S): (4, 3, 4, 3)

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


