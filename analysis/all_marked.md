---
title: Rough Analysis of all_marked.json
geometry: margin=2cm
---

# General Information

* Num. Entries: 582
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

* Average words: 205.0
* Maximum words: 353
* Minimum words: 94\
* Average tokens: 385.0
* Maximum tokens: 703
* Minimum tokens: 149\
* Entries with over 512 tokens: 69/582, 11.86%


## Tags

### Maximums

* Total tags: 85
* Unique tags: 32
* Max tags: 6
* Tagged words: 78
* Tagged words %: 39.2%
* Avg tags: 1.6
* MC words: 2

### Averages

* Total tags: 20.9
* Unique tags: 7.49
* Max tags: 1.42
* Tagged words: 19.68
* Tagged words %: 9.54%
* Avg tags: 1.05
* MC words: 0.02


## Links

### Maximums

* Total links: 143
* Unique links: 14
* Max links per tag, word: 10, 10
* Linked tags, words: 63, 57
* Linked % tags, words: 100.0%, 28.64%
* Avg links per tag, word: 4.48, 4.95

### Averages

* Total links: 8.65
* Unique links: 0.95
* Max links per tag, word: 0.71, 0.72
* Linked tags, words: 6.1, 5.76
* Linked % tags, words: 21.53%, 2.74%
* Avg links per tag, word: 0.5, 0.53


## Schema

* Maximums (B, I, E, S): 22, 41, 22, 29
* Averages (B, I, E, S): 5.7, 6.07, 5.7, 3.43


## Labels

* Label: Total, Maximum per entry, Average per entry

### Categories

* Perturbing_Action: 4101, 49, 7.05
* Context: 8606, 68, 14.79
* Effect: 7524, 80, 12.93

### Description

* Knock Out: 619, 47, 1.06
* Conditional Knock Out: 221, 15, 0.38
* Knock In: 24, 6, 0.04
* Conditional Knock In: 17, 4, 0.03
* Knock Down: 683, 45, 1.17
* Plasmid Vector: 41, 20, 0.07
* Viral Vector: 41, 10, 0.07
* Pharmacological Inhibition: 778, 20, 1.34
* Decreased Expression Level: 530, 18, 0.91
* Increased Expression Level: 426, 16, 0.73
* Other: 721, 26, 1.24

### Experiment_Type

* Organism: 837, 16, 1.44
* Tumour: 364, 17, 0.63
* Cells: 1527, 34, 2.62
* Cell Line: 191, 17, 0.33
* Transformed Cell Line: 995, 32, 1.71
* Primary Culture: 70, 7, 0.12
* Organoid Culture: 63, 14, 0.11
* Cell Transplantation: 0, 0, 0.0
* Xenotransplantation: 247, 24, 0.42
* Other: 3, 3, 0.01
* Not Stated: 6, 4, 0.01

### Species

* Human: 465, 27, 0.8
* Mouse: 750, 17, 1.29
* Rat: 64, 18, 0.11
* Fish: 4, 3, 0.01
* Fly: 15, 6, 0.03
* Yeast: 5, 3, 0.01
* Bacterium: 5, 5, 0.01
* Other: 39, 12, 0.07
* Not Stated: 2956, 32, 5.08

### Phenotype

* Adhesion: 13, 9, 0.02
* Apoptosis: 629, 17, 1.08
* Anoikis: 3, 3, 0.01
* Autophagy: 679, 23, 1.17
* Cell Cycle Arrest: 110, 14, 0.19
* Cell Death: 288, 24, 0.49
* Cell Growth: 155, 14, 0.27
* Cell Survival: 98, 7, 0.17
* Colony Formation: 31, 9, 0.05
* Differentiation: 113, 9, 0.19
* Entosis: 0, 0, 0.0
* Epithelial-Mesenchymal Transition: 53, 10, 0.09
* Ferroptosis: 146, 23, 0.25
* Invasion: 69, 13, 0.12
* Metastasis: 196, 17, 0.34
* Migration: 112, 13, 0.19
* Mitophagy: 59, 9, 0.1
* Necroptosis: 39, 7, 0.07
* Necrosis: 27, 7, 0.05
* Netosis: 0, 0, 0.0
* Oncosis: 12, 7, 0.02
* Proliferation: 264, 12, 0.45
* Pyroptosis: 22, 5, 0.04
* Quiescence: 13, 5, 0.02
* Self-Renewal: 39, 10, 0.07
* Senescence: 83, 14, 0.14
* Transformation: 43, 16, 0.07
* Tumour Growth: 258, 9, 0.44
* Tumourigenesis: 208, 18, 0.36

### Activity

* Causes: 855, 25, 1.47
* Inhibits: 680, 24, 1.17
* Increases: 899, 22, 1.54
* Decreases: 866, 19, 1.49
* Regulates: 166, 8, 0.29
* No Effect: 166, 29, 0.29
* Not Stated: 130, 14, 0.22


# Information on each entry

