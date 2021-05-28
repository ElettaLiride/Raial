import sys
import os

from costantini_code import ccdb_connection as cc, parameters_setting as pm

import run_reco
import run_plots
import run_filter

if __name__ == "__main__":
    ## INIT CCDB

    maindir = os.getcwd() + "/"
    calibration_connection = "sqlite:///" + maindir + "ccdb_4.3.2.sqlite"
    calibration_table = "/calibration/rich/misalignments"
    variation = "misalignments"
    user = "Costantini"

    provider = cc.connecting_ccdb(calibration_connection, variation)
    old_pars_table = cc.reading_ccdb(provider, calibration_table, variation)
    for col in old_pars_table.columns:
        if col == "sector" or col == "layer" or col == "component":
            continue
        else:
            old_pars_table[col].values[:] = 0
    toadd = old_pars_table.values.tolist()
    cc.adding_to_ccdb(toadd, provider, calibration_table, variation)


    filterdir = maindir + "output/filter/"
    recodir = maindir + "output/reco/"
    plotsdir = maindir + "output/plots/"

    # OUT FROM THE LOOP
    if len(sys.argv) == 3:
        nevents = " "
    else:
        nevents = sys.argv[3]

    run = run_filter.runcommand(sys.argv[1], sys.argv[2], nevents)
    fileforreco = filterdir + "rec_clas_" + run + "_AIskim1.hipo"

    # INTO THE LOOP
    run_reco.runcommand(fileforreco)
    fileforplot = recodir + "rec_clas_" + run + "_AIskim1.hipo"

    run_plots.runcommand(fileforplot)

    # HERE ADDING OPTIMIZATION PROCEDURE
    # FILES .OUT TO USE FOR OPTIMIZATION ARE IN OUTPUT/PLOTS
    # one has to provide to the function changing_parameters a module and a list of parameters (in the order of the ccdb
    # table misalignment), for each module. An example below The function change one module of the "old_pars_table"
    # at the time so the table has to be updated every time.

    module = [4, 201, 0]
    pars = [0, 0, 1, 1, 1, 0]

    # SHOULD LOOP OVER EACH MODULE

    # execute Costantini code for update ccdb
    # update ccdb
    new_pars_table = pm.changing_parameters(pars, old_pars_table, module)
    toadd = new_pars_table.values.tolist()

    cc.adding_to_ccdb(toadd, provider, calibration_table, variation)
