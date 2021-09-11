#!/bin/sh

echo "Regenerating data from raw files"
sh regen_fgen_data.sh

echo "Analysing data"
sh analyse_fgen_data.sh

echo "Starting model training"
sh current_best_l.sh

