import sys
import os

from config import globalpath
from src.python import tools as t

RICHGEOAL = os.getenv("RICHGEOAL")

def runcommand(input):
    """

    execute Mirazita code for build histogram and computing differences from expected and
    computed Cherenkov angles for single tile of the Aerogel panel

    :param filetoread:  file to read for the analysis
    :return: None

    """
    files = ""

    if os.path.isdir(input):
        for file in os.listdir(input):
            if os.path.isfile(input + file):
                files += " "
                files += input + file
    else:
       files = " " + input

    _ = t.runcommand(f"{globalpath.BINDIR}/richPlots -R{globalpath.RN} {files}")
    _ = t.runcommand(f"mv RichPlots_{globalpath.RN}.out {globalpath.PLOTDIR}/result_{globalpath.RN}_{globalpath.ITER}.out")
    _ = t.runcommand(f"mv RichPlots_{globalpath.RN}.root {globalpath.PLOTDIR}/result_{globalpath.RN}_{globalpath.ITER}.root")



if __name__ == "__main__":
    _ = runcommand(sys.argv[1], sys.argv[2])
