#!/bin/sh

. ~/user_venv/bin/activate
python3 -u main.py -f configs/verification -v > outputs/log.txt 2>&1

