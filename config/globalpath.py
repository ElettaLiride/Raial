import os
import pandas as pd


# important path
RICHGEOAL = os.getenv("RICHGEOAL")

FILTDIR = f'{RICHGEOAL}/output/filter'
PLOTDIR = f'{RICHGEOAL}/output/plots'
RECODIR = f'{RICHGEOAL}/output/reco'
OPTIDIR = f'{RICHGEOAL}/output/opt'
BINDIR = f'{RICHGEOAL}/bin'

# calibration connection
CALIBRATION_TABLE = "/calibration/rich/misalignments"
VARIATION = "scan_variation_15"
USER = "anonymous"
CALIBRATION_CONNECTION = f'sqlite:///{RICHGEOAL}/config/ccdb_4.3.2.sqlite'

# optimization run
if RICHGEOAL.split(sep='/')[1] == 'mnt':
    RECOUTIL = 'recon-util'
else:
    RECOUTIL = '/work/clas12/users/devita/rich/oldVersionWithNewGeo/clas12-offline-software/coatjava/bin/recon-util'

RN = 1
ITER = 0
STARTING_TABLE = pd.read_table('config/allzero_python.txt', sep='-')
