import sys
import os
import subprocess

import ccdb_connection as cc
import parameters_setting as pm

if __name__ == "__main__":
    calibration_connection = "sqlite:///$PWD/ccdb_4.3.2.sqlite "
    calibration_table = '/calibration/rich/misalignments'
    variation = 'misalignements'
    user = "Costantini"

    module = [4, 201, 1]
    pars = [0, 0, 1, 1, 1, 0]

    RunNumber = "0"
    Layer = "-1"
    filetofilter = "file"

    # executing Mirazita code for filtering
    if sys.argv[0] == '-f':
        subprocess.run(["./mirazita_code/RichAI_FilterC/filterHipo", "-R" + RunNumber, "-L" + Layer, filetofilter])

    # executing Mirazita code for Reconstruction and comparison
    subprocess.run(["/mirazita_code/RichAI_script/run.sh", "list.file"])

    # execute Costantini code for update ccdb
    #  update ccdb

    provider = cc.connecting_ccdb(calibration_connection, variation)
    old_pars_table = cc.reading_ccdb(provider, calibration_table, variation)
    new_pars_table = pm.changing_parameters(pars, old_pars_table, module)

    toadd = new_pars_table.values.tolist()
    cc.adding_to_ccdb(toadd, provider, calibration_table, variation)
