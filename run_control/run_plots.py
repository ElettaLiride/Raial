import sys
import os

import tools as t


def runcommand(filetoread):
    '''

    execute Mirazita code for build histogram and computing differences from expected and
    computed Cherenkov angles for single tile of the Aerogel panel

    :param filetoread:  file to read for the analysis
    :return: None

    '''
    runnumber = t.getrunnumber(os.path.basename(filetoread))

    command = "./scoring/RichAI_Plots/richPlots" + " -R" + runnumber + " " + filetoread
    _ = t.runcommand(command)
    # print(stdout[0])

    command = "mv RichPlots_" + runnumber + ".out output/plots/"
    _ = t.runcommand(command)
    command = "mv RichPlots_" + runnumber + ".root output/plots/"
    _ = t.runcommand(command)


if __name__ == "__main__":
    runcommand(sys.argv[1])