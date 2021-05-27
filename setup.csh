#!/bin/csh


source /group/clas12/packages/setup.csh

module load clas12/2.1

source autoinstall.csh

cd mirazita_code
source setenv.csh
cd ../

setenv CCDB_CONNECTION sqlite:///$PWD/ccdb_4.3.2.sqlite




