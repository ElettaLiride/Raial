import sys

from costantini_code import ccdb_connection as cc, parameters_setting as pm

import run_reco
import run_plots
import run_filter

if __name__ == "__main__":

    filterdir = "output/filter"
    recodir = "output/reco"
    plotsdir = "output/plots"



    run = run_filter.runcommand(sys.argv[1], sys.argv[2])
    fileforreco = filterdir + "rec_clas_" + run + "_AISkim1.hipo"

    run_reco.runcommand(fileforreco)
    fileforplot = recodir + "rec_clas_" + run + "_AISkim1.hipo"

    run_plots.runcommand(fileforplot)

    # HERE ADDING OPTIMIZATION PROCEDURE
    # FILES .OUT TO USE FOR OPTIMIZATION ARE IN OUTPUT/PLOTS

    module = [4, 201, 1]
    pars = [0, 0, 1, 1, 1, 0]
    # execute Costantini code for update ccdb
    # update ccdb

    calibration_connection = "sqlite:////$PWD/ccdb_4.3.2.sqlite "
    calibration_table = '/calibration/rich/misalignments'
    variation = 'misalignements'
    user = "Costantini"


    provider = cc.connecting_ccdb(calibration_connection, variation)
    old_pars_table = cc.reading_ccdb(provider, calibration_table, variation)
    new_pars_table = pm.changing_parameters(pars, old_pars_table, module)

    toadd = new_pars_table.values.tolist()
    cc.adding_to_ccdb(toadd, provider, calibration_table, variation)
