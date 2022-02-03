#!/bin/bash

source ~/.bashrc
source setup.sh

export RICHGEOAL=/work/clas12/users/costantini/RICH_alignment
export PYTHONPATH=$PYTHONPATH:$RICHGEOAL

python scripts/gp_minimize.py $1 $2 $3

dir="$RICHGEOAL/output/opt"
file="$3.pkl"

swif outfile $file file:$dir/$file