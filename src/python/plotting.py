import pandas as pd
from matplotlib import pyplot as plt
import os

def read_from_plotresult(file):
    """
    read plotting txt output file and gives back a float and a pandas dataframe with layer, tile, delta columns

    :param file: path of the file name
    :return: chi2 (float) deltas (pd.Dataframe)

    """
    rows = []
    chi2 = None

    f = open(file, "r")
    lines = f.readlines()
    for nline, line in enumerate(lines):
        if nline==0:
            chi2 = abs(float(line.split()[-1].split('=')[-1]))
        else:
            delta = float(line.split()[-1].split('=')[-1])
            layer = float(line.split()[1])
            tile = float(line.split()[3])
            rows.append([layer, tile, delta])
        nline = nline + 1
    f.close()

    deltas = pd.DataFrame(rows, columns=['layer', 'tile', 'delta'])

    return chi2, deltas


def plot_tiles_changing(list_for_x_axis, list_of_file):
    chi2plot = []
    deltaplot = []

    for f in list_of_file:
        chi2, deltas = read_from_plotresult(f)
        chi2plot.append(chi2)
        deltaplot.append(deltas)

    for tile in deltaplot[0].tile:
        temp = []
        for f in deltaplot:
            temp.append(f.delta[f.tile == tile].values[0])

        plt.scatter(list_for_x_axis, temp)
        plt.title(f'tile {tile}')
        plt.savefig(f'tile_{tile}.png')

if __name__=="__main__":

    files = []
    for file in os.listdir('output/plots'):
        if 'rich_10' in file and 'out' in file:
            file = 'output/plots/' + file
            files.append(file)

    files.append(files[2])
    files.remove('output/plots/rich_100010.out')

    x = [-4, -3.2, -2.4, -1.6, -0.8, 0, 0.8, 1.6, 2.4, 3.2, 4]
    plot_tiles_changing(x, files)