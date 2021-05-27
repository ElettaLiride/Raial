import sys

from costantini_code import tools as t


# executing Mirazita code for filtering
def runcommand(filetofilter, Layer, eventsnumber=" "):
    runnumber = t.getrunnumber(filetofilter)
    command = "./mirazita_code/RichAI_FilterC/filterHipo -n" + eventsnumber + "- R" + runnumber + " -L " + Layer + " " + filetofilter
    stdout = t.runcommand(command)
    print(stdout[0])


if __name__ == "__main__":
    runcommand(sys.argv[0], sys.argv[1], sys.argv[2])
