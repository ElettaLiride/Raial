import sys
import os
from costantini_code import tools as t


# executing Mirazita code for build histogram
def runcommand(filetoread):
    f = os.path.basename(filetoread)
    runnumber = t.getrunnumber(f)

    command = ".//mirazita_code/RichAI_Plots/richPlots" + " -R" + runnumber + " " + f
    stdout = t.runcommand(command)
    print(stdout[0])

    command = "mv RichPlots_" + runnumber + ".out output/plots/"
    stdout = t.runcommand(command)
    command = "mv RichPlots_" + runnumber + ".root output/plots/"
    stdout = t.runcommand(command)


if __name__ == "__main__":
    runcommand(sys.argv[1])