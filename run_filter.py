import sys

from costantini_code import tools as t
from costantini_code import ccdb_connection


# executing Mirazita code for filtering
def runfilter(filetofilter, Layer):
    runnumber = t.getrunnumber(filetofilter)
    command = "./mirazita_code/RichAI_FilterC/filterHipo -R" + runnumber + " -L " + Layer + " " + filetofilter
    stdout = t.runcommand(command)
    print(stdout[0])


if __name__ == "__main__":
    runfilter(sys.argv[0], sys.argv[1])