---
geometry: margin=2.5cm
---

# Transformer Natural Language Processing (NLP) | Functional Genomics


## Overview

Data and python code to train transformer based models for natural language processing, in particular named entity recognition (NER) and entity linking (EL) for functional genomics papers.


## Usage

To use the code to retrain models on updated datasets, follow the guidance in quick usage.
Other sections have details about specific operations.
Don't forget to check the help pages for main.py and any of the programs in the tools folder.


### Important Notes

Commands given assume you are using python 3, if you have python 2 and 3 installed run all python programs using 'python3' not 'python'.
Scripts use 'python3' for compatability.
Shell scripts assume you have a properly configured virtual environment at ~/user_venv.
If you dont, run **sh create_venv.sh**.


### Quick usage

* To re-run the best models on new available V2 data (and also analyse it) run **sh retrain_new_data.sh**.
It may take a while for models to train, use ctrl+z to suspend the process and then use command 'bg' to let the models train in the background.
* Note - converting the rough analysis markdown files to pdfs is done with pandoc so without it this step will fail
* The shell script will log model training to **outputs/log.txt** unbuffered so you can check this file periodically to see progress.
* Once trained, data about the models and their training are stored in **outputs/outputs_db.json**.
* Make a copy of the templates **link_full_analysis.json** and **tagging_full_analysis.json** that are found in the **configs/templates** folder.
* Take the names of the models found in **outputs/outputs_db.json** and put them in list keyed by "MODELS".
* Put the linking ones in the link copy and the tagging ones in the tag copy.
Optionally, change the save folders / output paths in the configs to avoid overwritting.
* Run the config files with **python3 main.py config_path1 config_path2**.
The config paths should point to the configs you made when you copied the templates.
* Use your markdown viewer / image viewer of choice to review the graphs and files generated.
Default folder for these is **model_analysis**.


### Preparing Data

There are various programs in the tools folder that allow you to create and manipulate json databases for the model.
Tools can be used manually, however 2 shell scripts are given to automate this for the functional genomics task.
**regen_fgen_data.sh** will create a number of json databases from the given folders in raw_data, including test and train databases for the NER task.
**analyse_fgen_data.sh** will run rough_analyser on these databases and then create pdfs detailing statistics of the data.
For manual use, run 'python tools/some_program.py -h' for more information on that particular program.


### Running Models

Models are run using main.py.
To run a model create a config file (see below) and then pass the path to this file as an argument to main.py. E.g. 'python main.py my_config'.
You can also give it multiple configs and folders of configs, see main.py -h for more information.
Various shell scripts are given that will run files in the respective folders in configs/.


### Analysing runs

See quick usage, more will be added here later.


### Trouble shooting

* If you get errors relating to packages, make sure you are in a properly configured virtual environment or if runnning things manually that you have the correct packages installed
* The data agreement tool still has hardcoded tag categories (currently setup for v2) so make sure to alter them (or generalise like the other programs) if the tag scheme changes


## Other information

### Head names

For tagging, head names must be the name of a field that is also given in the tag categories file given in the configuration file.

For linking there are several possible head names, each with different effects.
See src/dataloading.py for the code.
Apologies if this is confusing, only the first two given (link_only and link_same_tag_only) are probably relevant and useful.
The rest are for interest only.
link_only will use and try and predict links as they are given by the MAE software.
Essentially it tries to predict if 2 tokens have the same link id.
link_same_tag_only will try and predict if 2 tokens are part of the same tag.
This is only useful when a schema (e.g. BIO) is not being used.
link_all will do both of the above and will not distinguish between the two types of linking.
link_same_tag_and_link will combine the first 2 like link_all but will instead have 2 different labels for the two different types of link.
This is directly equivalent to a transformer with link_only and link_same_tag_only heads, though it combines things when reporting f1 scores which may not be very helpful.
link_same_tag_and_link_split is a special kind of linker that instead of learning on all possible links for all tagged items (like the other linkers), it only considers links between same_tags of the same actual tag value.
This is smarter than the normal same_tag_only but the lack of negative training data probably makes it worse.
It is possible to train things using link_same_tag_only but at deploy time only consider things of the same tag value but this has not been implemented yet on the deploy side of things.


### Multi GPU / not using cuda:0

By default the method which returns the cuda device (found in src/misc) will return cuda:0.
This is then saved on the model and in the heads as obj.cuda_device.
When creating new tensors in the code you can use this to make sure they are put on the right device.
Theoretically you should be able to modify the method ins src/misc to return cuda:1 to put everything on the second gpu.
However there seems to be an issue with the transformer from hugging face being initialised on cuda:0.
If you can find a way to initialise the transformer onto the same device as the model itself, running on any gpu is possible.
This should then be a config argument to alter which gpu the model runs on.

DataParallel is pytorch method often used to train models over multiple gpus.
This hasn't been used since it's not possible with batch size 1.
Whilst larger batch sizes would work with it, model run time seems to be the only factor affecting performance when batch size and number of epochs are concerned.
In essence, the ratio of epochs to batch size is all that matters so using DataParallel to allow for bigger batch size is pointless.

There are some untested models (see configs/more_vram_needed) that are too large for the 12GB GPUs on the server.
These are the 'large' transformer models.
If access to more VRAM was obtained then it would be a high priority to test these models as they may give improvements.
Just make sure the configs in that folder are up to date in terms of what is best for all there other parameters.


## To Do

### High Priority

