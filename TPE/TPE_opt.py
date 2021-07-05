from __future__ import print_function

# Import libraries:
import hyperopt
import pandas as pd
import time

from hyperopt import hp, tpe
from hyperopt.fmin import fmin
from costantini_code import ccdb_connection as cc, parameters_setting as pm
import os
from costantini_code import parameters_setting as pm
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

        mean = mean + float(line.split()[-1].split(sep='=')[-1])
    mean = mean / nline
    f.close()
    return mean


def pass_dict_param_to_table(dict, table):
    for layer, val in dict.items():
        module = [4, int(layer.split('_')[1]), 0]
        pars = [layer.split('_')[0], val]
        pm.changing_one_parameter(table, module, pars)

    return table


def objective(params):
    # COMPUTING SCORE

    # CHANGING PARAM ON CCDB
    old_pars_table = cc.reading_ccdb(provider, calibration_table, variation)
    old_pars_table = pass_dict_param_to_table(params, old_pars_table)
    toadd = old_pars_table.values.tolist()
    cc.adding_to_ccdb(toadd, provider, calibration_table, variation)

    sub_time1 = time.clock()
    # RUN EVENTBUILDER
    print("-----------------------------------------------------------------------------------------------")
    print("----------------------------------- START RECO -----------------------------------------")
    print("-----------------------------------------------------------------------------------------------")
    #run_reco.runcommand(fileforreco)
    sub_time2 = time.clock()

    # RUN ANGLE ANALYSIS
    print("-----------------------------------------------------------------------------------------------")
    print("----------------------------------- START PLOTTING -----------------------------------------")
    print("-----------------------------------------------------------------------------------------------")
    #run_plots.runcommand(fileforplot)
    sub_time3 = time.clock()

    # SCORING
    score = make_mean(filefromplot)

    reco_time = sub_time2 - sub_time1
    plot_time = sub_time3 - sub_time2

    return score, reco_time, plot_time


if __name__ == '__main__':

    filterdir = "output/filter/"
    plotdir = "output/plots/"
    recodir = "output/reco/"
    fileforreco = filterdir + "rec_clas_5206_AIskim1_-1.hipo"
    fileforplot = recodir + "rec_clas_5206_AIskim1_-1.hipo"
    filefromplot = plotdir + "RichPlots_5206.out"

    print("-----------------------------------------------------------------------------------------------")
    print("----------------------------------- START OF ANALYSIS -----------------------------------------")
    print("-----------------------------------------------------------------------------------------------")

    start_time = time.clock()


    print(("Start time: ", start_time))
    print("Init CCDB to zero ")

    calibration_connection = "sqlite:///../ccdb_4.3.2.sqlite"
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

    parameters = {'dx_401': 1,
        'dy_401': 1.,
        'dz_401': 4.,
        'dthx_401': 4.,
        'dthy_401': 1.,
        'dthz_401': 0.,
        'dx_201': 1.,
        'dy_201': 1.,
        'dz_201': 1.,
        'dthx_201': 0.,
        'dthy_201': 0.,
        'dthz_201': 0.,
        'dx_202': 2.,
        'dy_202': 1.,
        'dz_202': 0.,
        'dthx_202': 0.,
        'dthy_202': 3.,
        'dthz_202': 1.,
    }

    test_obj, reco_time, plot_time = objective(parameters)

    print("test score: ", test_obj)

    t1 = time.clock() - start_time

    print("Total time elapsed: ", t1)
    print("Time for reco:", reco_time)
    print("Time for plot:", reco_time)


    # space = {
    #     'dx_401': hp.uniform('dx401', -10, 10, 0.001),
    #     'dy_401': hp.uniform('dy401', -10, 10, 0.001),
    #     'dz_401': hp.uniform('dz401', -10, 10, 0.001),
    #     'dthx_401': hp.uniform('dtx401', -10, 10, 0.001),
    #     'dthy_401': hp.uniform('dty401', -10, 10, 0.001),
    #     'dthz_401': hp.uniform('dtz401', -10, 10, 0.001),
    #     'dx_201': hp.uniform('dx201', -10, 10, 0.001),
    #     'dy_201': hp.uniform('dy201', -10, 10, 0.001),
    #     'dz_201': hp.uniform('dz201', -10, 10, 0.001),
    #     'dthx_201': hp.uniform('dtx201', -10, 10, 0.001),
    #     'dthy_201': hp.uniform('dty201', -10, 10, 0.001),
    #     'dthz_201': hp.uniform('dtz201', -10, 10, 0.001),
    #     'dx_202': hp.uniform('dx202', -10, 10, 0.001),
    #     'dy_202': hp.uniform('dy202', -10, 10, 0.001),
    #     'dz_202': hp.uniform('dz202', -10, 10, 0.001),
    #     'dthx_202': hp.uniform('dtx202', -10, 10, 0.001),
    #     'dthy_202': hp.uniform('dty202', -10, 10, 0.001),
    #     'dthz_202': hp.uniform('dtz202', -10, 10, 0.001),
    #     # 'dx203': hp.quniform('dx203', -0.1, 0.1, 0.001),
    #     # 'dy203': hp.uniform('dy203', -0.1, 0.1, 0.001),
    #     # 'dz203': hp.quniform('dz203', -0.1, 0.1, 0.001),
    #     # 'dtx203': hp.uniform('dtx203', -0.1, 0.1, 0.001),
    #     # 'dty203': hp.uniform('dty203', -0.1, 0.1, 0.001),
    #     # 'dtz203': hp.quniform('dtz203', -0.1, 0.1, 0.001)
    # }
    #
    # trials = hyperopt.Trials()
    #
    # tpe = partial(
    #     hyperopt.tpe.suggest,
    #
    #     # Sample 1000 candidate and select candidate that
    #     # has highest Expected Improvement (EI)
    #     n_EI_candidates=400,
    #
    #     # Use 20% of best observations to estimate next
    #     # set of parameters
    #     gamma=0.2,
    #
    #     # First XX trials are going to be random
    #     n_startup_jobs=200
    # )
    #
    # best = fmin(fn=objective, space=space, algo=tpe, trials=trials, max_evals=1)
    #
    # print("Hyperopt estimated optimum {}".format(best))
