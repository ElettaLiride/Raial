import os
import pandas as pd



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
USER = "anonymous"
CALIBRATION_CONNECTION = f'sqlite:///{RICHGEOAL}/config/ccdb_4.3.2.sqlite'

STARTING_TABLE = pd.read_table('config/allzero_python.txt', sep='-')
