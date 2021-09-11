#!/bin/sh

. ~/user_venv/bin/activate
python3 -u main.py -f configs/active -vr > outputs/log.txt 2>&1

