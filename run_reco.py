import sys

from costantini_code import tools as t
from costantini_code import ccdb_connection


# executing Mirazita code for filtering
def runcommand(fileIN, fileOUT, yalm):
    runnumber = t.getrunnumber(fileIN)
    command = "/work/clas12/users/devita/clas12validation/clara-iss643-rich/plugins/clas12/bin/recon-util -i " + fileIN + " -o " + fileOUT + " -y " + yalm
    stdout = t.runcommand(command)
    print(stdout[0])


if __name__ == "__main__":
    runcommand(sys.argv[0], sys.argv[1], sys.argv[2])