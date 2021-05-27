import sys

from costantini_code import ccdb_connection as cc, parameters_setting as pm

import run_reco
import run_plots
import run_filter

if __name__ == "__main__":
    ## INIT CCDB

    calibration_connection = "sqlite:////work/clas12/users/costantini/RICH_alignement/Costantini_script/ccdb_4.3.2.sqlite"
    calibration_table = "/calibration/rich/misalignments"
    variation = "misalignments"
    user = "Costantini"

    provider = cc.connecting_ccdb(calibration_connection, variation)
    old_pars_table = cc.reading_ccdb(provider, calibration_table, variation)
    for col in old_pars_table.columns:
        if col == "sector" or col == "layer" or col == "component":
            break
        else:
            old_pars_table[col].values[:] = 0
    toadd = old_pars_table.values.tolist()
    cc.adding_to_ccdb(toadd, provider, calibration_table, variation)


    filterdir = "$PWD/output/filter/"
    recodir = "$PWD/output/reco/"
    plotsdir = "$PWD/output/plots/"

    # OUT FROM THE LOOP
    run = run_filter.runcommand(sys.argv[1], sys.argv[2], sys.argv[3])
    fileforreco = filterdir + "rec_clas_" + run + "_AISkim1.hipo"

    # INTO THE LOOP
    run_reco.runcommand(fileforreco)
    fileforplot = recodir + "rec_clas_" + run + "_AISkim1.hipo"

    run_plots.runcommand(fileforplot)

    # HERE ADDING OPTIMIZATION PROCEDURE
    # FILES .OUT TO USE FOR OPTIMIZATION ARE IN OUTPUT/PLOTS
    # one has to provide to the function changing_parameters a module and a list of parameters (in the order of the ccdb
    # table misalignment), for each module. An example below The function change one module of the "old_pars_table"
    # at the time so the table has to be updated every time.

    module = [4, 201, 1]
    pars = [0, 0, 1, 1, 1, 0]


    # execute Costantini code for update ccdb
    # update ccdb
    new_pars_table = pm.changing_parameters(pars, old_pars_table, module)
    toadd = new_pars_table.values.tolist()
    cc.adding_to_ccdb(toadd, provider, calibration_table, variation)
