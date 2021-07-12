import sys

from database import tools as t


# executing Mirazita code for drawing
def runcommand(runnumber):
    command = "root -l -p -q mirazita_code/RichAI_plots/DrawRichPlots.C(\"RichPlots_" + runnumber + ".root\")"
    stdout = t.runcommand(command)
    print(stdout[0])


if __name__ == "__main__":
    runcommand(sys.argv[1])
