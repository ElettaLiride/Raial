import sys

import costantini_code.tools as t


# executing Mirazita code for build histogram
def runcommand(filetoread):
    runnumber = t.getrunnumber(filetoread)
    command = ".//mirazita_code/RichAI_Plots/richPlots" + " -R" + runnumber + " " + filetoread
    stdout = t.runcommand(command)
    print(stdout[0])


if __name__ == "__main__":
    runcommand(sys.argv[0])