**Title**:
261_PMID30692209.txt_CC.xml,
Words: 166,
Tokens: 271\
Tag data:
Total: 24,
Unique: 11,
Max tags: 1,
Tagged words: 24 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 3,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (3 (12.5%), 3 (1.81%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (8, 3, 8, 5)

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
767_PMID30686770.txt_CC.xml,
Words: 128,
Tokens: 261\
Tag data:
Total: 11,
Unique: 4,
Max tags: 1,
Tagged words: 11 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 10,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (10 (90.91%), 10 (7.81%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 4, 3, 1)

**Title**:
166_PMID32060146.txt_CC.xml,
Words: 269,
Tokens: 431\
Tag data:
Total: 26,
Unique: 9,
Max tags: 2,
Tagged words: 25 (9%),
Avg tags: 1.04,
MC words: 0\
Link data:
Total: 30,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (24 (92.31%), 23 (8.55%))\
Avg links (tag, word): (1.25, 1.3),
Schema counts (B, I, E, S): (6, 10, 6, 4)

**Title**:
110_PMID32127356.txt_CC.xml,
Words: 291,
Tokens: 528\
Tag data:
Total: 19,
Unique: 6,
Max tags: 2,
Tagged words: 18 (6%),
Avg tags: 1.06,
MC words: 0\
Link data:
Total: 18,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (15 (78.95%), 14 (4.81%))\
Avg links (tag, word): (1.2, 1.29),
Schema counts (B, I, E, S): (5, 3, 5, 6)

**Title**:
734_PMID32860742.txt_CC.xml,
Words: 150,
Tokens: 282\
Tag data:
Total: 24,
Unique: 8,
Max tags: 2,
Tagged words: 22 (15%),
Avg tags: 1.09,
MC words: 0\
Link data:
Total: 9,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (8 (33.33%), 8 (5.33%))\
Avg links (tag, word): (1.12, 1.12),
Schema counts (B, I, E, S): (6, 7, 6, 5)

**Title**:
235_PMID32217665.txt_CC.xml,
Words: 166,
Tokens: 301\
Tag data:
Total: 16,
Unique: 7,
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
Schema counts (B, I, E, S): (4, 5, 4, 3)

**Title**:
573_PMID30515612.txt_CC.xml,
Words: 225,
Tokens: 381\
Tag data:
Total: 36,
Unique: 15,
Max tags: 2,
Tagged words: 34 (15%),
Avg tags: 1.06,
MC words: 0\
Link data:
Total: 42,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (20 (55.56%), 18 (8.0%))\
Avg links (tag, word): (2.1, 2.33),
Schema counts (B, I, E, S): (8, 9, 8, 11)

**Title**:
154_PMID32747363.txt_CC.xml,
Words: 249,
Tokens: 436\
Tag data:
Total: 28,
Unique: 10,
Max tags: 2,
Tagged words: 25 (10%),
Avg tags: 1.12,
MC words: 0\
Link data:
Total: 19,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (15 (53.57%), 12 (4.82%))\
Avg links (tag, word): (1.27, 1.58),
Schema counts (B, I, E, S): (9, 6, 9, 4)

**Title**:
226_PMID33303641.txt_CC.xml,
Words: 152,
Tokens: 276\
Tag data:
Total: 75,
Unique: 21,
Max tags: 4,
Tagged words: 57 (38%),
Avg tags: 1.32,
MC words: 0\
Link data:
Total: 60,
Unique: 8,
Max links (tag, word): (5, 5),
Linked (tags, words): (43 (57.33%), 32 (21.05%))\
Avg links (tag, word): (1.4, 1.88),
Schema counts (B, I, E, S): (17, 28, 17, 13)

**Title**:
9_PMID31441382.txt_CC.xml,
Words: 261,
Tokens: 607\
Tag data:
Total: 57,
Unique: 30,
Max tags: 2,
Tagged words: 55 (21%),
Avg tags: 1.04,
MC words: 0\
Link data:
Total: 48,
Unique: 8,
Max links (tag, word): (4, 4),
Linked (tags, words): (12 (21.05%), 12 (4.6%))\
Avg links (tag, word): (4.0, 4.0),
Schema counts (B, I, E, S): (19, 7, 19, 12)

**Title**:
149_PMD33093168.txt_CC.xml,
Words: 226,
Tokens: 399\
Tag data:
Total: 20,
Unique: 9,
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
Schema counts (B, I, E, S): (7, 4, 7, 2)

**Title**:
505_PMID32737652.txt_CC.xml,
Words: 156,
Tokens: 264\
Tag data:
Total: 11,
Unique: 6,
Max tags: 2,
Tagged words: 9 (6%),
Avg tags: 1.22,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (63.64%), 7 (4.49%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 1, 3, 4)

**Title**:
48_PMID31280658.txt_CC.xml,
Words: 155,
Tokens: 260\
Tag data:
Total: 12,
Unique: 3,
Max tags: 1,
Tagged words: 12 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 12,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (12 (100.0%), 12 (7.74%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 6, 3, 0)

**Title**:
257_PMID28465358.txt_CC.xml,
Words: 182,
Tokens: 332\
Tag data:
Total: 16,
Unique: 7,
Max tags: 1,
Tagged words: 16 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (37.5%), 6 (3.3%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 3, 4, 5)

**Title**:
738_PMID32619406.txt_CC.xml,
Words: 123,
Tokens: 251\
Tag data:
Total: 20,
Unique: 7,
Max tags: 1,
Tagged words: 20 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 22,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (18 (90.0%), 18 (14.63%))\
Avg links (tag, word): (1.22, 1.22),
Schema counts (B, I, E, S): (5, 8, 5, 2)

**Title**:
494_PMID30659235.txt_CC.xml,
Words: 222,
Tokens: 414\
Tag data:
Total: 41,
Unique: 14,
Max tags: 1,
Tagged words: 41 (18%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 12,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (12 (29.27%), 12 (5.41%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (11, 16, 11, 3)

**Title**:
372_PMID33130818.txt_CC.xml,
Words: 266,
Tokens: 537\
Tag data:
Total: 16,
Unique: 6,
Max tags: 1,
Tagged words: 16 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (43.75%), 7 (2.63%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 5, 4, 3)

**Title**:
127_PMID32651256.txt_CC.xml,
Words: 220,
Tokens: 365\
Tag data:
Total: 22,
Unique: 7,
Max tags: 2,
Tagged words: 19 (9%),
Avg tags: 1.16,
MC words: 0\
Link data:
Total: 40,
Unique: 4,
Max links (tag, word): (4, 4),
Linked (tags, words): (22 (100.0%), 19 (8.64%))\
Avg links (tag, word): (1.82, 2.11),
Schema counts (B, I, E, S): (5, 7, 5, 5)

**Title**:
18_PMID31931659.txt_CC.xml,
Words: 247,
Tokens: 534\
Tag data:
Total: 52,
Unique: 20,
Max tags: 2,
Tagged words: 50 (20%),
Avg tags: 1.04,
MC words: 0\
Link data:
Total: 29,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (22 (42.31%), 22 (8.91%))\
Avg links (tag, word): (1.32, 1.32),
Schema counts (B, I, E, S): (15, 14, 15, 8)

**Title**:
550_PMID31654241.txt_CC.xml,
Words: 293,
Tokens: 548\
Tag data:
Total: 55,
Unique: 18,
Max tags: 2,
Tagged words: 50 (17%),
Avg tags: 1.1,
MC words: 0\
Link data:
Total: 13,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (12 (21.82%), 12 (4.1%))\
Avg links (tag, word): (1.08, 1.08),
Schema counts (B, I, E, S): (10, 21, 10, 14)

**Title**:
77_PMID30806153.txt_CC.xml,
Words: 190,
Tokens: 422\
Tag data:
Total: 31,
Unique: 11,
Max tags: 2,
Tagged words: 29 (15%),
Avg tags: 1.07,
MC words: 0\
Link data:
Total: 15,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (10 (32.26%), 9 (4.74%))\
Avg links (tag, word): (1.5, 1.67),
Schema counts (B, I, E, S): (7, 11, 7, 6)

**Title**:
352_PMID33122623.txt_CC.xml,
Words: 262,
Tokens: 472\
Tag data:
Total: 52,
Unique: 19,
Max tags: 3,
Tagged words: 42 (16%),
Avg tags: 1.24,
MC words: 2\
Link data:
Total: 43,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (34 (65.38%), 29 (11.07%))\
Avg links (tag, word): (1.26, 1.48),
Schema counts (B, I, E, S): (17, 10, 17, 8)

**Title**:
539_PMID31473844.txt_CC.xml,
Words: 289,
Tokens: 553\
Tag data:
Total: 32,
Unique: 8,
Max tags: 2,
Tagged words: 30 (10%),
Avg tags: 1.07,
MC words: 0\
Link data:
Total: 40,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (31 (96.88%), 29 (10.03%))\
Avg links (tag, word): (1.29, 1.38),
Schema counts (B, I, E, S): (9, 12, 9, 2)

**Title**:
436_PMID30903103.txt_CC.xml,
Words: 260,
Tokens: 529\
Tag data:
Total: 32,
Unique: 8,
Max tags: 2,
Tagged words: 30 (12%),
Avg tags: 1.07,
MC words: 0\
Link data:
Total: 27,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (17 (53.12%), 15 (5.77%))\
Avg links (tag, word): (1.59, 1.8),
Schema counts (B, I, E, S): (7, 16, 7, 2)

**Title**:
442_PMID31209361.txt_CC.xml,
Words: 274,
Tokens: 594\
Tag data:
Total: 38,
Unique: 15,
Max tags: 2,
Tagged words: 37 (14%),
Avg tags: 1.03,
MC words: 0\
Link data:
Total: 21,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (17 (44.74%), 16 (5.84%))\
Avg links (tag, word): (1.24, 1.31),
Schema counts (B, I, E, S): (9, 8, 9, 12)

**Title**:
609_PMID32783918.txt_CC.xml,
Words: 157,
Tokens: 324\
Tag data:
Total: 13,
Unique: 5,
Max tags: 1,
Tagged words: 13 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (61.54%), 8 (5.1%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 5, 3, 2)

**Title**:
155_PMID33372040.txt_CC.xml,
Words: 222,
Tokens: 376\
Tag data:
Total: 40,
Unique: 10,
Max tags: 2,
Tagged words: 28 (13%),
Avg tags: 1.43,
MC words: 0\
Link data:
Total: 62,
Unique: 4,
Max links (tag, word): (4, 4),
Linked (tags, words): (26 (65.0%), 17 (7.66%))\
Avg links (tag, word): (2.38, 3.65),
Schema counts (B, I, E, S): (9, 17, 9, 5)

**Title**:
197_PMID32586982.txt_CC.xml,
Words: 235,
Tokens: 423\
Tag data:
Total: 39,
Unique: 11,
Max tags: 2,
Tagged words: 38 (16%),
Avg tags: 1.03,
MC words: 0\
Link data:
Total: 14,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (14 (35.9%), 14 (5.96%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (11, 16, 11, 1)

**Title**:
45_PMID30686098.txt_CC.xml,
Words: 238,
Tokens: 534\
Tag data:
Total: 18,
Unique: 8,
Max tags: 1,
Tagged words: 18 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (50.0%), 9 (3.78%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 4, 5, 4)

**Title**:
454_PMID32704090.txt_CC.xml,
Words: 324,
Tokens: 653\
Tag data:
Total: 12,
Unique: 5,
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
438_PMID31320749.txt_CC.xml,
Words: 274,
Tokens: 536\
Tag data:
Total: 60,
Unique: 20,
Max tags: 4,
Tagged words: 49 (18%),
Avg tags: 1.22,
MC words: 0\
Link data:
Total: 72,
Unique: 9,
Max links (tag, word): (4, 4),
Linked (tags, words): (42 (70.0%), 35 (12.77%))\
Avg links (tag, word): (1.71, 2.06),
Schema counts (B, I, E, S): (15, 13, 15, 17)

**Title**:
91_PMID31538542.txt_CC.xml,
Words: 232,
Tokens: 422\
Tag data:
Total: 17,
Unique: 9,
Max tags: 2,
Tagged words: 16 (7%),
Avg tags: 1.06,
MC words: 0\
Link data:
Total: 12,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (7 (41.18%), 7 (3.02%))\
Avg links (tag, word): (1.71, 1.71),
Schema counts (B, I, E, S): (5, 1, 5, 6)

**Title**:
316_PMID33009373.txt_1_CC.xml,
Words: 241,
Tokens: 449\
Tag data:
Total: 27,
Unique: 11,
Max tags: 2,
Tagged words: 26 (11%),
Avg tags: 1.04,
MC words: 0\
Link data:
Total: 28,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (14 (51.85%), 13 (5.39%))\
Avg links (tag, word): (2.0, 2.15),
Schema counts (B, I, E, S): (10, 4, 10, 3)

**Title**:
341_PMID33097685.txt_CC.xml,
Words: 225,
Tokens: 404\
Tag data:
Total: 28,
Unique: 11,
Max tags: 2,
Tagged words: 24 (11%),
Avg tags: 1.17,
MC words: 0\
Link data:
Total: 33,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (25 (89.29%), 21 (9.33%))\
Avg links (tag, word): (1.32, 1.57),
Schema counts (B, I, E, S): (10, 1, 10, 7)

**Title**:
262_PMID31488578.txt_CC.xml,
Words: 177,
Tokens: 312\
Tag data:
Total: 19,
Unique: 8,
Max tags: 1,
Tagged words: 19 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (42.11%), 8 (4.52%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 5, 5, 4)

**Title**:
329_PMID32895268.txt_CC.xml,
Words: 229,
Tokens: 496\
Tag data:
Total: 10,
Unique: 5,
Max tags: 2,
Tagged words: 9 (4%),
Avg tags: 1.11,
MC words: 0\
Link data:
Total: 12,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (8 (80.0%), 7 (3.06%))\
Avg links (tag, word): (1.5, 1.71),
Schema counts (B, I, E, S): (3, 0, 3, 4)

**Title**:
321_PMID33188176.txt_CC.xml,
Words: 179,
Tokens: 411\
Tag data:
Total: 21,
Unique: 8,
Max tags: 1,
Tagged words: 21 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (38.1%), 8 (4.47%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (8, 4, 8, 1)

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
470_PMID31332295.txt_CC.xml,
Words: 158,
Tokens: 259\
Tag data:
Total: 16,
Unique: 8,
Max tags: 1,
Tagged words: 16 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (50.0%), 8 (5.06%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 1, 5, 5)

**Title**:
38_PMID31679456.txt_CC.xml,
Words: 256,
Tokens: 486\
Tag data:
Total: 78,
Unique: 20,
Max tags: 2,
Tagged words: 73 (29%),
Avg tags: 1.07,
MC words: 0\
Link data:
Total: 41,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (23 (29.49%), 23 (8.98%))\
Avg links (tag, word): (1.78, 1.78),
Schema counts (B, I, E, S): (17, 38, 17, 6)

**Title**:
318_PMID32978367.txt_CC.xml,
Words: 232,
Tokens: 461\
Tag data:
Total: 28,
Unique: 10,
Max tags: 4,
Tagged words: 25 (11%),
Avg tags: 1.12,
MC words: 0\
Link data:
Total: 94,
Unique: 8,
Max links (tag, word): (8, 8),
Linked (tags, words): (21 (75.0%), 19 (8.19%))\
Avg links (tag, word): (4.48, 4.95),
Schema counts (B, I, E, S): (7, 8, 7, 6)

**Title**:
75_PMID31241013.txt_CC.xml,
Words: 131,
Tokens: 298\
Tag data:
Total: 18,
Unique: 4,
Max tags: 1,
Tagged words: 18 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 14,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (14 (77.78%), 14 (10.69%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 8, 3, 4)

**Title**:
640_PMID32783915.txt_CC.xml,
Words: 162,
Tokens: 273\
Tag data:
Total: 8,
Unique: 3,
Max tags: 1,
Tagged words: 8 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (100.0%), 8 (4.94%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (2, 3, 2, 1)

**Title**:
15_PMID32249716.txt_CC.xml,
Words: 240,
Tokens: 429\
Tag data:
Total: 31,
Unique: 14,
Max tags: 2,
Tagged words: 29 (12%),
Avg tags: 1.07,
MC words: 0\
Link data:
Total: 24,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (23 (74.19%), 21 (8.75%))\
Avg links (tag, word): (1.04, 1.14),
Schema counts (B, I, E, S): (8, 7, 8, 8)

**Title**:
64_PMID31775562.txt_CC.xml,
Words: 215,
Tokens: 424\
Tag data:
Total: 59,
Unique: 22,
Max tags: 4,
Tagged words: 51 (24%),
Avg tags: 1.16,
MC words: 0\
Link data:
Total: 28,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (22 (37.29%), 20 (9.3%))\
Avg links (tag, word): (1.27, 1.4),
Schema counts (B, I, E, S): (15, 13, 15, 16)

**Title**:
125_PMIDS32213542.txt_CC.xml,
Words: 217,
Tokens: 397\
Tag data:
Total: 18,
Unique: 8,
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
Schema counts (B, I, E, S): (7, 2, 7, 2)

**Title**:
355_PMID33184290.txt_CC.xml,
Words: 206,
Tokens: 343\
Tag data:
Total: 55,
Unique: 12,
Max tags: 2,
Tagged words: 44 (21%),
Avg tags: 1.25,
MC words: 0\
Link data:
Total: 30,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (17 (30.91%), 16 (7.77%))\
Avg links (tag, word): (1.76, 1.88),
Schema counts (B, I, E, S): (9, 30, 9, 7)

**Title**:
752_PMID31257072.txt_CC.xml,
Words: 136,
Tokens: 282\
Tag data:
Total: 17,
Unique: 5,
Max tags: 1,
Tagged words: 17 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (47.06%), 8 (5.88%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 6, 5, 1)

**Title**:
797_PMID29249692.txt_CC.xml,
Words: 126,
Tokens: 305\
Tag data:
Total: 18,
Unique: 10,
Max tags: 1,
Tagged words: 18 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (38.89%), 7 (5.56%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 2, 6, 4)

**Title**:
199_PMID32265225.txt_CC.xml,
Words: 290,
Tokens: 548\
Tag data:
Total: 31,
Unique: 10,
Max tags: 2,
Tagged words: 27 (9%),
Avg tags: 1.15,
MC words: 0\
Link data:
Total: 23,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (17 (54.84%), 13 (4.48%))\
Avg links (tag, word): (1.35, 1.77),
Schema counts (B, I, E, S): (11, 8, 11, 1)

**Title**:
34_PMID31286822.txt_CC.xml,
Words: 264,
Tokens: 535\
Tag data:
Total: 34,
Unique: 12,
Max tags: 2,
Tagged words: 33 (12%),
Avg tags: 1.03,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (23.53%), 8 (3.03%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (9, 12, 9, 4)

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
468_PMID31844253.txt_CC.xml,
Words: 282,
Tokens: 451\
Tag data:
Total: 27,
Unique: 10,
Max tags: 1,
Tagged words: 27 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 21,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (21 (77.78%), 21 (7.45%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 9, 7, 4)

**Title**:
276_PMID31879538.txt_CC.xml,
Words: 182,
Tokens: 322\
Tag data:
Total: 36,
Unique: 13,
Max tags: 2,
Tagged words: 35 (19%),
Avg tags: 1.03,
MC words: 0\
Link data:
Total: 21,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (15 (41.67%), 15 (8.24%))\
Avg links (tag, word): (1.4, 1.4),
Schema counts (B, I, E, S): (10, 8, 10, 8)

**Title**:
150_PMID32107212.txt_CC.xml,
Words: 150,
Tokens: 290\
Tag data:
Total: 15,
Unique: 3,
Max tags: 1,
Tagged words: 15 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 15,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (15 (100.0%), 15 (10.0%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (2, 10, 2, 1)

**Title**:
537_PMID29236199.txt_CC.xml,
Words: 243,
Tokens: 441\
Tag data:
Total: 18,
Unique: 6,
Max tags: 1,
Tagged words: 18 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 11,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (11 (61.11%), 11 (4.53%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 7, 4, 3)

**Title**:
407_PMID31114026.txt_CC.xml,
Words: 195,
Tokens: 351\
Tag data:
Total: 31,
Unique: 14,
Max tags: 2,
Tagged words: 30 (15%),
Avg tags: 1.03,
MC words: 1\
Link data:
Total: 15,
Unique: 2,
Max links (tag, word): (1, 2),
Linked (tags, words): (15 (48.39%), 14 (7.18%))\
Avg links (tag, word): (1.0, 1.07),
Schema counts (B, I, E, S): (11, 4, 11, 5)

**Title**:
430_PMID29317762.txt_CC.xml,
Words: 239,
Tokens: 438\
Tag data:
Total: 42,
Unique: 16,
Max tags: 2,
Tagged words: 41 (17%),
Avg tags: 1.02,
MC words: 0\
Link data:
Total: 55,
Unique: 7,
Max links (tag, word): (4, 4),
Linked (tags, words): (42 (100.0%), 41 (17.15%))\
Avg links (tag, word): (1.31, 1.34),
Schema counts (B, I, E, S): (14, 8, 14, 6)

**Title**:
536_PMID28856570.txt_CC.xml,
Words: 192,
Tokens: 283\
Tag data:
Total: 20,
Unique: 8,
Max tags: 1,
Tagged words: 20 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 17,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (17 (85.0%), 17 (8.85%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 7, 5, 3)

**Title**:
571_PMID31583496.txt_CC.xml,
Words: 213,
Tokens: 399\
Tag data:
Total: 53,
Unique: 20,
Max tags: 2,
Tagged words: 48 (23%),
Avg tags: 1.1,
MC words: 0\
Link data:
Total: 38,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (23 (43.4%), 23 (10.8%))\
Avg links (tag, word): (1.65, 1.65),
Schema counts (B, I, E, S): (19, 9, 19, 6)

**Title**:
562_PMID31641960.txt_CC.xml,
Words: 236,
Tokens: 456\
Tag data:
Total: 25,
Unique: 4,
Max tags: 1,
Tagged words: 25 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 17,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (17 (68.0%), 17 (7.2%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 17, 3, 2)

**Title**:
101_PMID32788173.txt_1_CC.xml,
Words: 177,
Tokens: 346\
Tag data:
Total: 21,
Unique: 7,
Max tags: 2,
Tagged words: 18 (10%),
Avg tags: 1.17,
MC words: 0\
Link data:
Total: 36,
Unique: 4,
Max links (tag, word): (4, 4),
Linked (tags, words): (15 (71.43%), 12 (6.78%))\
Avg links (tag, word): (2.4, 3.0),
Schema counts (B, I, E, S): (7, 3, 7, 4)

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
311_PMID33268765.txt_CC.xml,
Words: 223,
Tokens: 424\
Tag data:
Total: 60,
Unique: 19,
Max tags: 4,
Tagged words: 43 (19%),
Avg tags: 1.4,
MC words: 0\
Link data:
Total: 15,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (15 (25.0%), 15 (6.73%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (19, 14, 19, 8)

**Title**:
185_PMID32680921.txt_CC.xml,
Words: 160,
Tokens: 317\
Tag data:
Total: 27,
Unique: 6,
Max tags: 1,
Tagged words: 27 (17%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 27,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (27 (100.0%), 27 (16.88%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 14, 6, 1)

**Title**:
304_PMID32999283.txt_CC.xml,
Words: 160,
Tokens: 439\
Tag data:
Total: 33,
Unique: 14,
Max tags: 2,
Tagged words: 32 (20%),
Avg tags: 1.03,
MC words: 0\
Link data:
Total: 14,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (14 (42.42%), 14 (8.75%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (10, 4, 10, 9)

**Title**:
80_PMID31238825.txt_CC.xml,
Words: 210,
Tokens: 404\
Tag data:
Total: 21,
Unique: 10,
Max tags: 1,
Tagged words: 21 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (42.86%), 9 (4.29%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 4, 6, 5)

**Title**:
527_PMID31321634.txt_CC.xml,
Words: 211,
Tokens: 440\
Tag data:
Total: 60,
Unique: 20,
Max tags: 2,
Tagged words: 56 (27%),
Avg tags: 1.07,
MC words: 0\
Link data:
Total: 51,
Unique: 5,
Max links (tag, word): (2, 2),
Linked (tags, words): (43 (71.67%), 40 (18.96%))\
Avg links (tag, word): (1.19, 1.27),
Schema counts (B, I, E, S): (18, 19, 18, 5)

**Title**:
228_PMID28698299.txt_CC.xml,
Words: 229,
Tokens: 400\
Tag data:
Total: 34,
Unique: 12,
Max tags: 2,
Tagged words: 32 (14%),
Avg tags: 1.06,
MC words: 0\
Link data:
Total: 36,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (29 (85.29%), 27 (11.79%))\
Avg links (tag, word): (1.24, 1.33),
Schema counts (B, I, E, S): (9, 11, 9, 5)

**Title**:
263_PMID32381628.txt_CC.xml,
Words: 165,
Tokens: 286\
Tag data:
Total: 8,
Unique: 3,
Max tags: 1,
Tagged words: 8 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (100.0%), 8 (4.85%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (2, 2, 2, 2)

**Title**:
772_PMID32049046.txt_CC.xml,
Words: 131,
Tokens: 270\
Tag data:
Total: 7,
Unique: 3,
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
139_PMID32179514.txt_CC.xml,
Words: 211,
Tokens: 354\
Tag data:
Total: 31,
Unique: 12,
Max tags: 2,
Tagged words: 27 (13%),
Avg tags: 1.15,
MC words: 0\
Link data:
Total: 33,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (27 (87.1%), 25 (11.85%))\
Avg links (tag, word): (1.22, 1.32),
Schema counts (B, I, E, S): (10, 3, 10, 8)

**Title**:
490_PMID31740790.txt_CC.xml,
Words: 177,
Tokens: 343\
Tag data:
Total: 35,
Unique: 13,
Max tags: 3,
Tagged words: 28 (16%),
Avg tags: 1.25,
MC words: 0\
Link data:
Total: 24,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (20 (57.14%), 14 (7.91%))\
Avg links (tag, word): (1.2, 1.71),
Schema counts (B, I, E, S): (13, 1, 13, 8)

**Title**:
581_PMID32468177.txt_CC.xml,
Words: 231,
Tokens: 427\
Tag data:
Total: 30,
Unique: 12,
Max tags: 2,
Tagged words: 29 (13%),
Avg tags: 1.03,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (30.0%), 9 (3.9%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (8, 9, 8, 5)

**Title**:
419_PMID30850732.txt_CC.xml,
Words: 226,
Tokens: 401\
Tag data:
Total: 23,
Unique: 8,
Max tags: 1,
Tagged words: 23 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 29,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (17 (73.91%), 17 (7.52%))\
Avg links (tag, word): (1.71, 1.71),
Schema counts (B, I, E, S): (7, 6, 7, 3)

**Title**:
413_PMID33097833.txt_CC.xml,
Words: 236,
Tokens: 450\
Tag data:
Total: 26,
Unique: 8,
Max tags: 2,
Tagged words: 24 (10%),
Avg tags: 1.08,
MC words: 0\
Link data:
Total: 22,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (14 (53.85%), 12 (5.08%))\
Avg links (tag, word): (1.57, 1.83),
Schema counts (B, I, E, S): (8, 7, 8, 3)

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
43_PMID31204559.txt_CC.xml,
Words: 186,
Tokens: 320\
Tag data:
Total: 33,
Unique: 14,
Max tags: 1,
Tagged words: 33 (18%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 22,
Unique: 3,
Max links (tag, word): (1, 1),
Linked (tags, words): (22 (66.67%), 22 (11.83%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (11, 7, 11, 4)

**Title**:
748_PMID32243847.txt_CC.xml,
Words: 133,
Tokens: 281\
Tag data:
Total: 21,
Unique: 8,
Max tags: 1,
Tagged words: 21 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (38.1%), 8 (6.02%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 6, 7, 1)

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
405_PMID31804607.txt_CC.xml,
Words: 198,
Tokens: 422\
Tag data:
Total: 31,
Unique: 11,
Max tags: 2,
Tagged words: 27 (14%),
Avg tags: 1.15,
MC words: 0\
Link data:
Total: 12,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (10 (32.26%), 8 (4.04%))\
Avg links (tag, word): (1.2, 1.5),
Schema counts (B, I, E, S): (10, 7, 10, 4)

**Title**:
146_PMID32193285.txt_CC.xml,
Words: 215,
Tokens: 422\
Tag data:
Total: 45,
Unique: 11,
Max tags: 1,
Tagged words: 45 (21%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 20,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (20 (44.44%), 20 (9.3%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (11, 20, 11, 3)

**Title**:
161_PMID32816909.txt_CC.xml,
Words: 253,
Tokens: 488\
Tag data:
Total: 45,
Unique: 12,
Max tags: 1,
Tagged words: 45 (18%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 43,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (34 (75.56%), 34 (13.44%))\
Avg links (tag, word): (1.26, 1.26),
Schema counts (B, I, E, S): (10, 19, 10, 6)

**Title**:
568_PMID32405891.txt_CC.xml,
Words: 262,
Tokens: 469\
Tag data:
Total: 29,
Unique: 10,
Max tags: 1,
Tagged words: 29 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (20.69%), 6 (2.29%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 12, 7, 3)

**Title**:
779_PMID32109375.txt_CC.xml,
Words: 134,
Tokens: 271\
Tag data:
Total: 17,
Unique: 7,
Max tags: 2,
Tagged words: 16 (12%),
Avg tags: 1.06,
MC words: 0\
Link data:
Total: 20,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (12 (70.59%), 12 (8.96%))\
Avg links (tag, word): (1.67, 1.67),
Schema counts (B, I, E, S): (5, 3, 5, 4)

**Title**:
3_PMID31451060.txt_CC.xml,
Words: 210,
Tokens: 398\
Tag data:
Total: 31,
Unique: 15,
Max tags: 2,
Tagged words: 27 (13%),
Avg tags: 1.15,
MC words: 0\
Link data:
Total: 12,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (10 (32.26%), 10 (4.76%))\
Avg links (tag, word): (1.2, 1.2),
Schema counts (B, I, E, S): (8, 2, 8, 13)

**Title**:
799_PMID32589943.txt_CC.xml,
Words: 130,
Tokens: 240\
Tag data:
Total: 9,
Unique: 3,
Max tags: 1,
Tagged words: 9 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (100.0%), 9 (6.92%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (2, 4, 2, 1)

**Title**:
564_PMID30879166.txt_CC.xml,
Words: 235,
Tokens: 450\
Tag data:
Total: 36,
Unique: 9,
Max tags: 2,
Tagged words: 34 (14%),
Avg tags: 1.06,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (19.44%), 7 (2.98%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (8, 19, 8, 1)

**Title**:
489_PMID33277577.txt_CC.xml,
Words: 278,
Tokens: 528\
Tag data:
Total: 40,
Unique: 14,
Max tags: 2,
Tagged words: 35 (13%),
Avg tags: 1.14,
MC words: 0\
Link data:
Total: 23,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (18 (45.0%), 18 (6.47%))\
Avg links (tag, word): (1.28, 1.28),
Schema counts (B, I, E, S): (10, 11, 10, 9)

**Title**:
400_PMID33093470.txt_CC.xml,
Words: 301,
Tokens: 598\
Tag data:
Total: 18,
Unique: 9,
Max tags: 1,
Tagged words: 18 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 11,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (11 (61.11%), 11 (3.65%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 2, 5, 6)

**Title**:
164_PMID32019869.txt_CC.xml,
Words: 192,
Tokens: 302\
Tag data:
Total: 15,
Unique: 3,
Max tags: 1,
Tagged words: 15 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 15,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (15 (100.0%), 15 (7.81%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 9, 3, 0)

**Title**:
289_PMID30692206.txt_CC.xml,
Words: 174,
Tokens: 353\
Tag data:
Total: 22,
Unique: 8,
Max tags: 2,
Tagged words: 20 (11%),
Avg tags: 1.1,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (36.36%), 8 (4.6%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 5, 7, 3)

**Title**:
168_PMID32900774.txt_CC.xml,
Words: 218,
Tokens: 354\
Tag data:
Total: 42,
Unique: 13,
Max tags: 1,
Tagged words: 42 (19%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 28,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (23 (54.76%), 23 (10.55%))\
Avg links (tag, word): (1.22, 1.22),
Schema counts (B, I, E, S): (8, 19, 8, 7)

**Title**:
195_PMID32605998.txt_CC.xml,
Words: 205,
Tokens: 345\
Tag data:
Total: 17,
Unique: 7,
Max tags: 1,
Tagged words: 17 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 25,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (17 (100.0%), 17 (8.29%))\
Avg links (tag, word): (1.47, 1.47),
Schema counts (B, I, E, S): (6, 2, 6, 3)

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
140_PMID33239431.txt_CC.xml,
Words: 229,
Tokens: 431\
Tag data:
Total: 22,
Unique: 9,
Max tags: 1,
Tagged words: 22 (10%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 23,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (13 (59.09%), 13 (5.68%))\
Avg links (tag, word): (1.77, 1.77),
Schema counts (B, I, E, S): (9, 1, 9, 3)

**Title**:
32_PMID30290714.txt_CC.xml,
Words: 255,
Tokens: 462\
Tag data:
Total: 39,
Unique: 16,
Max tags: 2,
Tagged words: 37 (15%),
Avg tags: 1.05,
MC words: 0\
Link data:
Total: 35,
Unique: 5,
Max links (tag, word): (4, 4),
Linked (tags, words): (27 (69.23%), 25 (9.8%))\
Avg links (tag, word): (1.3, 1.4),
Schema counts (B, I, E, S): (15, 7, 15, 2)

**Title**:
589_PMID31177396.txt_CC.xml,
Words: 201,
Tokens: 336\
Tag data:
Total: 14,
Unique: 5,
Max tags: 1,
Tagged words: 14 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 10,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (10 (71.43%), 10 (4.98%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 2, 5, 2)

**Title**:
319_PMID33268783.txt_CC.xml,
Words: 207,
Tokens: 433\
Tag data:
Total: 29,
Unique: 9,
Max tags: 2,
Tagged words: 27 (13%),
Avg tags: 1.07,
MC words: 0\
Link data:
Total: 24,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (16 (55.17%), 14 (6.76%))\
Avg links (tag, word): (1.5, 1.71),
Schema counts (B, I, E, S): (9, 8, 9, 3)

**Title**:
737_PMID31526760.txt_CC.xml,
Words: 119,
Tokens: 228\
Tag data:
Total: 14,
Unique: 5,
Max tags: 1,
Tagged words: 14 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 10,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (10 (71.43%), 10 (8.4%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 3, 5, 1)

**Title**:
10_PMID30898012.txt_CC.xml,
Words: 239,
Tokens: 436\
Tag data:
Total: 27,
Unique: 9,
Max tags: 1,
Tagged words: 27 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 34,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (21 (77.78%), 21 (8.79%))\
Avg links (tag, word): (1.62, 1.62),
Schema counts (B, I, E, S): (5, 13, 5, 4)

**Title**:
425_PMID32814880.txt_CC.xml,
Words: 272,
Tokens: 507\
Tag data:
Total: 55,
Unique: 11,
Max tags: 1,
Tagged words: 55 (20%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 56,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (52 (94.55%), 52 (19.12%))\
Avg links (tag, word): (1.08, 1.08),
Schema counts (B, I, E, S): (10, 32, 10, 3)

**Title**:
478_PMID32764647.txt_CC.xml,
Words: 246,
Tokens: 443\
Tag data:
Total: 15,
Unique: 4,
Max tags: 1,
Tagged words: 15 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (46.67%), 7 (2.85%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 6, 4, 1)

**Title**:
35_PMID30894058.txt_CC.xml,
Words: 253,
Tokens: 543\
Tag data:
Total: 43,
Unique: 14,
Max tags: 1,
Tagged words: 43 (17%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 22,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (14 (32.56%), 14 (5.53%))\
Avg links (tag, word): (1.57, 1.57),
Schema counts (B, I, E, S): (12, 14, 12, 5)

**Title**:
68_PMID32186433.txt_CC.xml,
Words: 259,
Tokens: 536\
Tag data:
Total: 38,
Unique: 17,
Max tags: 2,
Tagged words: 33 (13%),
Avg tags: 1.15,
MC words: 0\
Link data:
Total: 34,
Unique: 4,
Max links (tag, word): (4, 4),
Linked (tags, words): (16 (42.11%), 12 (4.63%))\
Avg links (tag, word): (2.12, 2.83),
Schema counts (B, I, E, S): (9, 7, 9, 13)

**Title**:
448_PMID31024074.txt_CC.xml,
Words: 208,
Tokens: 406\
Tag data:
Total: 57,
Unique: 32,
Max tags: 2,
Tagged words: 53 (25%),
Avg tags: 1.08,
MC words: 0\
Link data:
Total: 42,
Unique: 6,
Max links (tag, word): (2, 4),
Linked (tags, words): (28 (49.12%), 25 (12.02%))\
Avg links (tag, word): (1.5, 1.68),
Schema counts (B, I, E, S): (14, 0, 14, 29)

**Title**:
486_PMID31802036.txt_CC.xml,
Words: 283,
Tokens: 489\
Tag data:
Total: 20,
Unique: 7,
Max tags: 2,
Tagged words: 18 (6%),
Avg tags: 1.11,
MC words: 0\
Link data:
Total: 24,
Unique: 3,
Max links (tag, word): (2, 3),
Linked (tags, words): (20 (100.0%), 18 (6.36%))\
Avg links (tag, word): (1.2, 1.33),
Schema counts (B, I, E, S): (6, 3, 6, 5)

**Title**:
384_PMID32968045.txt_CC.xml,
Words: 226,
Tokens: 366\
Tag data:
Total: 35,
Unique: 13,
Max tags: 3,
Tagged words: 31 (14%),
Avg tags: 1.13,
MC words: 0\
Link data:
Total: 17,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (14 (40.0%), 13 (5.75%))\
Avg links (tag, word): (1.21, 1.31),
Schema counts (B, I, E, S): (8, 5, 8, 14)

**Title**:
194_PMID32699135.txt_CC.xml,
Words: 196,
Tokens: 312\
Tag data:
Total: 7,
Unique: 3,
Max tags: 1,
Tagged words: 7 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (100.0%), 7 (3.57%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 0, 3, 1)

**Title**:
285_PMID29891559.txt_CC.xml,
Words: 188,
Tokens: 345\
Tag data:
Total: 39,
Unique: 13,
Max tags: 2,
Tagged words: 37 (20%),
Avg tags: 1.05,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (20.51%), 8 (4.26%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (15, 8, 15, 1)

**Title**:
162_PMID32737118.txt_CC.xml,
Words: 236,
Tokens: 412\
Tag data:
Total: 31,
Unique: 8,
Max tags: 2,
Tagged words: 27 (11%),
Avg tags: 1.15,
MC words: 0\
Link data:
Total: 32,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (20 (64.52%), 18 (7.63%))\
Avg links (tag, word): (1.6, 1.78),
Schema counts (B, I, E, S): (9, 6, 9, 7)

**Title**:
109_PMID32217697.txt_CC.xml,
Words: 213,
Tokens: 429\
Tag data:
Total: 18,
Unique: 6,
Max tags: 2,
Tagged words: 16 (8%),
Avg tags: 1.12,
MC words: 0\
Link data:
Total: 18,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (13 (72.22%), 11 (5.16%))\
Avg links (tag, word): (1.38, 1.64),
Schema counts (B, I, E, S): (6, 4, 6, 2)

**Title**:
66_PMID31512556.txt_CC.xml,
Words: 184,
Tokens: 404\
Tag data:
Total: 30,
Unique: 12,
Max tags: 1,
Tagged words: 30 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 30,
Unique: 4,
Max links (tag, word): (4, 4),
Linked (tags, words): (12 (40.0%), 12 (6.52%))\
Avg links (tag, word): (2.5, 2.5),
Schema counts (B, I, E, S): (11, 5, 11, 3)

**Title**:
531_PMID30610504.txt_CC.xml,
Words: 263,
Tokens: 517\
Tag data:
Total: 16,
Unique: 6,
Max tags: 1,
Tagged words: 16 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 16,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (16 (100.0%), 16 (6.08%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 4, 6, 0)

**Title**:
367_PMID33087696.txt_CC.xml,
Words: 261,
Tokens: 463\
Tag data:
Total: 24,
Unique: 13,
Max tags: 1,
Tagged words: 24 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (25.0%), 6 (2.3%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 4, 6, 8)

**Title**:
339_PMID33288741.txt_CC.xml,
Words: 157,
Tokens: 267\
Tag data:
Total: 6,
Unique: 3,
Max tags: 1,
Tagged words: 6 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (100.0%), 6 (3.82%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (2, 0, 2, 2)

**Title**:
484_PMID32346137.txt_CC.xml,
Words: 188,
Tokens: 387\
Tag data:
Total: 25,
Unique: 13,
Max tags: 1,
Tagged words: 25 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 17,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (17 (68.0%), 17 (9.04%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 5, 7, 6)

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
207_PMID31488580.txt_CC.xml,
Words: 109,
Tokens: 229\
Tag data:
Total: 25,
Unique: 9,
Max tags: 1,
Tagged words: 25 (23%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 16,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (16 (64.0%), 16 (14.68%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (8, 6, 8, 3)

**Title**:
54_PMID31373534.txt_CC.xml,
Words: 233,
Tokens: 448\
Tag data:
Total: 35,
Unique: 15,
Max tags: 1,
Tagged words: 35 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 23,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (20 (57.14%), 20 (8.58%))\
Avg links (tag, word): (1.15, 1.15),
Schema counts (B, I, E, S): (10, 9, 10, 6)

**Title**:
86_PMID31865844.txt_CC.xml,
Words: 182,
Tokens: 290\
Tag data:
Total: 19,
Unique: 5,
Max tags: 2,
Tagged words: 18 (10%),
Avg tags: 1.06,
MC words: 0\
Link data:
Total: 24,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (15 (78.95%), 14 (7.69%))\
Avg links (tag, word): (1.6, 1.71),
Schema counts (B, I, E, S): (5, 5, 5, 4)

**Title**:
141_PMID32046982.txt_CC.xml,
Words: 238,
Tokens: 360\
Tag data:
Total: 21,
Unique: 5,
Max tags: 1,
Tagged words: 21 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 21,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (15 (71.43%), 15 (6.3%))\
Avg links (tag, word): (1.4, 1.4),
Schema counts (B, I, E, S): (5, 11, 5, 0)

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
598_PMID25218423.txt_CC.xml,
Words: 220,
Tokens: 456\
Tag data:
Total: 28,
Unique: 14,
Max tags: 1,
Tagged words: 28 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 12,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (12 (42.86%), 12 (5.45%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (9, 1, 9, 9)

**Title**:
115_PMID32661137.txt_CC.xml,
Words: 222,
Tokens: 375\
Tag data:
Total: 78,
Unique: 15,
Max tags: 2,
Tagged words: 71 (32%),
Avg tags: 1.1,
MC words: 0\
Link data:
Total: 73,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (49 (62.82%), 42 (18.92%))\
Avg links (tag, word): (1.49, 1.74),
Schema counts (B, I, E, S): (17, 41, 17, 3)

**Title**:
456_PMID30683914.txt_CC.xml,
Words: 173,
Tokens: 323\
Tag data:
Total: 35,
Unique: 13,
Max tags: 2,
Tagged words: 33 (19%),
Avg tags: 1.06,
MC words: 0\
Link data:
Total: 29,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (23 (65.71%), 21 (12.14%))\
Avg links (tag, word): (1.26, 1.38),
Schema counts (B, I, E, S): (10, 11, 10, 4)

**Title**:
189_PMID32094301.txt_CC.xml,
Words: 251,
Tokens: 462\
Tag data:
Total: 53,
Unique: 9,
Max tags: 1,
Tagged words: 53 (21%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 62,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (40 (75.47%), 40 (15.94%))\
Avg links (tag, word): (1.55, 1.55),
Schema counts (B, I, E, S): (9, 34, 9, 1)

**Title**:
100_PMID31462126.txt_CC.xml,
Words: 141,
Tokens: 277\
Tag data:
Total: 35,
Unique: 13,
Max tags: 2,
Tagged words: 34 (24%),
Avg tags: 1.03,
MC words: 0\
Link data:
Total: 22,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (17 (48.57%), 16 (11.35%))\
Avg links (tag, word): (1.29, 1.38),
Schema counts (B, I, E, S): (10, 8, 10, 7)

**Title**:
310_PMID32934217.txt_CC.xml,
Words: 262,
Tokens: 452\
Tag data:
Total: 35,
Unique: 15,
Max tags: 1,
Tagged words: 35 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 15,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (15 (42.86%), 15 (5.73%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (12, 6, 12, 5)

**Title**:
421_PMID30341421.txt_CC.xml,
Words: 211,
Tokens: 382\
Tag data:
Total: 18,
Unique: 5,
Max tags: 1,
Tagged words: 18 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 14,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (14 (77.78%), 14 (6.64%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 8, 3, 4)

**Title**:
269_PMID32561546.txt_CC.xml,
Words: 145,
Tokens: 207\
Tag data:
Total: 13,
Unique: 4,
Max tags: 1,
Tagged words: 13 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 19,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (13 (100.0%), 13 (8.97%))\
Avg links (tag, word): (1.46, 1.46),
Schema counts (B, I, E, S): (4, 5, 4, 0)

**Title**:
174_PMID33239430.txt_CC.xml,
Words: 131,
Tokens: 226\
Tag data:
Total: 24,
Unique: 5,
Max tags: 1,
Tagged words: 24 (18%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 11,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (11 (45.83%), 11 (8.4%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 12, 5, 2)

**Title**:
244_PMID31727771.txt_CC.xml,
Words: 215,
Tokens: 433\
Tag data:
Total: 64,
Unique: 10,
Max tags: 2,
Tagged words: 41 (19%),
Avg tags: 1.56,
MC words: 0\
Link data:
Total: 58,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (31 (48.44%), 30 (13.95%))\
Avg links (tag, word): (1.87, 1.93),
Schema counts (B, I, E, S): (8, 37, 8, 11)

**Title**:
728_PMID32183950.txt_CC.xml,
Words: 126,
Tokens: 274\
Tag data:
Total: 47,
Unique: 16,
Max tags: 2,
Tagged words: 46 (37%),
Avg tags: 1.02,
MC words: 0\
Link data:
Total: 23,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (17 (36.17%), 17 (13.49%))\
Avg links (tag, word): (1.35, 1.35),
Schema counts (B, I, E, S): (13, 16, 13, 5)

**Title**:
392_PMID33060569.txt_CC.xml,
Words: 212,
Tokens: 420\
Tag data:
Total: 54,
Unique: 20,
Max tags: 6,
Tagged words: 36 (17%),
Avg tags: 1.5,
MC words: 0\
Link data:
Total: 25,
Unique: 4,
Max links (tag, word): (3, 3),
Linked (tags, words): (19 (35.19%), 13 (6.13%))\
Avg links (tag, word): (1.32, 1.92),
Schema counts (B, I, E, S): (15, 4, 15, 20)

**Title**:
704_PMID32531268.txt_CC.xml,
Words: 125,
Tokens: 225\
Tag data:
Total: 17,
Unique: 6,
Max tags: 2,
Tagged words: 15 (12%),
Avg tags: 1.13,
MC words: 0\
Link data:
Total: 18,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (13 (76.47%), 11 (8.8%))\
Avg links (tag, word): (1.38, 1.64),
Schema counts (B, I, E, S): (6, 3, 6, 2)

**Title**:
44_PMID31818185.txt_CC.xml,
Words: 249,
Tokens: 455\
Tag data:
Total: 35,
Unique: 13,
Max tags: 2,
Tagged words: 33 (13%),
Avg tags: 1.06,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (17.14%), 6 (2.41%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (12, 9, 12, 2)

**Title**:
332_PMID33100331.txt_CC.xml,
Words: 166,
Tokens: 348\
Tag data:
Total: 10,
Unique: 5,
Max tags: 1,
Tagged words: 10 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (70.0%), 7 (4.22%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 1, 4, 1)

**Title**:
267_PMID32675324.txt_CC.xml,
Words: 203,
Tokens: 352\
Tag data:
Total: 33,
Unique: 8,
Max tags: 1,
Tagged words: 33 (16%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 16,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (16 (48.48%), 16 (7.88%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 19, 6, 2)

**Title**:
434_PMID33208891.txt_CC.xml,
Words: 302,
Tokens: 515\
Tag data:
Total: 27,
Unique: 11,
Max tags: 2,
Tagged words: 24 (8%),
Avg tags: 1.12,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (18.52%), 5 (1.66%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (8, 6, 8, 5)

**Title**:
7_PMID31679460.txt_CC.xml,
Words: 255,
Tokens: 598\
Tag data:
Total: 69,
Unique: 31,
Max tags: 2,
Tagged words: 66 (26%),
Avg tags: 1.05,
MC words: 2\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (10.14%), 7 (2.75%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (22, 9, 22, 16)

**Title**:
417_PMID31320750.txt_CC.xml,
Words: 273,
Tokens: 487\
Tag data:
Total: 35,
Unique: 14,
Max tags: 2,
Tagged words: 32 (12%),
Avg tags: 1.09,
MC words: 0\
Link data:
Total: 26,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (21 (60.0%), 18 (6.59%))\
Avg links (tag, word): (1.24, 1.44),
Schema counts (B, I, E, S): (11, 5, 11, 8)

**Title**:
463_PMID31511651.txt_CC.xml,
Words: 202,
Tokens: 370\
Tag data:
Total: 32,
Unique: 13,
Max tags: 2,
Tagged words: 30 (15%),
Avg tags: 1.07,
MC words: 0\
Link data:
Total: 27,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (18 (56.25%), 16 (7.92%))\
Avg links (tag, word): (1.5, 1.69),
Schema counts (B, I, E, S): (9, 6, 9, 8)

**Title**:
458_PMID32999468.txt_CC.xml,
Words: 253,
Tokens: 527\
Tag data:
Total: 51,
Unique: 20,
Max tags: 1,
Tagged words: 51 (20%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 25,
Unique: 3,
Max links (tag, word): (1, 1),
Linked (tags, words): (25 (49.02%), 25 (9.88%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (9, 17, 9, 16)

**Title**:
549_PMID32564202.txt_CC.xml,
Words: 248,
Tokens: 506\
Tag data:
Total: 19,
Unique: 11,
Max tags: 1,
Tagged words: 19 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 20,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (13 (68.42%), 13 (5.24%))\
Avg links (tag, word): (1.54, 1.54),
Schema counts (B, I, E, S): (4, 3, 4, 8)

**Title**:
98_PMID31432739.txt_CC.xml,
Words: 229,
Tokens: 481\
Tag data:
Total: 18,
Unique: 6,
Max tags: 1,
Tagged words: 18 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 11,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (11 (61.11%), 11 (4.8%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 4, 6, 2)

**Title**:
312_PMID33012781.txt_CC.xml,
Words: 268,
Tokens: 504\
Tag data:
Total: 38,
Unique: 18,
Max tags: 2,
Tagged words: 35 (13%),
Avg tags: 1.09,
MC words: 0\
Link data:
Total: 49,
Unique: 7,
Max links (tag, word): (2, 2),
Linked (tags, words): (34 (89.47%), 31 (11.57%))\
Avg links (tag, word): (1.44, 1.58),
Schema counts (B, I, E, S): (12, 4, 12, 10)

**Title**:
112_PMID33051252.txt_CC.xml,
Words: 238,
Tokens: 414\
Tag data:
Total: 30,
Unique: 13,
Max tags: 3,
Tagged words: 27 (11%),
Avg tags: 1.11,
MC words: 0\
Link data:
Total: 70,
Unique: 9,
Max links (tag, word): (6, 6),
Linked (tags, words): (26 (86.67%), 24 (10.08%))\
Avg links (tag, word): (2.69, 2.92),
Schema counts (B, I, E, S): (8, 5, 8, 9)

**Title**:
592_PMID30426280.txt_CC.xml,
Words: 148,
Tokens: 243\
Tag data:
Total: 13,
Unique: 4,
Max tags: 2,
Tagged words: 12 (8%),
Avg tags: 1.08,
MC words: 0\
Link data:
Total: 20,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (13 (100.0%), 12 (8.11%))\
Avg links (tag, word): (1.54, 1.67),
Schema counts (B, I, E, S): (3, 5, 3, 2)

**Title**:
390_PMID33082333.txt_CC.xml,
Words: 191,
Tokens: 343\
Tag data:
Total: 36,
Unique: 10,
Max tags: 2,
Tagged words: 32 (17%),
Avg tags: 1.12,
MC words: 0\
Link data:
Total: 13,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (13 (36.11%), 13 (6.81%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (10, 13, 10, 3)

**Title**:
22_PMID30909785.txt_CC.xml,
Words: 250,
Tokens: 391\
Tag data:
Total: 9,
Unique: 4,
Max tags: 1,
Tagged words: 9 (4%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (55.56%), 5 (2.0%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 2, 3, 1)

**Title**:
19_PMID31177901.txt_CC.xml,
Words: 232,
Tokens: 453\
Tag data:
Total: 25,
Unique: 8,
Max tags: 1,
Tagged words: 25 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 28,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (16 (64.0%), 16 (6.9%))\
Avg links (tag, word): (1.75, 1.75),
Schema counts (B, I, E, S): (6, 9, 6, 4)

**Title**:
360_PMID33257688.txt_CC.xml,
Words: 199,
Tokens: 387\
Tag data:
Total: 85,
Unique: 28,
Max tags: 4,
Tagged words: 78 (39%),
Avg tags: 1.09,
MC words: 0\
Link data:
Total: 143,
Unique: 14,
Max links (tag, word): (10, 10),
Linked (tags, words): (63 (74.12%), 57 (28.64%))\
Avg links (tag, word): (2.27, 2.51),
Schema counts (B, I, E, S): (21, 25, 21, 18)

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
266_PMID32912902.txt_CC.xml,
Words: 214,
Tokens: 348\
Tag data:
Total: 29,
Unique: 8,
Max tags: 2,
Tagged words: 25 (12%),
Avg tags: 1.16,
MC words: 0\
Link data:
Total: 10,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (10 (34.48%), 10 (4.67%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (9, 10, 9, 1)

**Title**:
120_PMID32122909.txt_CC.xml,
Words: 288,
Tokens: 599\
Tag data:
Total: 25,
Unique: 9,
Max tags: 2,
Tagged words: 23 (8%),
Avg tags: 1.09,
MC words: 0\
Link data:
Total: 27,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (21 (84.0%), 19 (6.6%))\
Avg links (tag, word): (1.29, 1.42),
Schema counts (B, I, E, S): (7, 6, 7, 5)

**Title**:
423_PMID32203171.txt_CC.xml,
Words: 180,
Tokens: 256\
Tag data:
Total: 13,
Unique: 6,
Max tags: 1,
Tagged words: 13 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (46.15%), 6 (3.33%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 1, 5, 2)

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

**Title**:
399_PMID33203836.txt_CC.xml,
Words: 198,
Tokens: 311\
Tag data:
Total: 30,
Unique: 15,
Max tags: 2,
Tagged words: 29 (15%),
Avg tags: 1.03,
MC words: 0\
Link data:
Total: 16,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (11 (36.67%), 11 (5.56%))\
Avg links (tag, word): (1.45, 1.45),
Schema counts (B, I, E, S): (8, 4, 8, 10)

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
119_PMID33023950.txt_CC.xml,
Words: 231,
Tokens: 417\
Tag data:
Total: 58,
Unique: 18,
Max tags: 2,
Tagged words: 56 (24%),
Avg tags: 1.04,
MC words: 0\
Link data:
Total: 71,
Unique: 6,
Max links (tag, word): (3, 3),
Linked (tags, words): (47 (81.03%), 45 (19.48%))\
Avg links (tag, word): (1.51, 1.58),
Schema counts (B, I, E, S): (14, 22, 14, 8)

**Title**:
81_PMID30654731.txt_CC.xml,
Words: 208,
Tokens: 355\
Tag data:
Total: 31,
Unique: 15,
Max tags: 1,
Tagged words: 31 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 48,
Unique: 6,
Max links (tag, word): (6, 6),
Linked (tags, words): (17 (54.84%), 17 (8.17%))\
Avg links (tag, word): (2.82, 2.82),
Schema counts (B, I, E, S): (7, 6, 7, 11)

**Title**:
31_PMID31066324.txt_CC.xml,
Words: 260,
Tokens: 487\
Tag data:
Total: 38,
Unique: 12,
Max tags: 1,
Tagged words: 38 (15%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (13.16%), 5 (1.92%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (12, 13, 12, 1)

**Title**:
591_PMID32901335.txt_CC.xml,
Words: 145,
Tokens: 265\
Tag data:
Total: 31,
Unique: 9,
Max tags: 2,
Tagged words: 26 (18%),
Avg tags: 1.19,
MC words: 0\
Link data:
Total: 69,
Unique: 6,
Max links (tag, word): (6, 6),
Linked (tags, words): (21 (67.74%), 16 (11.03%))\
Avg links (tag, word): (3.29, 4.31),
Schema counts (B, I, E, S): (6, 14, 6, 5)

**Title**:
481_PMID31570854.txt_CC.xml,
Words: 195,
Tokens: 382\
Tag data:
Total: 12,
Unique: 5,
Max tags: 1,
Tagged words: 12 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 16,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (10 (83.33%), 10 (5.13%))\
Avg links (tag, word): (1.6, 1.6),
Schema counts (B, I, E, S): (5, 2, 5, 0)

**Title**:
586_PMID31342239.txt_CC.xml,
Words: 209,
Tokens: 397\
Tag data:
Total: 25,
Unique: 10,
Max tags: 2,
Tagged words: 24 (11%),
Avg tags: 1.04,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (24.0%), 6 (2.87%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 5, 6, 8)

**Title**:
143_PMID330223944.txt_CC.xml,
Words: 183,
Tokens: 300\
Tag data:
Total: 9,
Unique: 3,
Max tags: 1,
Tagged words: 9 (5%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (100.0%), 9 (4.92%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 3, 3, 0)

**Title**:
479_PMID31659279.txt_CC.xml,
Words: 250,
Tokens: 471\
Tag data:
Total: 28,
Unique: 12,
Max tags: 2,
Tagged words: 27 (11%),
Avg tags: 1.04,
MC words: 0\
Link data:
Total: 38,
Unique: 4,
Max links (tag, word): (4, 4),
Linked (tags, words): (15 (53.57%), 14 (5.6%))\
Avg links (tag, word): (2.53, 2.71),
Schema counts (B, I, E, S): (6, 7, 6, 9)

**Title**:
181_PMID32179512.txt_CC.xml,
Words: 227,
Tokens: 393\
Tag data:
Total: 29,
Unique: 9,
Max tags: 1,
Tagged words: 29 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (20.69%), 6 (2.64%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 13, 7, 2)

**Title**:
354_PMID33159047.txt_CC.xml,
Words: 296,
Tokens: 539\
Tag data:
Total: 50,
Unique: 14,
Max tags: 1,
Tagged words: 50 (17%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 38,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (26 (52.0%), 26 (8.78%))\
Avg links (tag, word): (1.46, 1.46),
Schema counts (B, I, E, S): (13, 21, 13, 3)

**Title**:
575_PMID28879567.txt_CC.xml,
Words: 196,
Tokens: 452\
Tag data:
Total: 27,
Unique: 13,
Max tags: 1,
Tagged words: 27 (14%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (33.33%), 9 (4.59%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 4, 4, 15)

**Title**:
504_PMID31175486.txt_CC.xml,
Words: 260,
Tokens: 568\
Tag data:
Total: 39,
Unique: 13,
Max tags: 2,
Tagged words: 38 (15%),
Avg tags: 1.03,
MC words: 0\
Link data:
Total: 13,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (13 (33.33%), 13 (5.0%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (10, 14, 10, 5)

**Title**:
497_PMID33398092.txt_CC.xml,
Words: 211,
Tokens: 402\
Tag data:
Total: 27,
Unique: 14,
Max tags: 1,
Tagged words: 27 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 3,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (3 (11.11%), 3 (1.42%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 7, 5, 10)

**Title**:
97_PMID32403970.txt_CC.xml,
Words: 210,
Tokens: 397\
Tag data:
Total: 42,
Unique: 16,
Max tags: 2,
Tagged words: 35 (17%),
Avg tags: 1.2,
MC words: 0\
Link data:
Total: 17,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (16 (38.1%), 10 (4.76%))\
Avg links (tag, word): (1.06, 1.7),
Schema counts (B, I, E, S): (9, 12, 9, 12)

**Title**:
600_PMID26467923.txt_CC.xml,
Words: 283,
Tokens: 504\
Tag data:
Total: 38,
Unique: 14,
Max tags: 1,
Tagged words: 38 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (23.68%), 9 (3.18%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (13, 10, 13, 2)

**Title**:
33_PMID31223056.txt_CC.xml,
Words: 250,
Tokens: 515\
Tag data:
Total: 28,
Unique: 10,
Max tags: 1,
Tagged words: 28 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 13,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (13 (46.43%), 13 (5.2%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (9, 9, 9, 1)

**Title**:
751_PMID30205049.txt_CC.xml,
Words: 128,
Tokens: 236\
Tag data:
Total: 15,
Unique: 7,
Max tags: 1,
Tagged words: 15 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 6,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (6 (40.0%), 6 (4.69%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 1, 6, 2)

**Title**:
718_PMID31185212.txt_CC.xml,
Words: 137,
Tokens: 285\
Tag data:
Total: 17,
Unique: 6,
Max tags: 1,
Tagged words: 17 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 7,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (7 (41.18%), 7 (5.11%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 6, 5, 1)

**Title**:
491_PMID31101885.txt_CC.xml,
Words: 155,
Tokens: 248\
Tag data:
Total: 58,
Unique: 13,
Max tags: 2,
Tagged words: 53 (34%),
Avg tags: 1.09,
MC words: 0\
Link data:
Total: 33,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (24 (41.38%), 21 (13.55%))\
Avg links (tag, word): (1.38, 1.57),
Schema counts (B, I, E, S): (14, 29, 14, 1)

**Title**:
124_PMID32665355.txt_CC.xml,
Words: 235,
Tokens: 437\
Tag data:
Total: 47,
Unique: 16,
Max tags: 2,
Tagged words: 44 (19%),
Avg tags: 1.07,
MC words: 0\
Link data:
Total: 32,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (30 (63.83%), 27 (11.49%))\
Avg links (tag, word): (1.07, 1.19),
Schema counts (B, I, E, S): (11, 15, 11, 10)

**Title**:
72_PMID31238788.txt_CC.xml,
Words: 178,
Tokens: 368\
Tag data:
Total: 40,
Unique: 15,
Max tags: 1,
Tagged words: 40 (22%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 37,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (30 (75.0%), 30 (16.85%))\
Avg links (tag, word): (1.23, 1.23),
Schema counts (B, I, E, S): (13, 8, 13, 6)

**Title**:
331_PMID33040078.txt_CC.xml,
Words: 304,
Tokens: 546\
Tag data:
Total: 58,
Unique: 20,
Max tags: 3,
Tagged words: 55 (18%),
Avg tags: 1.05,
MC words: 0\
Link data:
Total: 87,
Unique: 10,
Max links (tag, word): (6, 6),
Linked (tags, words): (31 (53.45%), 28 (9.21%))\
Avg links (tag, word): (2.81, 3.11),
Schema counts (B, I, E, S): (15, 18, 15, 10)

**Title**:
396_PMID33257682.txt_CC.xml,
Words: 264,
Tokens: 436\
Tag data:
Total: 16,
Unique: 7,
Max tags: 1,
Tagged words: 16 (6%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (5 (31.25%), 5 (1.89%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (4, 4, 4, 4)

**Title**:
165_PMID32303578.txt_CC.xml,
Words: 269,
Tokens: 484\
Tag data:
Total: 27,
Unique: 11,
Max tags: 2,
Tagged words: 25 (9%),
Avg tags: 1.08,
MC words: 0\
Link data:
Total: 23,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (19 (70.37%), 17 (6.32%))\
Avg links (tag, word): (1.21, 1.35),
Schema counts (B, I, E, S): (11, 2, 11, 3)

**Title**:
325_PMID33303756.txt_CC.xml,
Words: 266,
Tokens: 485\
Tag data:
Total: 27,
Unique: 10,
Max tags: 2,
Tagged words: 24 (9%),
Avg tags: 1.12,
MC words: 0\
Link data:
Total: 16,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (12 (44.44%), 9 (3.38%))\
Avg links (tag, word): (1.33, 1.78),
Schema counts (B, I, E, S): (7, 8, 7, 5)

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
5_PMID30870073.txt_CC.xml,
Words: 242,
Tokens: 491\
Tag data:
Total: 29,
Unique: 11,
Max tags: 1,
Tagged words: 29 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 11,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (8 (27.59%), 8 (3.31%))\
Avg links (tag, word): (1.38, 1.38),
Schema counts (B, I, E, S): (9, 9, 9, 2)

**Title**:
142_PMID33277366.txt_CC.xml,
Words: 185,
Tokens: 326\
Tag data:
Total: 9,
Unique: 4,
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
16_PMID31232177.txt_CC.xml,
Words: 210,
Tokens: 420\
Tag data:
Total: 39,
Unique: 13,
Max tags: 3,
Tagged words: 37 (18%),
Avg tags: 1.05,
MC words: 0\
Link data:
Total: 38,
Unique: 5,
Max links (tag, word): (4, 4),
Linked (tags, words): (26 (66.67%), 24 (11.43%))\
Avg links (tag, word): (1.46, 1.58),
Schema counts (B, I, E, S): (8, 15, 8, 8)

**Title**:
178_PMID32999000.txt_CC.xml,
Words: 228,
Tokens: 404\
Tag data:
Total: 18,
Unique: 6,
Max tags: 2,
Tagged words: 16 (7%),
Avg tags: 1.12,
MC words: 0\
Link data:
Total: 20,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (14 (77.78%), 12 (5.26%))\
Avg links (tag, word): (1.43, 1.67),
Schema counts (B, I, E, S): (7, 3, 7, 1)

**Title**:
391_PMID32943609.txt_CC.xml,
Words: 225,
Tokens: 413\
Tag data:
Total: 15,
Unique: 6,
Max tags: 1,
Tagged words: 15 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (60.0%), 9 (4.0%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 2, 5, 3)

**Title**:
53_PMID30774023.txt_CC.xml,
Words: 207,
Tokens: 400\
Tag data:
Total: 28,
Unique: 13,
Max tags: 2,
Tagged words: 26 (13%),
Avg tags: 1.08,
MC words: 0\
Link data:
Total: 15,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (12 (42.86%), 10 (4.83%))\
Avg links (tag, word): (1.25, 1.5),
Schema counts (B, I, E, S): (8, 5, 8, 7)

**Title**:
87_PMID32160082.txt_CC.xml,
Words: 258,
Tokens: 538\
Tag data:
Total: 70,
Unique: 26,
Max tags: 2,
Tagged words: 66 (26%),
Avg tags: 1.06,
MC words: 0\
Link data:
Total: 26,
Unique: 3,
Max links (tag, word): (2, 2),
Linked (tags, words): (19 (27.14%), 19 (7.36%))\
Avg links (tag, word): (1.37, 1.37),
Schema counts (B, I, E, S): (15, 26, 15, 14)

**Title**:
59_PMID31876243.txt_CC.xml,
Words: 201,
Tokens: 313\
Tag data:
Total: 27,
Unique: 10,
Max tags: 1,
Tagged words: 27 (13%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 12,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (12 (44.44%), 12 (5.97%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 11, 6, 3)

**Title**:
323_PMID32913185.txt_CC.xml,
Words: 186,
Tokens: 323\
Tag data:
Total: 22,
Unique: 8,
Max tags: 1,
Tagged words: 22 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 16,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (16 (72.73%), 16 (8.6%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 4, 7, 4)

**Title**:
725_PMID31679823.txt_CC.xml,
Words: 123,
Tokens: 233\
Tag data:
Total: 10,
Unique: 4,
Max tags: 1,
Tagged words: 10 (8%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 17,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (10 (100.0%), 10 (8.13%))\
Avg links (tag, word): (1.7, 1.7),
Schema counts (B, I, E, S): (3, 2, 3, 2)

**Title**:
706_PMID31935369.txt_CC.xml,
Words: 127,
Tokens: 255\
Tag data:
Total: 9,
Unique: 3,
Max tags: 1,
Tagged words: 9 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (100.0%), 9 (7.09%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (3, 2, 3, 1)

**Title**:
147_PMID31941699.txt_CC.xml,
Words: 180,
Tokens: 295\
Tag data:
Total: 26,
Unique: 8,
Max tags: 2,
Tagged words: 23 (13%),
Avg tags: 1.13,
MC words: 0\
Link data:
Total: 15,
Unique: 2,
Max links (tag, word): (2, 2),
Linked (tags, words): (10 (38.46%), 10 (5.56%))\
Avg links (tag, word): (1.5, 1.5),
Schema counts (B, I, E, S): (8, 7, 8, 3)

**Title**:
623_PMID33242418.txt_CC.xml,
Words: 156,
Tokens: 243\
Tag data:
Total: 31,
Unique: 11,
Max tags: 1,
Tagged words: 31 (20%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 29,
Unique: 3,
Max links (tag, word): (1, 1),
Linked (tags, words): (29 (93.55%), 29 (18.59%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 13, 7, 4)

**Title**:
444_PMID32231246.txt_CC.xml,
Words: 237,
Tokens: 447\
Tag data:
Total: 27,
Unique: 13,
Max tags: 1,
Tagged words: 27 (11%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 17,
Unique: 3,
Max links (tag, word): (3, 3),
Linked (tags, words): (12 (44.44%), 12 (5.06%))\
Avg links (tag, word): (1.42, 1.42),
Schema counts (B, I, E, S): (5, 7, 5, 10)

**Title**:
596_PMID26456506.txt_CC.xml,
Words: 262,
Tokens: 578\
Tag data:
Total: 80,
Unique: 25,
Max tags: 2,
Tagged words: 70 (27%),
Avg tags: 1.14,
MC words: 0\
Link data:
Total: 47,
Unique: 7,
Max links (tag, word): (2, 2),
Linked (tags, words): (38 (47.5%), 38 (14.5%))\
Avg links (tag, word): (1.24, 1.24),
Schema counts (B, I, E, S): (18, 29, 18, 15)

**Title**:
132_PMID32366477.txt_CC.xml,
Words: 183,
Tokens: 314\
Tag data:
Total: 36,
Unique: 10,
Max tags: 1,
Tagged words: 36 (20%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 23,
Unique: 2,
Max links (tag, word): (1, 1),
Linked (tags, words): (23 (63.89%), 23 (12.57%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (9, 14, 9, 4)

**Title**:
597_PMID30680481.txt_CC.xml,
Words: 255,
Tokens: 524\
Tag data:
Total: 18,
Unique: 7,
Max tags: 1,
Tagged words: 18 (7%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 10,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (10 (55.56%), 10 (3.92%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 3, 6, 3)

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
499_PMID30478383.txt_CC.xml,
Words: 270,
Tokens: 536\
Tag data:
Total: 43,
Unique: 20,
Max tags: 2,
Tagged words: 40 (15%),
Avg tags: 1.07,
MC words: 0\
Link data:
Total: 28,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (22 (51.16%), 21 (7.78%))\
Avg links (tag, word): (1.27, 1.33),
Schema counts (B, I, E, S): (11, 8, 11, 13)

**Title**:
203_PMID31831627.txt_CC.xml,
Words: 201,
Tokens: 349\
Tag data:
Total: 27,
Unique: 11,
Max tags: 2,
Tagged words: 25 (12%),
Avg tags: 1.08,
MC words: 0\
Link data:
Total: 50,
Unique: 6,
Max links (tag, word): (6, 6),
Linked (tags, words): (17 (62.96%), 15 (7.46%))\
Avg links (tag, word): (2.94, 3.33),
Schema counts (B, I, E, S): (11, 4, 11, 1)

**Title**:
67_PMID30661440.txt_CC.xml,
Words: 225,
Tokens: 409\
Tag data:
Total: 27,
Unique: 9,
Max tags: 1,
Tagged words: 27 (12%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (33.33%), 9 (4.0%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (7, 8, 7, 5)

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
50_PMID31868081.txt_CC.xml,
Words: 255,
Tokens: 457\
Tag data:
Total: 25,
Unique: 6,
Max tags: 2,
Tagged words: 19 (7%),
Avg tags: 1.32,
MC words: 0\
Link data:
Total: 56,
Unique: 4,
Max links (tag, word): (4, 4),
Linked (tags, words): (23 (92.0%), 17 (6.67%))\
Avg links (tag, word): (2.43, 3.29),
Schema counts (B, I, E, S): (8, 9, 8, 0)

**Title**:
36_PMID30653446.txt_CC.xml,
Words: 260,
Tokens: 548\
Tag data:
Total: 44,
Unique: 14,
Max tags: 2,
Tagged words: 43 (17%),
Avg tags: 1.02,
MC words: 1\
Link data:
Total: 5,
Unique: 1,
Max links (tag, word): (1, 2),
Linked (tags, words): (5 (11.36%), 4 (1.54%))\
Avg links (tag, word): (1.0, 1.25),
Schema counts (B, I, E, S): (14, 15, 14, 1)

**Title**:
335_PMID32980857.txt_CC.xml,
Words: 305,
Tokens: 588\
Tag data:
Total: 27,
Unique: 13,
Max tags: 1,
Tagged words: 27 (9%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 10,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (10 (37.04%), 10 (3.28%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (5, 7, 5, 10)

**Title**:
102_PMID32054768.txt_CC.xml,
Words: 234,
Tokens: 429\
Tag data:
Total: 48,
Unique: 16,
Max tags: 1,
Tagged words: 48 (21%),
Avg tags: 1.0,
MC words: 0\
Link data:
Total: 42,
Unique: 4,
Max links (tag, word): (2, 2),
Linked (tags, words): (34 (70.83%), 34 (14.53%))\
Avg links (tag, word): (1.24, 1.24),
Schema counts (B, I, E, S): (14, 17, 14, 3)

**Title**:
485_PMID32001780.txt_CC.xml,
Words: 236,
Tokens: 406\
Tag data:
Total: 45,
Unique: 17,
Max tags: 2,
Tagged words: 41 (17%),
Avg tags: 1.1,
MC words: 0\
Link data:
Total: 9,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (9 (20.0%), 9 (3.81%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (14, 11, 14, 6)

**Title**:
70_PMID31448672.txt_CC.xml,
Words: 179,
Tokens: 365\
Tag data:
Total: 34,
Unique: 9,
Max tags: 2,
Tagged words: 28 (16%),
Avg tags: 1.21,
MC words: 0\
Link data:
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (23.53%), 8 (4.47%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (10, 12, 10, 2)

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
462_PMID31767934.txt_CC.xml,
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
Total: 8,
Unique: 1,
Max links (tag, word): (1, 1),
Linked (tags, words): (8 (44.44%), 8 (4.47%))\
Avg links (tag, word): (1.0, 1.0),
Schema counts (B, I, E, S): (6, 4, 6, 2)

**Title**:
365_PMID33110058.txt_CC.xml,
Words: 187,
Tokens: 297\
Tag data:
Total: 26,
Unique: 9,
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
Schema counts (B, I, E, S): (8, 8, 8, 2)

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


