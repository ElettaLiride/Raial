#!/bin/bash

source /group/clas12/packages/setup.sh
module load clas12/pro
module load anaconda3
module load hipo/1.3

source /w/hallb-scshelf2102/clas12/users/costantini/ccdb/environment.bash
export CCDB_CONNECTION=sqlite:////work/clas12/users/costantini/RICH_alignment/database/ccdb_4.3.2.sqlite

conda activate /w/hallb-scshelf2102/clas12/users/costantini/RICH_alignment/alignment-env/
