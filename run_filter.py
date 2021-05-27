import sys
import os

from costantini_code import tools as t


# executing Mirazita code for filtering
def runcommand(filetofilter, Layer="-1", eventsnumber=" "):
    f = os.path.basename(filetofilter)
    print(f)
    runnumber = t.getrunnumber(f)
    print(runnumber)
    command = "./mirazita_code/RichAI_FilterC/filterHipo -n" + eventsnumber + " -R" + runnumber + " -L" + Layer + " " + filetofilter
    stdout = t.runcommand(command)
    print(stdout[0])

    command = "mv rec_clas_" + runnumber + "_AIskim1.hipo output/filter/"
    stdout = t.runcommand(command)
    command = "mv rec_clas_" + runnumber + "_AIskim1_events.out output/filter/"
    stdout = t.runcommand(command)


if __name__ == "__main__":
    runcommand(sys.argv[1], sys.argv[2], sys.argv[3])
