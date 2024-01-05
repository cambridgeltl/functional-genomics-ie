#!/bin/sh

conda activate tfm_nlp
python3 -u main.py -f configs/active -vr > outputs/log.txt 2>&1

