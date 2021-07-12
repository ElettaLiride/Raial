#!/bin/tcsh

if ( ! -d "hipo" ) then
  git clone --recurse-submodules https://github.com/gavalian/hipo
  cd hipo
  make
  cd ../
  source setenv.csh
  cd RichAI_FilterC
  make
  cd ../RichAI_Plots/
  make
  cd ../
endif

