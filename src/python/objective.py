import os
import numpy as np
import functools

from src.python import parameters_setting as pm, ccdb_connection as cc, run_reco, run_plots
from src.python import globalpath
from src.python import tools


#### OTHER THINGS
def fake_obj(**d):
    change_parameter_given_dir(d)
    df = cc.reading_ccdb()
    print(df)
    print(df.info())


def read_output(string):
    tiles = string.split('Layer')[1:]
    chi = float(str(string).split('Layer')[0].split('chi2=')[1].split('\\')[0])
    val = [float(tile.split('dEtaC=')[1].split('\\')[0]) for tile in tiles]
    layer = [float(tile.split()[0]) for tile in tiles]
    t = [float(tile.split()[2]) for tile in tiles]
    nice_output = np.asarray([layer, t, val])

    return nice_output, chi


def pass_dict_param_to_table(par_dict, table):
    for layer, val in par_dict.items():
        module = [4, int(layer.split('_')[1]), 0]
        pars = [layer.split('_')[0], val]
        pm.changing_one_parameter(table, module, pars)

    return table


def change_parameter_given_dir(params):
    # CHANGING PARAM ON CCDB
    new_table = pass_dict_param_to_table(params, globalpath.STARTING_TABLE)
    #to_add = new_table.values.tolist()
    to_add = list(map(list, new_table.itertuples(index=False)))
    cc.adding_to_ccdb(to_add, comment=f'iteration {globalpath.ITER}')


### MAIN
def main_obj(**params):
    """

    :param space:
    :param names:
    :return:
    """
    #UPDATE ITARATION NUMBER
    globalpath.ITER = globalpath.ITER + 1
    # CHANGING PARAM ON CCDB
    change_parameter_given_dir(params)

    # RUN EVENTBUILDER
    for file in os.listdir(globalpath.FILTDIR):
        if os.path.isfile(f'{globalpath.FILTDIR}/{file}'):
            run_reco.run_reco(f'{globalpath.FILTDIR}/{file}')
    # RUN ANGLE ANALYSIS
    run_plots.run_plot(globalpath.RECODIR)


def applyscore(func):
    """Apply the score to the main objective"""
    @functools.wraps(func)
    def wrapper_score(*args, **kwargs):
        main_obj(**kwargs)
        value = func()
        return value
    return wrapper_score


#### SCORING
def runthescore(datadir):
    tools.init_opt(datadir, 'test', globalpath.RN)
    for file in os.listdir(globalpath.FILTDIR):
        if os.path.isfile(f'{globalpath.FILTDIR}/{file}'):
            run_reco.run_reco(f'{globalpath.FILTDIR}/{file}')
    # RUN ANGLE ANALYSIS
    run_plots.run_plot(globalpath.RECODIR)


@applyscore
def minimize_chi():
    file = f'{globalpath.PLOTDIR}/result_{globalpath.RN}_{globalpath.ITER}.out'
    f = open(file, "r")
    lines = f.readlines()
    chi2 = abs(float(lines[0].split()[-1].split('=')[-1]))

    return chi2


@applyscore
def minimize_chi_and_diff():
    file = f'{globalpath.PLOTDIR}/result_{globalpath.RN}_{globalpath.ITER}.out'
    f = open(file, "r")
    nline = 0
    mean = 0
    chi2 = 0
    lines = f.readlines()

    for line in lines:
        if nline == 0:
            chi2 = abs(float(line.split()[-1].split('=')[-1]))
        else:
            mean = mean + abs(float(line.split()[-1].split('=')[-1]))
        nline = nline + 1
    f.close()

    mean = mean / (nline - 1)
    mean = np.exp(-1/mean) + chi2

    return mean


@applyscore
def minimize_mean_diff():
    file = f'{globalpath.PLOTDIR}/result_{globalpath.RN}_{globalpath.ITER}.out'
    f = open(file, "r")
    nline = 0
    mean = 0
    lines = f.readlines()

    for line in lines:
        if nline == 0:
            continue
        else:
            mean = mean + abs(float(line.split()[-1].split('=')[-1]))
        nline = nline + 1
    f.close()

    mean = mean / (nline - 1)
    mean = 1 - np.exp(mean)

    return mean



if __name__ == "__main__":
    import sys
    runthescore(sys.argv[1])

