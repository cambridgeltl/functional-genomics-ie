#!/bin/sh

conda activate tfm_nlp
python3 -u main.py -f configs/v2_single_heads -v > outputs/log.txt 2>&1

