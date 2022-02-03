import os
import numpy as np

from src.python import parameters_setting as pm, ccdb_connection as cc, run_reco, run_plots

RICHGEOAL = os.getenv("RICHGEOAL")

filterdir = RICHGEOAL + "/output/filter/layer0/"
plotdir = RICHGEOAL + "/output/plots/"
recodir = RICHGEOAL + "/output/reco/"

calibration_connection = "sqlite:///" + RICHGEOAL + "/config/ccdb_4.3.2.sqlite"
calibration_table = "/calibration/rich/misalignments"
variation = "subtest"
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

def minimize_chi(file):
    f = open(file, "r")
    lines = f.readlines()
    chi2 = abs(float(lines[0].split()[-1].split('=')[-1]))

    return abs(1-chi2)

def make_mean_plus_chi2(file):
    f = open(file, "r")
    nline = 0
    mean = 0
    chi2 = 0
    lines = f.readlines()

    for line in lines:
        if nline==0:
            chi2 = abs(float(line.split()[-1].split('=')[-1]))
        else:
            mean = mean + abs(float(line.split()[-1].split('=')[-1]))
        nline = nline + 1
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


def obj_gp(**params):
    """

    :param space:
    :param names:
    :return:
    """

    RN = "10"
    filefromplot = "RichPlots_" + RN + ".out"

    my_provider = cc.connecting_ccdb(calibration_connection, variation)

    # CHANGING PARAM ON CCDB
    old_pars_table = cc.reading_ccdb(my_provider, calibration_table, variation)
    new_table = pass_dict_param_to_table(params, old_pars_table)
    to_add = new_table.values.tolist()
    cc.adding_to_ccdb(to_add, my_provider, calibration_table, variation)

    # RUN EVENTBUILDER
    for file in os.listdir(filterdir):
        if os.path.isfile(filterdir + file):
            run_reco.runcommand(filterdir + file)
    # RUN ANGLE ANALYSIS
    _ = run_plots.runcommand(recodir, RN)
    # SCORING
    #obj_score = make_mean_plus_chi2(filefromplot)
    obj_score = minimize_chi(filefromplot)
    print("score: ", obj_score)
    return obj_score



# print("-----------------------------------------------------------------------------------------------")
# print("----------------------------------- START PLOTTING --------------------------------------------")
# print("-----------------------------------------------------------------------------------------------")
# print("-----------------------------------------------------------------------------------------------")
# print("----------------------------------- START RECO ------------------------------------------------")
# print("-----------------------------------------------------------------------------------------------")

