import sys

from src.python import tools as t


# executing Mirazita code for drawing
def runcommand(runnumber):
    command = "root -l -p -q src/cpp/DrawRichPlots.C(\"output/plots/RichPlots_" + runnumber + ".root\")"
    stdout = t.runcommand(command)
    print(stdout[0])


if __name__ == "__main__":
    runcommand(sys.argv[1])
