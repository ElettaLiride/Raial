import sys
import os

from src.python import tools as t
from src.python import globalpath


@t.timer
def run_reco(fileIN, fileOUT=None, yaml=globalpath.RICHYAML):

    """
    execute Rich engine for reconstruction of events

    :param fileIN: name of the file with raw data for the reconstruction
    :param fileOUT: output file name of the reconstruction
    :param yaml: yaml file for the configuration of the reconstruction
    :return: None
    """

    f = os.path.basename(fileIN).split('.')[0]

    if fileOUT is None:
        fileOUT = f'{f}_{globalpath.ITER}_{globalpath.RN}.hipo'

    t.runcommand(f"{globalpath.RECOUTIL} -i {fileIN} -o {fileOUT} -y {yaml}", output=globalpath.PRINTreco)
    t.runcommand(f"mv {fileOUT} {globalpath.RECODIR}/")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        run_reco(sys.argv[1])
    else:
        run_reco(sys.argv[1], sys.argv[2])
