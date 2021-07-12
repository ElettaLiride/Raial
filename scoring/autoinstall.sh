#!/bin/bash

if [[ ! -d "hipo" ]]
then
  git clone --recurse-submodules https://github.com/gavalian/hipo
  cd hipo
  make
  cd ../
  source setenv.sh
  cd RichAI_FilterC
  make
  cd ../RichAI_Plots/
  make
  cd ../
fi
