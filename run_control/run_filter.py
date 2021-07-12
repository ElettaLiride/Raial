import sys
import os

from database import tools as t


# executing Mirazita code for filtering
# 3 argument:
# -file to filter
# -layer to filter
# -number of events to read from file (not necessary)
def runcommand(filetofilter, Layer="-1", eventsnumber=" "):
    f = os.path.basename(filetofilter)
    runnumber = t.getrunnumber(f)

    command = "./mirazita_code/RichAI_FilterC/filterHipo -n" + eventsnumber + " -R" + runnumber + " -L" + Layer + " " + filetofilter
    stdout = t.runcommand(command)
    print(stdout[0])

    command = "mv rec_clas_" + runnumber + "_AIskim1.hipo output/filter/rec_clas_" + runnumber + "_AIskim1_" + Layer + ".hipo"
    stdout = t.runcommand(command)

    return runnumber

if __name__ == "__main__":
    if len(sys.argv) == 3:
        nevents = " "
    else:
        nevents = sys.argv[3]
    runcommand(sys.argv[1], sys.argv[2], nevents)
