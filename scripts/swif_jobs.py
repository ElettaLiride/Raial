import os
import sys

from src.python import tools as t
from src.python import globalpath


RICHGEOAL = os.getenv("RICHGEOAL")

time = "6h"
ram = "1500mb"
name = "test"
phase = "0"
track = "debug"

aerogel_dat = RICHGEOAL + "/Aerogel_ccdb.dat"
ccdb_file = RICHGEOAL + "/database/ccdb_4.3.2_old.sqlite"
ccdb_set_file = RICHGEOAL + "/../ccdb/environment.bash"
set_file = RICHGEOAL + "setup.sh"
python_reco = RICHGEOAL + "/scripts/run_reco.py"
recon_util = RICHGEOAL + "/work/clas12/users/devita/rich/oldVersionWithNewGeo/clas12-offline-software/coatjava" +\
                         "/bin/recon-util"
python_plot = RICHGEOAL + "/scripts/run_plots.py"
rich_plot = RICHGEOAL + "/work/clas12/users/costantini/RICH_alignment/scoring/RichAI_Plots/richPlots"


def add_job_1(WF, filelist, RN, space_yaml, config_yaml):
    size = 0
    for fname in filelist:
        size += os.path.getsize(fname)/1024./1024.*1.15
    cmd = "swif add-job " +  "-workflow " + WF
    cmd += " -ram " + ram
    cmd += " -track " + track
    cmd += " -disk " + "{0:.0f}".format(size)
    cmd += " -project clas12"
    cmd += " -phase " + phase
    cmd += " -name " + name
    cmd += " -time " + time
    cmd += " -shell /bin/bash"
    cmd += " -input " + " file:" + aerogel_dat
    cmd += " -input " + " file:" + ccdb_file
    cmd += " -input " + " file:" + set_file
    cmd += " -input " + " file:" + python_reco
    cmd += " -input " + " file:" + recon_util
    cmd += " -input " + " file:" + python_plot
    cmd += " -input " + " file:" + rich_plot

    cmd += " -input " + " file:" + yaml_opt
    cmd += " -input " + " file:" + yaml_space
    cmd += " -input " + " file:" + yaml_reco
    cmd += " -input " + " file:" + ccdb_sqlite
    cmd += " -input " + " file:" + aerogel_dat

    cmd += " -input " + " file:" + rich_plot
    cmd += " -input " + " file:" + rich_reco
    cmd += " -input " + " file:" + rich_objective
    cmd += " -input " + " file:" + rich_global
    cmd += " -input " + " file:" + rich_util

    cmd += " -input " + " file:" + bash_script


    for fname in filelist:
        cmd += " -input " + os.path.basename(fname) + " file:" + fname

    cmd += " ./run_opt " + filelist + " " + RN + " " + yaml
    _ = t.runcommand(cmd)

def add_job(WF, filelist, RN, yaml):
    size = 0
    for fname in filelist:
        size += os.path.getsize(fname)/1024./1024.*1.15
    cmd = "swif add-job " +  "-workflow " + WF
    cmd += " -ram " + ram
    cmd += " -track " + track
    cmd += " -disk " + "{0:.0f}".format(size)
    cmd += " -project clas12"
    cmd += " -phase " + phase
    cmd += " -name " + name
    cmd += " -time " + time
    cmd += " -shell /bin/bash"
    cmd += " -input " + " file:" + aerogel_dat
    cmd += " -input " + " file:" + ccdb_file
    cmd += " -input " + " file:" + set_file
    cmd += " -input " + " file:" + python_reco
    cmd += " -input " + " file:" + recon_util
    cmd += " -input " + " file:" + python_plot
    cmd += " -input " + " file:" + rich_plot

    for fname in filelist:
        cmd += " -input " + os.path.basename(fname) + " file:" + fname

    cmd += " ./run_opt " + filelist + " " + RN + " " + yaml
    _ = t.runcommand(cmd)

def run_workflow(WF):
    _ = t.runcommand('swif run ' + WF)

def create_workflow(WF):
    _ = t.runcommand('swif create ' + WF)

