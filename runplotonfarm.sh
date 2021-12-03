#!/bin/bash

source ~/.bashrc
source setup1.sh

export PYTHONPATH=$PYTHONPATH:/work/clas12/users/costantini/RICH_alignment/
python /work/clas12/users/costantini/RICH_alignment/run_control/run_plots.py $1

dir="/work/clas12/users/costantini/RICH_alignment/output/plots"
file="RichPlots_2010.out"
swif outfile $file file:$dir/$file 
