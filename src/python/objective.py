import os
import numpy as np

from src.python import parameters_setting as pm, ccdb_connection as cc
from scripts import run_plots
from scripts import run_reco

RICHGEOAL = os.path.basename("RICHGEOAL")

filterdir = RICHGEOAL + "/output/filter/"
plotdir = RICHGEOAL + "/output/plots/"
recodir = RICHGEOAL + "/output/reco/"

calibration_connection = "sqlite:///" + RICHGEOAL + "/database/ccdb_4.3.2.sqlite"
calibration_table = "/calibration/rich/misalignments"
variation = "default"
user = "Costantini"


def read_output(string):
    tiles = string.split('Layer')[1:]
    chi = float(str(string).split('Layer')[0].split('chi2=')[1].split('\\')[0])
    val = [float(tile.split('dEtaC=')[1].split('\\')[0]) for tile in tiles]
    layer = [float(tile.split()[0]) for tile in tiles]
    t = [float(tile.split()[2]) for tile in tiles]
    nice_output = np.asarray([layer, t, val])

    return nice_output, chi


def compute_score(nice_output, chi):
    return sum([abs(el) for el in nice_output]) / len(nice_output) + chi


def make_mean_plus_chi2(file):
    f = open(file, "r")
    nline = 0
    mean = 0
    chi2 = 0
    lines = f.readlines()

    for line in lines:
        if nline==1:
            chi2 = abs(float(line.split()[-1].split('=')[-1]))

        mean = mean + abs(float(line.split()[-1].split('=')[-1]))
        nline+=1
    mean = mean/(nline-1) + chi2
    f.close()
    return mean


def make_mean_all(file):
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


def pass_dict_param_to_table(par_dict, table):
    for layer, val in par_dict.items():
        module = [4, int(layer.split('_')[1]), 0]
        pars = [layer.split('_')[0], val]
        pm.changing_one_parameter(table, module, pars)

    return table


def obj_gp(space, names, RN):
    """

    :param space:
    :param names:
    :return:
    """
    global recodir, plotdir, calibration_table, calibration_connection, variation, user
    filefromplot = "RichPlots_" + RN + ".out"

    my_provider = cc.connecting_ccdb(calibration_connection, variation)

    params = {names[i]: space[i] for i in range(len(space))}

    # CHANGING PARAM ON CCDB
    old_pars_table = cc.reading_ccdb(my_provider, calibration_table, variation)
    new_table = pass_dict_param_to_table(params, old_pars_table)
    to_add = new_table.values.tolist()
    cc.adding_to_ccdb(to_add, my_provider, calibration_table, variation)

    # start_time = time.time()
    # RUN EVENTBUILDER
    print("-----------------------------------------------------------------------------------------------")
    print("----------------------------------- START RECO ------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------")

    for file in os.listdir(filterdir):
        if os.path.isfile(filterdir + file):
            run_reco.runcommand(filterdir + file)
        else:
            run_reco.runcommand(filterdir)

    # reco_time = int(time.time() - start_time)
    # second_time = time.time()

    # RUN ANGLE ANALYSIS
    print("-----------------------------------------------------------------------------------------------")
    print("----------------------------------- START PLOTTING --------------------------------------------")
    print("-----------------------------------------------------------------------------------------------")

    _ = run_plots.runcommand(recodir, RN)
    # plot_time = int(time.time() - second_time)

    # SCORING

    obj_score = make_mean_plus_chi2(filefromplot)

    # , reco_time, plot_time
    print("score: ", obj_score)
    return obj_score
