import os
import pandas as pd


# General configuration
RICHGEOAL = os.getenv("RICHGEOAL")

FILTDIR = f'{RICHGEOAL}/output/filter'
PLOTDIR = f'{RICHGEOAL}/output/plots'
RECODIR = f'{RICHGEOAL}/output/reco'
OPTIDIR = f'{RICHGEOAL}/output/opt'
BINDIR = f'{RICHGEOAL}/bin'

PRINTplot = True
PRINTreco = True

# Reco configuration
RICHYAML = f'{RICHGEOAL}/config/rich.yaml'

if RICHGEOAL.split(sep='/')[1] == 'work':
    RECOUTIL = '/work/clas12/users/devita/rich/oldVersionWithNewGeo/clas12-offline-software/coatjava/bin/recon-util'
else:
    RECOUTIL = 'recon-util'
RICHPLOTBIN = os.getenv('RICHPLOTBIN')

# Calibration connection
CALIBRATION_TABLE = "/calibration/rich/misalignments"
VARIATION = "default"
USER = "anonymous"
CCDBenv = os.getenv('CCDB_CONNECTION')
CALIBRATION_CONNECTION = f'{CCDBenv}'

# Optimization configuration
RN = 1
ITER = 0
STARTING_TABLE = pd.read_table('config/table/python/webccdb_python.txt', sep='-')
