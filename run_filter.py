import sys

from costantini_code import tools as t


# executing Mirazita code for filtering
def runcommand(filetofilter, Layer, eventsnumber=" "):
    runnumber = t.getrunnumber(filetofilter)
    command = "./mirazita_code/RichAI_FilterC/filterHipo -n" + eventsnumber + "- R" + runnumber + " -L " + Layer + " " + filetofilter
    stdout = t.runcommand(command)
    print(stdout[0])

    command = "mv rec_clas_" + runnumber + "AIskim1.hipo output/filter/"
    stdout = t.runcommand(command)
    command = "mv rec_clas_" + runnumber + "AIskim1_events.out output/filter/"
    stdout = t.runcommand(command)


if __name__ == "__main__":
    runcommand(sys.argv[1], sys.argv[2], sys.argv[3])
