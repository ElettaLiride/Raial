#!/bin/bash
export RICHGEOAL=$PWD
export PYTHONPATH=$PYTHONPATH:$RICHGEOAL


## SetUp for jlab farm
if [[ -d "/group/" ]]
then
source /group/clas12/packages/setup.sh
module load clas12/pro
module load anaconda3
module load hipo/1.3

export HIPO4ROOT=$HIPO
export HIPO4LIB=$HIPO4ROOT/lib
export HIPO4INC=$HIPO4ROOT/hipo4
export LZ4DIR=$HIPO4ROOT/lz4


source /w/hallb-scshelf2102/clas12/users/costantini/ccdb/environment.bash
conda activate /w/hallb-scshelf2102/clas12/users/costantini/RICH_alignment/alignment-env/

fi

export CCDB_CONNECTION=sqlite:///$RICHGEOAL/config/ccdb_4.3.2.sqlite
