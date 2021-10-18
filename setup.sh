#!/bin/bash

source /group/clas12/packages/setup.sh
module load clas12/2.1
# source mirazita_code/setenv.sh

#installing mirazita code
if [[ ! -d "scoring/hipo" ]]
then
  cd scoring
  source autoinstall.sh
  cd ../

else
  cd scoring/
  source setenv.sh
  cd ../

fi

#making output direcotries
if [[ ! -d "output" ]]
then
  mkdir output
  mkdir output/plots
  mkdir output/filter
  mkdir output/reco
  mkdir output/opt
fi

#CCDB env
cd database

#wget https://clasweb.jlab.org/clas12offline/sqlite/ccdb/LATEST
#lat=$(cat LATEST)
#
#if [[ ! -f ccdb_$lat.sqlite ]]
#then
#    wget https://clasweb.jlab.org/clas12offline/sqlite/ccdb/ccdb_$lat.sqlite
#fi
#rm LATEST

if [[ ! -f "ccdb_4.3.2.sqlite" ]]
then
  wget https://clasweb.jlab.org/clas12offline/sqlite/ccdb/clas12tags/ccdb_4.3.2.sqlite $PWD
fi

export PATH_CCDB_L=$PWD/ccdb_$lat.sqlite
export PATH_CCDB_t=$PWD/ccdb_4.3.2.sqlite

#connecting CCDB to local snapshot

export CCDB_CONNECTION=sqlite:///$PATH_CCDB_t

cd ../


##praparing python env
if [[ ! -d "alignment-env" ]]
then
  module load anaconda3
  conda create -p alignment-env
  conda activate 
  pip install scikit-optimize
  pip install pandas
  pip install matplotplib
else
  source activate alignment-env
fi

