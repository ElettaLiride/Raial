#!/bin/bash

source ~/.bashrc
source setup.sh

export PYTHONPATH=$PYTHONPATH:/work/clas12/users/costantini/RICH_alignment/
python /work/clas12/users/costantini/RICH_alignment/run_control/run_plots.py $1

dir="/work/clas12/users/costantini/RICH_alignment/output/plots"
file="RichPlots_2010.out"
echo $dir/$file
swif outfile $file file:$dir/$file 
