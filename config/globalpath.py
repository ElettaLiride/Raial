import os
import pandas as pd


# important path
RICHGEOAL = os.getenv("RICHGEOAL")

FILTDIR = f'{RICHGEOAL}/output/filter'
PLOTDIR = f'{RICHGEOAL}/output/plots'
RECODIR = f'{RICHGEOAL}/output/reco'
OPTIDIR = f'{RICHGEOAL}/output/opt'
BINDIR = f'{RICHGEOAL}/bin'

if RICHGEOAL.split(sep='/')[1] == 'work':
    RECOUTIL = '/work/clas12/users/devita/rich/oldVersionWithNewGeo/clas12-offline-software/coatjava/bin/recon-util'
else:
    RECOUTIL = 'recon-util'

RICHYAML = f'{RICHGEOAL}/config/rich.yaml'
# calibration connection
CALIBRATION_TABLE = "/calibration/rich/misalignments"
VARIATION = "default"
USER = "anonymous"
CALIBRATION_CONNECTION = f'sqlite:///{RICHGEOAL}/config/ccdb_4.3.2.sqlite'

# optimization run
RN = 1
ITER = 0
STARTING_TABLE = pd.read_table('config/allzero_python.txt', sep='-')
