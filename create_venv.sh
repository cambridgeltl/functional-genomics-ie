#!/bin/sh

python3 -m venv ~/user_venv
conda activate tfm_nlp
pip install -r requirements.txt
deactivate

