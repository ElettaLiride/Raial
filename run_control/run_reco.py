import sys
import os

from run_control import tools as t


def runcommand(fileIN, fileOUT=None, yaml="/work/clas12/users/costantini/RICH_alignment/scoring/rich.yaml"):
    '''

    execute Rich engine for reconstruction of events

    :param fileIN: name of the file with raw data for the reconstruction
    :param fileOUT: output file name of the reconstruction
    :param yaml: yaml file for the configuration of the reconstruction
    :return: None

    '''
    f = os.path.basename(fileIN)

    if fileOUT is None:
        fileOUT = f

    #/work/clas12/users/devita/rich/oldVersionWithNewGeo/clas12-offline-software/coatjava/bin/recon-util
    #/cache/clas12/rg-a/production/recon/fall2018/torus-1/pass1/v0/dst/recon
    #command = os.environ['COATJAVA'] + "/bin/recon-util -i " + fileIN + " -o " + fileOUT + " -y " + yaml
    
    command = "/work/clas12/users/devita/rich/oldVersionWithNewGeo/clas12-offline-software/coatjava/bin/recon-util -i " + fileIN + " -o " + fileOUT + " -y " + yaml
    _ = t.runcommand(command)
    # print(stdout[0])

    command = "cp " + fileOUT + " /work/clas12/users/costantini/RICH_alignment/output/reco/"
    _ = t.runcommand(command)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        runcommand(sys.argv[1])
    else:
        runcommand(sys.argv[1], sys.argv[2])
