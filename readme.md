# Rich AI ALignments

This software uses NN and Bayesian optimization for finding optimal geometric parameters (rotational angles and traslational displacement) of the
mirrors, aerogel panels and photomultiplier plane which compose the main part of the [RICH](https://clasweb.jlab.org/wiki/index.php/Clas12_RICH) detector of CLAS12.

This software is structured as follows:

###CODE
To install the code run:
```bash
source setup.csh
```
This will run the autoinstall.csh code, which install the Hipo4 libraries and compile the Mirazita code.
To run the code ccdb python api, pandas, numpy and root and the clas12 eventbuilder are needed. The best solution is to run it on the Jlab farm loading module clas12/2.1 (this is loaded with the setup.csh script).

mirazita_code direcotories contain anaylis of hipo files for rich code. 
- The FilterC directory has a script for filtering events with direct photon produced by an electron passing trough  one of Aerogel layer (or all the layers).
- The Plots directory has a script which outputs a root file and txt file. The root files has histograms, here an example (to output the pdf of the histogram the Drawing script is used) and the txt files contain the chi2 for the clusters and difference between the predicted Cherenkov angle and the measured one.
To choose one layer one has to input -L(0/1/2) for choosing layer 0,1 or 2 and input nothing for choosing all the layers.

costantini_code has scripts for updating the ccdb.

the run_* script run separately the various step for the alignment.
the main script run one step of the loop for the alignment. One has to provide the file (or a file with the list of files NOT YET IMPLEMENTED) with data and the layer of reference.

###CCDB
The [CCDB](https://clasweb.jlab.org/wiki/index.php/CLAS12_Constants_Database) is the CLAS12 databese which contains all the constants for the events reconstraction.
For the research of the optimal parameters multiple reconstructions of the events have to be done. For each reconstruction the CCDB has to be updated with the new choice of the paramters and the event_builder is called. 
The table in the ccdb which has to be updated is [/calibration/rich/misalignments](https://clasweb.jlab.org/cgi-bin/ccdb/versions?table=/calibration/rich/misalignments).

We will work with a local snapshot of this database, on a variation dedicated to the misalignments called misalignments (we lack of fantasy). 

The table is like this:
![Misalignments table](/fig/ccdb.png)

the first three columns define the component of the detecotr. The fourth sector is the sector of the RICH, the 20* layer are the 4 layers of the aerogel, the 30* layers are the mirrors and finally 401 is the photomultiplyer (PMT) plane.
The other six columns are the six parameters three translations (in cm) and three rotations (in mrad). 

###DATA
For the moment we use two hipo files as a proof of concept. One from an inbending run (5206), the other from an outbending run (5424).

Semi-raw data are in three main directories:

/lustre19/expphy/volatile/clas12/richskims/skim1/
/lustre19/expphy/volatile/clas12/richskims/skim2/
/lustre19/expphy/volatile/clas12/richskims/skim3/

Here a screenshot of the readme for the specs of the files in each directory. In each directory files are also divided in inbending and outbending runs.
![Misalignments table](/fig/data_repos.png)

##Alignment procedure
Here below described the alignment procedure which are made at present. This could change when bayesian optimization method is applied since this are thought in roder to align the rich's component separately.
###PMT
The PMT are align via a chi2 parameter which is present directly in a bank of the hipo files. This is a squared difference between the cluster position made by particle passing directly trough the PMT and the predicted position from the track reconstruction. 
At present the PMT are not align separatly, but the layer 0 paramters are changed, so that the entire rich move when the PMT are aligned. 
###AEROGEL
The aerogel is on three layers and each layer has a different number of tiles. 
The procedure for aligning the aerogel layer is based on comparing the cherenkov angle of electron measured by the rich computed only with direct photon with the theorical angle computed with the nominal refractive index. The angle difference is computed for each aerogel tile, but the parameters are referred to the layers.
Here the scheme of the four layers and tiles: 
![Layer 201-202](/fig/layer201-202.png)
![Layer 203-204](/fig/layer203-204.png)

