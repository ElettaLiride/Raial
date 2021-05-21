## Software for the alignment of Rich's components of CLAS12

This software uses NN and Bayesian optimization for finding optimal geometric parameter (angles and positions) of the
mirrors, aerogel panels and photomultiplier plane which constitue the main part of the RICH detector of CLAS12.

This software is structured as follows:

At the moment we are working only on the aerogel panels. For the alignment of these components we use as input


1) Download and install the hipo libraries
> git clone --recurse-submodules https://github.com/gavalian/hipo
> cd hipo
> make
> cd ../

2) Copy the analysis programs
> tar -xvf RichAI.tar
> source setenv.csh
> cd RichAI_FilterC
> make
> cd ../RichAI_Plots/
> make
> cd ../

3) Run the code
> cd RichAI_script/

Make the list of input hipo files
> ls /hipodir/hipofiles > files.list
> ./run.sh files.list

