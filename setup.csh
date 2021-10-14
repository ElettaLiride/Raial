#!/bin/csh
#just a change
source /group/clas12/packages/setup.csh
module load clas12/2.1
#source mirazita_code/setenv.csh

#installing mirazita code
if (! -d "scoring/hipo") then
  cd scoring
  source autoinstall.csh
  cd ../

else
  cd scoring/
  source setenv.csh
  cd ../

endif

#making output direcotries
if ( ! -d "output" ) then
  mkdir output
  mkdir output/plots
  mkdir output/filter
  mkdir output/reco
endif

#CCDB env
cd database

wget https://clasweb.jlab.org/clas12offline/sqlite/ccdb/LATEST
set lat=`cat LATEST`
if (! -f ccdb_$lat.sqlite) then
    wget https://clasweb.jlab.org/clas12offline/sqlite/ccdb/ccdb_$lat.sqlite
endif
rm LATEST

if (! -f "ccdb_4.3.2.sqlite") then
  wget https://clasweb.jlab.org/clas12offline/sqlite/ccdb/clas12tags/ccdb_4.3.2.sqlite $PWD
endif

setenv PATH_CCDB_L $PWD/ccdb_$lat.sqlite
setenv PATH_CCDB_t $PWD/ccdb_4.3.2.sqlite

#connecting CCDB to local snapshot

setenv CCDB_CONNECTION sqlite:///$PATH_CCDB_L

unset lat
cd ../

#praparing python env
if (! -d "raial-env") then
  module load python3/3.9.5
  pip3 install virtualenv --user
  $HOME/.local/bin/virtualenv raial-env
endif

source raial-env/bin/activate.csh
ll
>>>>>>> master
end




