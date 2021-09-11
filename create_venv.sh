#!/bin/sh

python3 -m venv ~/user_venv
. ~/user_venv/bin/activate
pip install -r requirements.txt
deactivate

