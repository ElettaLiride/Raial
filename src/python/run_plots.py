import sys
import os
import time

from src.python import tools as t

RICHGEOAL = os.getenv("RICHGEOAL")

def runcommand(filetoread, RN):
    """

    execute Mirazita code for build histogram and computing differences from expected and
    computed Cherenkov angles for single tile of the Aerogel panel

    :param filetoread:  file to read for the analysis
    :return: None

    """
    files = ""

    if os.path.isdir(filetoread):
        for file in os.listdir(filetoread):
            if os.path.isfile(filetoread + file):
                files += " "
                files += filetoread + file
    else:
       files = " " + filetoread

    command = RICHGEOAL + "/bin/richPlots" + " -R" + RN + " " + files
    output, err = t.runcommand(command)
    tim = str(time.time())
    command = "cp RichPlots_" + RN + ".out " + RICHGEOAL + "/output/plots/rich_" + tim + ".out"
    _ = t.runcommand(command)
    command = "cp RichPlots_" + RN + ".root " + RICHGEOAL + "/output/plots/rich_" + tim + ".root"
    _ = t.runcommand(command)
    # command = "mv RichPlots_" + RN + ".root " + RICHGEOAL + "/output/plots/"
    # _ = t.runcommand(command)
    return str(output)


if __name__ == "__main__":
    _ = runcommand(sys.argv[1], sys.argv[2])
