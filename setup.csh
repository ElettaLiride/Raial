#!/bin/csh


source /group/clas12/packages/setup.csh
module load clas12/2.1
#source mirazita_code/setenv.csh

#installing mirazita code
if (! -d "mirazita_code/hipo") then
  cd mirazita_code
  source autoinstall.csh
  cd ../
endif

cd mirazita_code/
source setenv.csh
cd ../

#making output direcotries
if ( ! -d "output" ) then
  mkdir output
  mkdir output/plots
  mkdir output/filter
  mkdir output/reco
endif

#coping ccdb snapshot
if (! -f "ccdb_4.3.2.sqlite") then
  cp /group/clas12/packages/local/share/ccdb/sqlite/clas12tags/ccdb_4.3.2.sqlite $PWD
endif

#connecting CCDB to local snapshot
setenv CCDB_CONNECTION sqlite:///$PWD/ccdb_4.3.2.sqlite

#praparing python env
if (! -d "raial-env") then
  module load python3/3.9.5
  pip3 install virtualenv --user
  $HOME/.local/bin/virtualenv raial-env
endif

source raial-env/bin/activate.csh

end




