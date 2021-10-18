import sys
import os

from skopt import Space

from database import ccdb_connection as cc
from optimization.objective import obj_gp
from optimization.bo_gp import BoRichGp

if __name__ == "__main__":


    calibration_connection = "sqlite:///database/ccdb_4.3.2.sqlite"
    calibration_table = "/calibration/rich/misalignments"
    variation = "default"
    user = "Costantini"
    provider = cc.connecting_ccdb(calibration_connection, variation)

    # INIT CCDB
    cc.init_ccdb(provider, calibration_table, variation)
    # READING SPACE
    space = Space.from_yaml('example_space.yaml')
    # OPTIMIZE
    bo_optimizer = BoRichGp(obj=obj_gp, space=space, n_call=10, dir='output/opt', id='test')
    bo_optimizer.optimize()





    #
    # filterdir = maindir + "output/filter/"
    # recodir = maindir + "output/reco/"
    # plotsdir = maindir + "output/plots/"
    #
    # # OUT FROM THE LOOP
    # if len(sys.argv) == 3:
    #     nevents = " "
    # else:
    #     nevents = sys.argv[3]
    #
    # run = run_filter.runcommand(sys.argv[1], sys.argv[2], nevents)
    #
    # # INTO THE LOOP
    # fileforreco = filterdir + "rec_clas_" + run + "_AIskim1.hipo"
    # run_reco.runcommand(fileforreco)
    #
    # fileforplot = recodir + "rec_clas_" + run + "_AIskim1.hipo"
    # run_plots.runcommand(fileforplot)
    #
    # # HERE ADDING OPTIMIZATION PROCEDURE
    # # FILES .OUT TO USE FOR OPTIMIZATION ARE IN OUTPUT/PLOTS
    # # one has to provide to the function changing_parameters a module and a list of parameters (in the order of the ccdb
    # # table misalignment), for each module. An example below The function change one module of the "old_pars_table"
    # # at the time so the table has to be updated every time.
    #
    # module = [4, 201, 0]
    # pars = [0, 0, 1, 1, 1, 0]
    #
    # # SHOULD LOOP OVER EACH MODULE
    #
    # # execute Costantini code for update ccdb
    # # update ccdb
    # new_pars_table = pm.changing_parameters(old_pars_table, module, pars)
    # toadd = new_pars_table.values.tolist()
    #
    # cc.adding_to_ccdb(toadd, provider, calibration_table, variation)
