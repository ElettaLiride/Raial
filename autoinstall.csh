#!/bin/tcsh
cd
git clone --recurse-submodules https://github.com/gavalian/hipo

cd hipo
make
cd ../

tar -xvf RichAI.tar
source setenv.csh
cd RichAI_FilterC
make
cd ../RichAI_Plots/
make
cd ../

source setenv
python setup.py