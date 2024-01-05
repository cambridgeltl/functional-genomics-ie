#!/bin/sh

conda activate tfm_nlp
python3 -u main.py -f configs/verification -v > outputs/log.txt 2>&1

