import sys
import os

from costantini_code import tools as t


# executing Mirazita code for filtering
def runcommand(fileIN, fileOUT=None, yalm="mirazita_code/RichAI_script/rich.yaml"):
    f = os.path.basename(fileIN)
    if fileOUT == None:
        fileOUT = f
    runnumber = t.getrunnumber(f)


    command = "/work/clas12/users/devita/clas12validation/clara-iss643-rich/plugins/clas12/bin/recon-util -i " + f + " -o " + fileOUT + " -y " + yalm
    stdout = t.runcommand(command)
    print(stdout[0])

    command = "mv " + fileOUT + " output/reco/"
    stdout = t.runcommand(command)


if __name__ == "__main__":
    runcommand(sys.argv[1], sys.argv[2])
