
# Functional Genomics NLP


## Overview

Data and python code to train transformer based models for named entity recognition and entity linking for functional genomics papers. `main.py` and other tools should have help pages, supply `-h` as a command line option to see these (e.g. `python foo.py -h`)


## Running Existing Models

To run an existing model, `path/to/model.pkl`, on a text file, `path/to/text.txt`, do the following:

1. Copy one of the relevant configuration files in `configs/deploy`, saving it to e.g. `my/new/config.json`
2. Edit it, setting `MODEL -> PATH` to `path/to/model.pkl` and `DATA -> PATH` to `path/to/text.txt` (`MODEL -> EXTRA_PATHS` may also need altering if performing both tagging and linking)
3. Run the config via `python main.py my/new/config.json`


## General Usage


### Scripts

The shell scripts provided give shortcut commands to using the codebase as well as examples of usage, they should be executed from the top level folder.
They assume you have a properly configured virtual environment at ~/user_venv, if you dont, run `create_venv.sh`.
`retrain_new_data.sh` and its child scripts `regen_fgen_data.sh`, `analyse_fgen_data.sh`, `current_best_l.sh`, provide an example pipeline of data processing, analysis, and model training.
`analyse_fgen_data.sh` requires pandoc to be installed.
Scripts ending in `_l`, e.g. `current_best_l.sh`, will redirect stdout and stderr to `outputs/log.txt` unbuffered for ease of background execution and monitering.
Once trained, data about the models and their training are typically stored in `outputs/outputs_db.json`.


### Data Preparation

There are various programs in the tools folder that allow you to create and manipulate json databases for the model.
See their help pages for more specific information.


### Data Format

Example data for the models to be trained on is given in `json_data/v2_marked_and_linked.json` and similar files.
It consists of a dictionary keyed by abstract names.
The values in the dictionary are lists of all word datums in that abstract.
Words are defined as a contiguous block of non-whitespace characters.
Each word datum has at least the following fields:

* `WORD`: The characters of that word.
* `TOKENS`: The tokens resulting from that word from the given tokenizer, each to be fed into the transformer based model.
* `SENTENCE`: Which (0-indexed) sentence in the abstract this word occours in.
* `POS`: Which (0-indexed) character in the abstract this word starts at.

It then additionally has fields for each tag category.
These fields contain lists of tag data for tags belonging to that category.
Each tag datum has at least the following fields:

* `id`: The id of the tag this datum belongs to, as tags can spread across many contiguous words
* `link_ids`: A list of link id's.
Tag datums which share link ids are considered to be linked.
* `schema`: Beggining/Inner/End/Singular (BIES) schema indicator.
This indicates where this word sits in the tagged span of words with this tag.
Models can be trained using simpler schemas, such as BIO, which can be easily derived from this.

Addtionally each tag datum then has another key-value entry where the key is the tag sub-category (often the same as the tag category), and the value is the label of the tag.


### Running Models

Models are run using main.py.
To run a model create a config file (see below) and then pass this files path as an argument to main.py. E.g. `python3 main.py my_config.json`.
You can also give it multiple configs and folders of configs, see `main.py`'s help page for more information, or scripts for example usage.


### Analysing Training Run Metrics

This has not been automated yet, an example workflow is given instead:

* Make a copy of the templates `link_full_analysis.json` and `tagging_full_analysis.json` that are found in the `configs/templates` folder.
* Take the names of the models found in `outputs/outputs_db.json` and put them in list keyed by `MODELS`.
* Put the linking ones in the link copy and the tagging ones in the tag copy.
Optionally, change the save folders / output paths in the configs to avoid overwritting.
* Run the config files with `python3 main.py config_path1 config_path2`.
The config paths should point to the configs made when copying the templates.
* Open markdown/image viewer of choice to review the graphs and files generated.
Default folder for these is `model_analysis`.


### Troubleshooting

* For errors relating to packages, make sure virtual environment is properly configured or correct packages are installed.
* The data agreement tool still has hardcoded tag categories (currently setup for v2) so make sure to alter them (or generalise like the other programs) for different tag schemes.


## Other information

### Head names

For tagging, head names must be the name of a field that is also given in the tag categories file.
This file is used in the `MODEL` -> `TAG_CATEGORY_DEFINITIONS` field, and the `-c` option of `tools/rough_analyser.py`.
For examples see `tag_categories.json` and `tag_categories_v2.json`.

For linking there are several possible head names, each with different effects.
See `src/dataloading.py` for the code.
`link_only` is the most relevant and useful, others are mainly provided for interest.

* `link_only` will use and try and predict links as they are given by the MAE software.
Essentially it tries to predict if 2 tokens have the same link id.
* `link_same_tag_only` will try and predict if 2 tokens are part of the same tag.
This is only useful when a schema (e.g. BIO) is not being used.
* `link_same_tag_and_link` will do both `link_only` and `link_same_tag_only`, with 2 different labels for the two different types of link.
This is directly equivalent to a transformer with link_only and link_same_tag_only heads, though it combines metrics such as f1 scores.
* `link_all` will do both `link_only` and `link_same_tag_only`, and will not distinguish between the two types of linking at all.
* `link_same_tag_and_link_split` is a special kind of linker that instead of learning on all possible links for all tagged items (like the other linkers), it only considers links between tags of the same actual tag value.
This is smarter than the normal `link_same_tag_only` but lack of negative training data can lead to worse performance.
It should be possible to train things using `link_same_tag_only` but at deploy time use this, but this has not been implemented yet on the deploy side of things.


