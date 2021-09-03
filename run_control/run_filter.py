import sys
import os
import re
from run_control import tools as t


def runcommand(filetofilter, Layer="-1", eventsnumber=" "):
    '''
    execute Mirazita code for filtering the events of interst for the analysis

    :param filetofilter: file to read
    :param Layer: Aerogel layer to select, default all the layers
    :param eventsnumber: number of events to read in the file, default all the events
    :return:

    '''

    f = os.path.basename(filetofilter)
    regex = re.compile(r'\d+')
    runnumber = str(int(regex.findall(f)[1]))
    # runnumber = t.getrunnumber(f)

    command = "./scoring/RichAI_FilterC/filterHipo -n" + eventsnumber + " -R" + runnumber + " -L" \
              + Layer + " " + filetofilter
    _ = t.runcommand(command)
    # print(stdout[0])

    command = "mv rec_clas_" + runnumber + "_AIskim1.hipo output/filter/rec_clas_" + runnumber \
              + "_AIskim1_" + Layer + ".hipo"
    _ = t.runcommand(command)

    return runnumber


if __name__ == "__main__":
    if len(sys.argv) == 3:
        nevents = " "
    else:
        nevents = sys.argv[3]
    runcommand(sys.argv[1], sys.argv[2], nevents)
