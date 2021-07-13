from __future__ import print_function

# Import libraries:
import hyperopt
import time
import os
import pandas as pd

from hyperopt import hp, tpe
from hyperopt.fmin import fmin
from database import ccdb_connection as cc, parameters_setting as pm

from run_control import run_plots
from run_control import run_reco
from functools import partial


def make_mean(file):
    f = open(file, "r")
    nline = 0
    mean = 0
    while (True):
        nline += 1
        line = f.readline()
        if not line:
            break

        mean = mean + abs(float(line.split()[-1].split('=')[-1]))
    mean = mean / nline
    f.close()
    return mean


def pass_dict_param_to_table(dict, table):
    for layer, val in dict.items():
        module = [4, int(layer.split('_')[1]), 0]
        pars = [layer.split('_')[0], val]
        pm.changing_one_parameter(table, module, pars)

    return table


def objective(space):
    # COMPUTING SCORE
    params = {
        'dx_401': float(space['dx_401']),
        'dy_401': float(space['dy_401']),
        'dz_401': float(space['dz_401']),
        'dthx_401': float(space['dthx_401']),
        'dthy_401': float(space['dthy_401']),
        'dthz_401': float(space['dthz_401']),
        'dx_201': float(space['dx_201']),
        'dy_201': float(space['dy_201']),
        'dz_201': float(space['dz_201']),
        'dthx_201': float(space['dthx_201']),
        'dthy_201': float(space['dthy_201']),
        'dthz_201': float(space['dthz_201']),
        'dx_202': float(space['dx_202']),
        'dy_202': float(space['dy_202']),
        'dz_202': float(space['dz_202']),
        'dthx_202': float(space['dthx_202']),
        'dthy_202': float(space['dthy_202']),
        'dthz_202': float(space['dthz_202'])
    }

    # CHANGING PARAM ON CCDB
    old_pars_table = cc.reading_ccdb(provider, calibration_table, variation)
    old_pars_table = pass_dict_param_to_table(params, old_pars_table)
    toadd = old_pars_table.values.tolist()
    cc.adding_to_ccdb(toadd, provider, calibration_table, variation)

    # start_time = time.time()
    # RUN EVENTBUILDER
    print("-----------------------------------------------------------------------------------------------")
    print("----------------------------------- START RECO -----------------------------------------")
    print("-----------------------------------------------------------------------------------------------")
    run_reco.runcommand(fileforreco)
    # reco_time = int(time.time() - start_time)
    # second_time = time.time()


    # RUN ANGLE ANALYSIS
    print("-----------------------------------------------------------------------------------------------")
    print("----------------------------------- START PLOTTING -----------------------------------------")
    print("-----------------------------------------------------------------------------------------------")

    run_plots.runcommand(fileforplot)
    # plot_time = int(time.time() - second_time)

    # SCORING
    score = make_mean(filefromplot)
    #, reco_time, plot_time
    print("score: ", score)
    return score


if __name__ == '__main__':

    maindir = os.getcwd() + "/database/"
    filterdir = maindir + "output/filter/"
    plotdir = maindir + "output/plots/"
    recodir = maindir + "output/reco/"
    fileforreco = filterdir + "rec_clas_5137_AIskim1_-1.hipo"
    fileforplot = recodir + "rec_clas_5137_AIskim1_-1.hipo"
    filefromplot = plotdir + "RichPlots_5137.out"

    print("-----------------------------------------------------------------------------------------------")
    print("----------------------------------- START OF ANALYSIS -----------------------------------------")
    print("-----------------------------------------------------------------------------------------------")

    start_time = time.time()


    print(("Start time: ", start_time))
    print("Init CCDB to zero ")

    calibration_connection = "sqlite:///" + maindir + "ccdb_4.3.2.sqlite"
    print(calibration_connection)
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

    # parameters = {'dx_401': 1,
    #     'dy_401': 1.,
    #     'dz_401': 4.,
    #     'dthx_401': 4.,
    #     'dthy_401': 1.,
    #     'dthz_401': 0.,
    #     'dx_201': 1.,
    #     'dy_201': 1.,
    #     'dz_201': 1.,
    #     'dthx_201': 0.,
    #     'dthy_201': 0.,
    #     'dthz_201': 0.,
    #     'dx_202': 2.,
    #     'dy_202': 1.,
    #     'dz_202': 0.,
    #     'dthx_202': 0.,
    #     'dthy_202': 3.,
    #     'dthz_202': 1.,
    # }
    #
    # test_obj, reco_time, plot_time = objective(parameters)
    #     print('{:02d}:{:02d}:{:02d}'.format(reco_time // 3600, (reco_time % 3600 // 60), reco_time % 60))
    #     print('{:02d}:{:02d}:{:02d}'.format(plot_time // 3600, (plot_time % 3600 // 60), plot_time % 60))
    #     print("Time for reco:", reco_time)
    #     print("Time for plot:", reco_time)
    # print("test score: ", test_obj)




    space = {
        'dx_401': hp.uniform('dx401', -10, 10),
        'dy_401': hp.uniform('dy401', -10, 10),
        'dz_401': hp.uniform('dz401', -10, 10),
        'dthx_401': hp.uniform('dtx401', -10, 10),
        'dthy_401': hp.uniform('dty401', -10, 10),
        'dthz_401': hp.uniform('dtz401', -10, 10),
        'dx_201': hp.uniform('dx201', -10, 10),
        'dy_201': hp.uniform('dy201', -10, 10),
        'dz_201': hp.uniform('dz201', -10, 10),
        'dthx_201': hp.uniform('dtx201', -10, 10),
        'dthy_201': hp.uniform('dty201', -10, 10),
        'dthz_201': hp.uniform('dtz201', -10, 10),
        'dx_202': hp.uniform('dx202', -10, 10),
        'dy_202': hp.uniform('dy202', -10, 10),
        'dz_202': hp.uniform('dz202', -10, 10),
        'dthx_202': hp.uniform('dtx202', -10, 10),
        'dthy_202': hp.uniform('dty202', -10, 10),
        'dthz_202': hp.uniform('dtz202', -10, 10)
        # 'dx203': hp.quniform('dx203', -0.1, 0.1, 0.001),
        # 'dy203': hp.uniform('dy203', -0.1, 0.1, 0.001),
        # 'dz203': hp.quniform('dz203', -0.1, 0.1, 0.001),
        # 'dtx203': hp.uniform('dtx203', -0.1, 0.1, 0.001),
        # 'dty203': hp.uniform('dty203', -0.1, 0.1, 0.001),
        # 'dtz203': hp.quniform('dtz203', -0.1, 0.1, 0.001)
    }

    trials = hyperopt.Trials()

    tpe = partial(
        hyperopt.tpe.suggest,

        # Sample 1000 candidate and select candidate that
        # has highest Expected Improvement (EI)
        n_EI_candidates=400,

        # Use 20% of best observations to estimate next
        # set of parameters
        gamma=0.2,

        # First XX trials are going to be random
        n_startup_jobs=200
    )

    best = fmin(fn=objective, space=space, algo=tpe, trials=trials, max_evals=3)

    print("Hyperopt estimated optimum {}".format(best))

    tot_time = int(time.time() - start_time)
    print('{:02d}:{:02d}:{:02d}'.format(tot_time // 3600, (tot_time % 3600 // 60), tot_time % 60))

