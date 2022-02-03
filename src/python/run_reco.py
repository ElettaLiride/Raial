import sys
import os

from src.python import tools as t

RICHGEOAL = os.getenv("RICHGEOAL")

def runcommand(fileIN, fileOUT=None, yaml="config/rich.yaml"):
    '''

    execute Rich engine for reconstruction of events

    :param fileIN: name of the file with raw data for the reconstruction
    :param fileOUT: output file name of the reconstruction
    :param yaml: yaml file for the configuration of the reconstruction
    :return: None

    '''

    f = os.path.basename(fileIN)

    if fileOUT is None:
        fileOUT = "reco_" + f

    command = "recon-util -i " + fileIN + " -o " + fileOUT + " -y " + yaml
    _ = t.runcommand(command)
    command = "mv " + fileOUT + " " + RICHGEOAL + "/output/reco/"
    _ = t.runcommand(command)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        runcommand(sys.argv[1])
    else:
        runcommand(sys.argv[1], sys.argv[2])
