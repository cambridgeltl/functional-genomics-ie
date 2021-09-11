#!/bin/sh

. ~/user_venv/bin/activate
python3 -u main.py -f configs/current_best -v > outputs/log.txt 2>&1

