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

* Average words: 203.5
* Maximum words: 291
* Minimum words: 128\
* Average tokens: 386.5
* Maximum tokens: 591
* Minimum tokens: 233\
* Entries with over 512 tokens: 7/59, 11.86%


## Tags

### Maximums

* Total tags: 55
* Unique tags: 17
* Max tags: 4
* Tagged words: 44
* Tagged words %: 21.36%
* Avg tags: 1.25
* MC words: 0

### Averages

* Total tags: 19.41
* Unique tags: 7.12
* Max tags: 1.36
* Tagged words: 18.61
* Tagged words %: 9.37%
* Avg tags: 1.03
* MC words: 0.0


## Links

### Maximums

* Total links: 94
* Unique links: 8
* Max links per tag, word: 8, 8
* Linked tags, words: 27, 27
* Linked % tags, words: 100.0%, 16.88%
* Avg links per tag, word: 4.48, 4.95

### Averages

* Total links: 8.63
* Unique links: 0.92
* Max links per tag, word: 0.71, 0.73
* Linked tags, words: 5.93, 5.64
* Linked % tags, words: 24.86%, 2.81%
* Avg links per tag, word: 0.54, 0.56


## Schema

* Maximums (B, I, E, S): 14, 30, 14, 11
* Averages (B, I, E, S): 5.37, 5.47, 5.37, 3.19


## Labels

* Label: Total, Maximum per entry, Average per entry

### Categories

* Perturbing_Action: 385, 34, 6.53
* Context: 814, 46, 13.8
* Effect: 706, 44, 11.97

### Description

* Knock Out: 72, 12, 1.22
* Conditional Knock Out: 33, 11, 0.56
* Knock In: 4, 4, 0.07
* Conditional Knock In: 0, 0, 0.0
* Knock Down: 18, 6, 0.31
* Plasmid Vector: 0, 0, 0.0
* Viral Vector: 0, 0, 0.0
* Pharmacological Inhibition: 61, 10, 1.03
* Decreased Expression Level: 45, 10, 0.76
* Increased Expression Level: 58, 9, 0.98
* Other: 94, 21, 1.59

### Experiment_Type

* Organism: 76, 11, 1.29
* Tumour: 37, 9, 0.63
* Cells: 167, 21, 2.83
* Cell Line: 10, 4, 0.17
* Transformed Cell Line: 76, 11, 1.29
* Primary Culture: 11, 5, 0.19
* Organoid Culture: 7, 7, 0.12
* Cell Transplantation: 0, 0, 0.0
* Xenotransplantation: 21, 7, 0.36
* Other: 0, 0, 0.0
* Not Stated: 2, 2, 0.03

### Species

* Human: 15, 5, 0.25
* Mouse: 67, 14, 1.14
* Rat: 0, 0, 0.0
* Fish: 0, 0, 0.0
* Fly: 4, 4, 0.07
* Yeast: 2, 2, 0.03
* Bacterium: 0, 0, 0.0
* Other: 0, 0, 0.0
* Not Stated: 319, 21, 5.41

### Phenotype

* Adhesion: 0, 0, 0.0
* Apoptosis: 49, 9, 0.83
* Anoikis: 0, 0, 0.0
* Autophagy: 79, 22, 1.34
* Cell Cycle Arrest: 0, 0, 0.0
* Cell Death: 24, 8, 0.41
* Cell Growth: 17, 10, 0.29
* Cell Survival: 15, 6, 0.25
* Colony Formation: 3, 3, 0.05
* Differentiation: 12, 5, 0.2
* Entosis: 0, 0, 0.0
* Epithelial-Mesenchymal Transition: 8, 8, 0.14
* Ferroptosis: 27, 12, 0.46
* Invasion: 7, 3, 0.12
* Metastasis: 17, 5, 0.29
* Migration: 6, 2, 0.1
* Mitophagy: 0, 0, 0.0
* Necroptosis: 8, 4, 0.14
* Necrosis: 0, 0, 0.0
* Netosis: 0, 0, 0.0
* Oncosis: 0, 0, 0.0
* Proliferation: 34, 6, 0.58
* Pyroptosis: 0, 0, 0.0
* Quiescence: 0, 0, 0.0
* Self-Renewal: 2, 2, 0.03
* Senescence: 0, 0, 0.0
* Transformation: 0, 0, 0.0
* Tumour Growth: 35, 9, 0.59
* Tumourigenesis: 10, 8, 0.17

### Activity

* Causes: 96, 15, 1.63
* Inhibits: 57, 8, 0.97
* Increases: 84, 9, 1.42
* Decreases: 77, 9, 1.31
* Regulates: 15, 7, 0.25
* No Effect: 6, 6, 0.1
* Not Stated: 18, 4, 0.31


# Information on each entry

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


