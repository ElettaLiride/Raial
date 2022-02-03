#!/bin/bash


source ~/.bashrc
source setup.sh

export PYTHONPATH=$PYTHONPATH:/work/clas12/users/costantini/RICH_alignment/
python /work/clas12/users/costantini/RICH_alignment/run_control/run_filter.py $1 $2 $3