if __name__=="__main__":
    create_workflow(sys.argv[1])
    add_job(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    #run_workflow(sys.argv[1])

    # for filter
    # swif
    # add-job
    # -workflow AL_test
    # -ram 1500mb
    # -project clas12
    # -time 6h
    # -track debug
    # -phase 0
    # -name test_2
    # -shell /bin/bash
    # -input run_filter.py file:$PWD/run_control/run_filter.py
    # -input filterHipo file:$PWD/scoring/RichAI_FilterC/filterHipo
    # -input rec_clas_005032.evio.00085-00089.hipo file:/cache/clas12/rg-a/production/recon/fall2018/torus-1/pass1/v0/dst/recon/005032/rec_clas_005032.evio.00085-00089.hipo
    # -input runfilteronfarm.sh file:$PWD/runfilteronfarm.sh
    # -input setup.sh file:$PWD/setup.sh
    # -input environment.bash file:$PWD/../ccdb/environment.bash
    # -input ccdb_4.3.2_old.sqlite file:$PWD/database/ccdb_4.3.2_old.sqlite
    # -input test.txt file:$PWD/output/test.txt -stderr file:$PWD/err.txt
    # ./runfilteronfarm.sh /work/clas12/users/costantini/RICH_alignment/output/test.txt 27 -1

    # for filter
    # swif add-job -workflow AL_test -ram 1500mb -project clas12 -time 6h -track debug -phase 0 -name test_2 -shell /bin/bash -input run_filter.py file:$PWD/run_control/run_filter.py -input filterHipo file:$PWD/scoring/RichAI_FilterC/filterHipo -input rec_clas_005032.evio.00085-00089.hipo file:/cache/clas12/rg-a/production/recon/fall2018/torus-1/pass1/v0/dst/recon/005032/rec_clas_005032.evio.00085-00089.hipo -input runfilteronfarm.sh file:$PWD/runfilteronfarm.sh -input setup.sh file:$PWD/setup.sh -input environment.bash file:$PWD/../ccdb/environment.bash -input ccdb_4.3.2_old.sqlite file:$PWD/database/ccdb_4.3.2_old.sqlite -input test.txt file:$PWD/output/test.txt -stderr file:$PWD/err.txt ./runfilteronfarm.sh /work/clas12/users/costantini/RICH_alignment/output/test.txt 27 -1
    # swif2 add-job -workflow AL_test -ram 1500mb -account clas12 -time 6h -partition debug -phase 0 -name test_2 -shell /bin/bash -input run_filter.py file:$PWD/run_control/run_filter.py -input filterHipo file:$PWD/scoring/RichAI_FilterC/filterHipo -input rec_clas_005032.evio.00085-00089.hipo file:/cache/clas12/rg-a/production/recon/fall2018/torus-1/pass1/v0/dst/recon/005032/rec_clas_005032.evio.00085-00089.hipo -input runfilteronfarm.sh file:$PWD/runfilteronfarm.sh -input setup.sh file:$PWD/setup.sh -input environment.bash file:$PWD/../ccdb/environment.bash -input ccdb_4.3.2_old.sqlite file:$PWD/database/ccdb_4.3.2_old.sqlite -input test.txt file:$PWD/output/test.txt -stderr file:$PWD/err.txt ./runfilteronfarm.sh /work/clas12/users/costantini/RICH_alignment/output/test.txt 27 -1

    # swif2 add-job -workflow AL_test -ram 1500mb -account clas12 -time 6h -partition debug -phase 0 -name test_2 -shell /bin/bash -input run_filter.py file:$VOLPATH/scripts/run_filter.py -input filterHipo file:$VOLPATH/bin/filterHipo -input rec_clas_005032.evio.00085-00089.hipo file:/cache/clas12/rg-a/production/recon/fall2018/torus-1/pass1/v0/dst/recon/005032/rec_clas_005032.evio.00085-00089.hipo -input runfilteronfarm.sh file:$VOLPATH/bin/runfilteronfarm.sh -input setup.sh file:$VOLPATH/setup.sh -input environment.bash file:$VOLPATH/../ccdb/environment.bash -input ccdb_4.3.2_old.sqlite file:$VOLPATH/database/ccdb_4.3.2_old.sqlite -input test.txt file:$VOLPATH/output/test.txt -stderr file:$VOLPATH/err.txt ./$VOLPATH/bin/runfilteronfarm.sh $VOLPATH/output/test.txt 27 -1

    ##for reco
    # swif add-job -workflow reco_test -ram 1500mb -project clas12 -time 6h -track debug -phase 0 -name test_reco -shell /bin/bash -input run_reco.py file:$PWD/run_control/run_reco.py -input recon_util file:/work/clas12/users/devita/rich/oldVersionWithNewGeo/clas12-offline-software/coatjava/bin/recon-util -input rec_clas_27_AIskim1_-1.hipo file:$PWD/output/filter/rec_clas_27_AIskim1_-1.hipo -input runrecoonfarm.sh file:$PWD/runrecoonfarm.sh -input setup.sh file:$PWD/setup.sh -input environment.bash file:$PWD/../ccdb/environment.bash -input ccdb_4.3.2_old.sqlite file:$PWD/database/ccdb_4.3.2_old.sqlite -input test.txt file:$PWD/output/test.txt -stderr file:$PWD/err.txt ./runrecoonfarm.sh rec_clas_27_AIskim1_-1.hipo

    ## for plot
    # swif add-job
    # -workflow AL_test
    # -ram 1500mb
    # -project clas12
    # -time 6h
    # -track debug
    # -phase 0
    # -name test_plot
    # -shell /bin/bash

    # -input run_plot.py file:$PWD/run_control/run_plots.py
    # -input richPlots file:/work/clas12/users/costantini/RICH_alignment/scoring/RichAI_Plots/richPlots
    # -input rec_clas_27_AIskim1_-1.hipo file:$PWD/output/reco/rec_clas_27_AIskim1_-1.hipo
    # -input runplotonfarm.sh file:$PWD/runplotonfarm.sh
    # -input setup.sh file:$PWD/setup.sh
    # -input environment.bash file:$PWD/../ccdb/environment.bash
    # -input ccdb_4.3.2_old.sqlite file:$PWD/database/ccdb_4.3.2_old.sqlite
    # -stderr file:$PWD/err_plot.txt
    # ./runplotonfarm.sh /work/clas12/users/costantini/RICH_alignment/output/reco/rec_clas_27_AIskim1_-1.hipo
    # swif add-job -workflow AL_test -ram 1500mb -project clas12 -time 6h -track debug -phase 0 -name test_plot -shell /bin/bash -input run_plots.py file:$PWD/run_control/run_plots.py -input richPlots file:/work/clas12/users/costantini/RICH_alignment/scoring/RichAI_Plots/richPlots -input rec_clas_27_AIskim1_-1.hipo file:$PWD/output/reco/rec_clas_27_AIskim1_-1.hipo -input runplotonfarm.sh file:$PWD/runplotonfarm.sh -input setup.sh file:$PWD/setup.sh -input environment.bash file:$PWD/../ccdb/environment.bash -input ccdb_4.3.2_old.sqlite file:$PWD/database/ccdb_4.3.2_old.sqlite -stderr file:$PWD/err_plot.txt ./runplotonfarm.sh /work/clas12/users/costantini/RICH_alignment/output/reco/rec_clas_27_AIskim1_-1.hipo
    ##QUELLA FINALE:
    # swif
    # add-job
    # -workflow AL_test
    # -ram 1500mb
    # -project clas12
    # -time 6h
    # -track debug
    # -phase 0
    # -name test_2
    # -shell /bin/bash

    # -input rec_clas_27_AIskim1_-1.hipo file:$PWD/output/filter/rec_clas_27_AIskim1_-1.hipo
    # -input setup.sh file:$PWD/setup.sh
    # -input environment.bash file:$PWD/../ccdb/environment.bash
    # -input ccdb_4.3.2_old.sqlite file:$PWD/database/ccdb_4.3.2_old.sqlite
    # -input run_reco.py file:$PWD/run_control/run_reco.py
    # -input run_plot.py file:$PWD/run_control/run_plots.py
    # -input recon_util file:/work/clas12/users/devita/rich/oldVersionWithNewGeo/clas12-offline-software/coatjava/bin/recon-util
    # -input richPlots file:/work/clas12/users/costantini/RICH_alignment/scoring/RichAI_Plots/richPlots
    # -input runplotonfarm.sh file:$PWD/runplotonfarm.sh
    # -input Aerogel_ccdb.dat file:$PWD/Aerogel_ccdb.dat
    # -stderr file:$PWD/err_plot.txt
    # ./runplotonfarm.sh /work/clas12/users/costantini/RICH_alignment/output/reco/rec_clas_27_AIskim1_-1.hipo

    # swif add-job -workflow AL_test -ram 1500mb -project clas12 -time 6h -track debug -phase 0 -name test_all -shell /bin/bash -input opt_firstlayer.py file:$PWD/optimization/opt_firstlayer.py -input recon_util file:/work/clas12/users/devita/rich/oldVersionWithNewGeo/clas12-offline-software/coatjava/bin/recon-util -input rec_clas_27_AIskim1_-1.hipo file:$PWD/output/filter/rec_clas_27_AIskim1_-1.hipo -input richPlots file:$PWD/scoring/RichAI_Plots/richPlots -input runallprocedure.sh file:$PWD/runallprocedure.sh -input setup.sh file:$PWD/setup.sh -input environment.bash file:$PWD/../ccdb/environment.bash -input ccdb_4.3.2_old.sqlite file:$PWD/database/ccdb_4.3.2_old.sqlite -stderr file:$PWD/err_all.txt ./runallprocedure.sh



#"root -l -b -q '" . $root_plots . "(\"" . $fileRoot . "\")'"

