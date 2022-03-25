#!/bin/bash
export RICHGEOAL=$PWD
export PYTHONPATH=$PYTHONPATH:$RICHGEOAL
export PATH=$PATH:/$RICHGEOAL/bin

if [[ ! -f "$RICHGEOAL/config/ccdbsnapshot/ccdb_4.3.2.sqlite" ]]
then
  wget https://clasweb.jlab.org/clas12offline/sqlite/ccdb/clas12tags/cccdb_4.3.2.sqlite
  mv cccdb_4.3.2.sqlite $RICHGEOAL/config/ccdbsnapshot
fi

cp $RICHGEOAL/config/ccdbsnapshot/ccdb_4.3.2.sqlite $RICHGEOAL/config/ccdbsnapshot/ccdb_$1.sqlite
export CCDB_CONNECTION=sqlite:///$RICHGEOAL/config/ccdbsnapshot/ccdb_$1.sqlite

## SetUp for jlab farm
if [[ -d "/group/" ]]
then
source /group/clas12/packages/setup.sh
module load clas12/pro
module load anaconda3
module load hipo/1.3

export HIPO4ROOT=$HIPO

source /w/hallb-scshelf2102/clas12/users/costantini/ccdb/environment.bash
conda activate /w/hallb-scshelf2102/clas12/users/costantini/RICH_alignment/alignment-env/

fi

export HIPO4LIB=$HIPO4ROOT/lib
export HIPO4INC=$HIPO4ROOT/hipo4
export LZ4DIR=$HIPO4ROOT/lz4

