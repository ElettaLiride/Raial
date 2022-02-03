#!/bin/bash

source ~/.bashrc
source setup.sh

export PYTHONPATH=$PYTHONPATH:/work/clas12/users/costantini/RICH_alignment/
python /work/clas12/users/costantini/RICH_alignment/run_control/run_reco.py $1

dir="/work/clas12/users/costantini/RICH_alignment/output/reco"
file="out_rec_clas_27_AIskim1_-1.hipo"
#echo $dir/$file
swif outfile $file file:$dir/$file
