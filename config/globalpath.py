import os


RICHGEOAL = os.getenv("RICHGEOAL")

FILTDIR = f'{RICHGEOAL}/output/filter'
PLOTDIR = f'{RICHGEOAL}/output/plots'
RECODIR = f'{RICHGEOAL}/output/reco'
OPTIDIR = f'{RICHGEOAL}/output/opt'
BINDIR = f'{RICHGEOAL}/bin'

RN = 1
ITER = 0
CALIBRATION_TABLE = "/calibration/rich/misalignments"
VARIATION = "subtest"
USER = "Costantini"
CALIBRATION_CONNECTION = os.getenv("CCDB_CONNECTION")