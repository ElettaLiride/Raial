#!/bin/bash
export RICHGEOAL=$PWD
export CCDB_CONNECTION=sqlite:///$RICHGEOAL/config/ccdb_4.3.2.sqlite

## SetUp for jlab farm
if [[ -d "/group/" ]]
then
source /group/clas12/packages/setup.sh
module load clas12/pro
module load anaconda3
module load hipo/1.3

source /w/hallb-scshelf2102/clas12/users/costantini/ccdb/environment.bash

conda activate /w/hallb-scshelf2102/clas12/users/costantini/RICH_alignment/alignment-env/

## Setup for local env
else
export PYTHONPATH=$PYTHONPATH:$RICHGEOAL

fi