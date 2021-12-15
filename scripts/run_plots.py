import sys
import os

from scripts import tools as t

RICHGEOAL = os.path.basename("RICHGEOAL")

def runcommand(filetoread, RN):
    """

    execute Mirazita code for build histogram and computing differences from expected and
    computed Cherenkov angles for single tile of the Aerogel panel

    :param filetoread:  file to read for the analysis
    :return: None

    """

    global RICHGEOAL
    files = ""

    if os.path.isdir(filetoread):
        for file in os.listdir(filetoread):
            if os.path.isfile(filetoread + file):
                files += " "
                files += filetoread + file
    else:
       files = " " + filetoread

    command = RICHGEOAL + "/scoring/RichAI_Plots/richPlots" + " -R" + RN + " " + files
    output, err = t.runcommand(command)

    command = "mv RichPlots_" + RN + ".out " + RICHGEOAL + "/" + RN + "/output/plots/"
    _ = t.runcommand(command)
    command = "mv RichPlots_" + RN + ".root " + RICHGEOAL + "/" + RN + "/output/plots/"
    _ = t.runcommand(command)
    return str(output)


if __name__ == "__main__":
    _ = runcommand(sys.argv[1])
