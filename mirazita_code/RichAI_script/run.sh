#!/bin/bash

export CCDB_CONNECTION=sqlite:////w/hallb-scifs17exp/clas12/mirazita/RICH/clas12rich_reprocessing/ccdb/ccdb_4.3.2.sqlite
#echo $CCDB_CONNECTION

./runAI.pl $1