* Analysis of latest models on v2 data
* Crf head
    * Find a way to speed up
    * Find a way to balance losses
        * Pushing / pulling the logits should work, logic for it is done however it needs to be coded in a way that will preserve tensor gradients and also be efficient
    * Train on bs1 for 36 epochs
* Improve code documentation and information in README
    * Configs
* Variance for k-folding
    * In analysis based on special config parameter
    * Or generate after training with tool to calc for existing db entries

### Medium Priotity

* Make data_agreement tool use a tag categories definition file rather than hardcoding
* Combined accuracy of joint prediction
    * Predict tags with one model and then links with other
    * How to measure this joint accuracy?
* fgen deploy
    * Multi model deploy method that can decide on tags and then link them (using 2 models)
        * Some sort of continuous tag detection that groups output for those words (could be done via explicit methods or using link predictions)
    * Add link prediction to deploy method
* Fully support multi-input to transformer heads
    * Test multi input heads
* Linking improvements
    * [CLS] Token link predictions
    * Entity start and entity end markers for BIO entities for linking
    * Need ability to have many inputs for transformer input so each tag pair can be tested
* Per label prf1a
    * Support for this in analyse

### Low Priotity

* Training and testing of different architectures
    * Different dropout
    * Different nonlin head setups
        * Head keyword argument that specifies full non-linear classifier architecture
* No category head & cp2l for more epochs as result is inconclusive
* Code clean / refactoring
    * Move dataloading and misc stuff into either classes, util or combined file
    * Copious type annotations
    * abc abstract classing?
    * Public / privating in model.py
    * Type conditions in construction of main things (i.e. tell linter what's a head or model)
* Use end of text when over 512 tokens
* Write data format explanations
* Rough analysis of sentence lengths
* Ability to specify set colours in analysis config
* Multi-model framework extension
* Add tag links to data agreement
* Model checkpointing
* Unit testing


## Config File

Note this section is currently unfinished.
Refer to existing configs for examples.
Be careful of older configs which may be setup differently, when in doubt trust the newer one.

### Notes:

If a key is not marked as (ar) or (o) then it only needs to be present if it is in the refs of another value in the parent dict

refs -> required extra fields

ar -> always required

o -> Optional

### Config options:

* MODE (ar)
    * train, refs: MODEL, DATA, TRAINING
    * test, refs: MODEL, DATA, TESTING
    * deploy, refs: MODEL, DATA, DEPLOY
    * analyse, refs: HISTORY_DATA, ANALYSIS

* MODEL
    * TYPE (ar)
        * pretrained, refs: TRANSFORMER_MODEL, HEADS, MAX_TOKEN_LENGTH, TAG_CATEGORY_DEFINITIONS
        * existing, refs: PATH
    * TRANSFORMER_MODEL: Transformer to use, called via AutoModel
    * TRANSFORMER_KWARGS (o): Dict containing kwargs for the automodel call
    * HEADS: Dict containing data on heads for the model, keys are the head names and values are dicts of args for that head, keys for those dicts are given below. Head names may need to be matched to things in TAG_CATEGORY_DEFINITIONS or in dataloading.
        * htype (ar): The head class to use e.g. single_label, multi_label or link
        * num_labels (ar): Number of labels head will need to predict for
        * schema (o): Schema to use, E.g. 'BIO'
    * TOKENIZER_MODEL (o): Tokenizer to use, called via AutoTokenizer, defaults to TRANSFORMER_MODEL
    * TOKENIZER_KWARGS (o): Dict containing kwargs for the autotokenizer call
    * TAG_LIST_DEFINITIONS (o): Path to a file contained definitions of tag lists for the heads, helps when data does not contain them all
    * TAG_CATEGORY_DEFINITIONS: Path to file containing data on tag categories to be used by dataloading to know what to look for. These files are also used by the maexml_to_json_data tool
    * MAX_TOKEN_LENGTH: Max token length of any input, usually 512 for big input tasks
    * PATH: Path to transformer file (.pkl), file extension is not needed

* DATA (TEST_DATA)
    * PATH (ar): Path to file with data on it
    * FILETYPE (ar): Currently only json_fgeom is supported
    * BATCH_SIZE (ar): Batch size for model inputs
    * BALANCE_CLASSES (ar): 0 means no balancing of losses, 1 means full balancing (i.e. if a label in single_label or positive value in multi_label occours half as often compared to the average / negative value then scale losses for this label by 2), in between values mix between these

* TRAINING
    * TRAINED_NAME (ar): Name to give trained model when saving it
    * OPTIMIZER_CLASS (ar): Class for the optimiser, currently only AdamW supported
    * OPTIMIZER_KWARGS (ar): Dict of kwargs for optimiser call, putting lr and eps is recommended
    * EPOCHS (ar): Number of epochs to run for
    * FULL_FINETUNING (o): Default True, whether to tune the transformer as well as the classifier
    * MAX_GRAD_NORM (o): For clipping gradients norms, default is 1
    * VERBOSE (o): Verbosity level, 0-3, default is 1
        * 0: Don't print any training info
        * 1: Print epoch numbers
        * 2: Print epoch loss / accuracy and time left
        * 3: Print batch numbers and when calculating accuracy
    * K_FOLDS (o): If present will use this number of folds in k-fold cross validation, validation scores are averaged across all folds and train losses are given from the final train across the whole dataset

* TESTING: Currently no args but its presence is required for testing or post train testing