### GPU Notes

By default the method which returns the cuda device (found in `src/misc`) will return `cuda:0`.
This is then saved on the model and in the heads as `obj.cuda_device`.
When creating new tensors in the code you can use this to make sure they are put on the right device.
Theoretically you should be able to modify the method in `src/misc` to return `cuda:1` to put everything on the second gpu.
However there seems to be an issue with the transformer from hugging face being always initialised on `cuda:0`.
Modification of the code to initialise the transformer onto the same device as the model itself would allow running on any gpu.
Support for a config argument to alter which gpu the model runs on should then be added.


## Config File

Refer to existing configs for examples.
Be careful of older configs which may be setup differently, when in doubt trust newer ones.
The ones in `configs/current_best` are most up to date.

### Notes:

If a key is not marked as always required (AR) or optional (Opt) then it only needs to be present if it is in the required extra fields (REFs) of another value in the parent dict.
This specification is incomplete, when in doubt check examples or code.

### Config options:

* MODE (AR)
    * train REFs: MODEL, DATA, TRAINING
    * test REFs: MODEL, DATA, TESTING
    * deploy REFs: MODEL, DATA, DEPLOY
    * analyse REFs: HISTORY_DATA, ANALYSIS

* VERBOSE (Opt): Global verbosity that overwrites verboseness in rest of config (0-3, default 1)

* MODEL
    * TYPE (AR)
        * pretrained REFs: TRANSFORMER_MODEL, HEADS, MAX_TOKEN_LENGTH, TAG_CATEGORY_DEFINITIONS
        * existing REFs: PATH
    * TRANSFORMER_MODEL: Transformer to use, called via AutoModel
    * TRANSFORMER_KWARGS (Opt): Dict containing kwargs for the automodel call
    * HEADS: Dict containing data on heads for the model, keys are the head names and values are dicts of args for that head, keys for those dicts are given below. Head names may need to be matched to things in TAG_CATEGORY_DEFINITIONS or in dataloading.
        * htype (AR): The head class to use e.g. single_label, multi_label or link
        * num_labels (AR): Number of labels head will need to predict for
        * schema (Opt): Schema to use, E.g. 'BIO'
    * TOKENIZER_MODEL (Opt): Tokenizer to use, called via AutoTokenizer, defaults to TRANSFORMER_MODEL
    * TOKENIZER_KWARGS (Opt): Dict containing kwargs for the autotokenizer call
    * TAG_LIST_DEFINITIONS (Opt): Path to a file contained definitions of tag lists for the heads, helps when data does not contain them all
    * TAG_CATEGORY_DEFINITIONS: Path to file containing data on tag categories to be used by dataloading to know what to look for. These files are also used by the maexml_to_json_data tool
    * MAX_TOKEN_LENGTH: Max token length of any input, usually 512 for big input tasks
    * PATH: Path to transformer file (.pkl), file extension is not needed
    * EXTRA_PATHS: Dictionary of paths to other transformer files. Needed for linking, in this case key should be `link`.

* DATA
    * PATH (AR): Path to file with data on it
    * FILETYPE (AR): Currently only `json_fgeom` is supported for training, `txt` is also supported for deploy
    * BATCH_SIZE (AR): Batch size for model inputs
    * BALANCE_CLASSES (AR): 0 means no balancing of losses, 1 means full balancing (i.e. if a label in single_label or positive value in multi_label occours half as often compared to the average / negative value then scale losses for this label by 2), in between values mix between these

* TEST DATA: See DATA

* TRAINING
    * TRAINED_NAME (AR): Name to give trained model when saving it
    * OPTIMIZER_CLASS (AR): Class for the optimiser, currently only AdamW supported
    * OPTIMIZER_KWARGS (AR): Dict of kwargs for optimiser call, putting lr and eps is recommended
    * EPOCHS (AR): Number of epochs to run for
    * FULL_FINETUNING (Opt): Default True, whether to tune the transformer as well as the classifier
    * MAX_GRAD_NORM (Opt): For clipping gradients norms, default is 1
    * VERBOSE (Opt): Verbosity level, 0-3, default is 1
        * 0: Don't print any training info
        * 1: Print epoch numbers
        * 2: Print epoch loss / accuracy and time left
        * 3: Print batch numbers and when calculating accuracy
    * K_FOLDS (Opt): If present will use this number of folds in k-fold cross validation, validation scores are averaged across all folds and train losses are given from the final train across the whole dataset

* TESTING: Currently no args but its presence is required for testing or post train testing

* DEPLOY
    * OUTPUT (AR): Output mode, `print` or `txt`, latter saves to a file and requires PATH field
    * PATH (Opt): Needed if OUTPUT is `txt`, file path to save to
    * LINK (Opt): Whether a linking model is present (requires EXTRA_PATHS entry in MODEL)

