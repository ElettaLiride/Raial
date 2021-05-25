import sys

from costantini_code import tools as t
from costantini_code import ccdb_connection


# executing Mirazita code for build histogram
def runcommand(filetoread):
    runnumber = t.getrunnumber(filetoread)
    command = ".//mirazita_code/RichAI_Plots/richPlots" + " -R" + runnumber + " " + filetoread
    stdout = t.runcommand(command)
    print(stdout[0])


if __name__ == "__main__":
    runcommand(sys.argv[0], sys.argv[1])