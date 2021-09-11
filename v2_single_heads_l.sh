#!/bin/sh

. ~/user_venv/bin/activate
python3 -u main.py -f configs/v2_single_heads -v > outputs/log.txt 2>&1

