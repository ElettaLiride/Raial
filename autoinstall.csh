#!/bin/tcsh
cd mirazita_code

if [ ! -d "hipo" ]
then
  git clone --recurse-submodules https://github.com/gavalian/hipo

  cd hipo

  source setenv.csh

  make
  cd ../

  cd RichAI_FilterC

  make

  cd ../RichAI_Plots/

  make

  cd ../

else

 source setenv.csh

fi

