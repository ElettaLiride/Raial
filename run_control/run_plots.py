import sys
import os

from run_control import tools as t


def runcommand(filetoread):
    '''

    execute Mirazita code for build histogram and computing differences from expected and
    computed Cherenkov angles for single tile of the Aerogel panel

    :param filetoread:  file to read for the analysis
    :return: None

    '''

    files = ""

    if os.path.isdir(filetoread):
        for file in os.listdir(filetoread):
            if os.path.isfile(filetoread + file):
                files += " "
                files += file
    else:
        files = " " + filetoread
    print(files)
    #runnumber = t.getrunnumber(os.path.basename(filetoread))

    command = "./scoring/RichAI_Plots/richPlots" + " -R2010" + files
    _ = t.runcommand(command)
    # print(stdout[0])

    command = "mv RichPlots_" + "2010" + ".out output/plots/"
    _ = t.runcommand(command)
    command = "mv RichPlots_" + "2010" + ".root output/plots/"
    _ = t.runcommand(command)


if __name__ == "__main__":
    runcommand(sys.argv[1])
