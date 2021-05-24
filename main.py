import sys
import os
import subprocess

import ccdb_connection as cc
import parameters_setting as pm

if __name__=="__main__":
    calibration_connection = "sqlite:////work/clas12/users/costantini/RICH_alignement/Costantini_script/ccdb_4.3.2.sqlite"
    calibration_table      = '/calibration/rich/misalignments'
    variation              = 'misalignements'
    user                   = "Costantini"
    module = [4,201,1]
    pars = [0,0,1,1,1,0]
    RunNumber = "0"
    Layer = "-1"
    filetofilter = "file"

    ## update ccdb

    provider = cc.connecting_ccdb(calibration_connection)
    old_pars_table = cc.reading_ccdb(provider, calibration_table, variation)
    new_pars_table = pm.changing_parameters(pars, old_pars_table, module[0], module[1], module[2])

    toadd = new_pars_table.values.tolist()
    cc.adding_to_ccdb(toadd, provider, calibration_table, variation)

    # ##executing Mirazita code for filtering
    # if sys.argv[0] == '-f':
    #     subprocess.run(["./mirazita_code/RichAI_FilterC/filterHipo", "-R" + RunNumber, "-L" + Layer, filetofilter] )
    #
    # ##executing Mirazita code for Reconstruction and comparison
    # subprocess.run(["/mirazita_code/RichAI_script/run.sh", "list.file"])
    #
    # ##execute Costantini code for update ccdb
