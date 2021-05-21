import sys
import pandas as pd
import numpy as np

import ccdb_connector as cc
import parameters_manipulator as pm

if __name__=="__main__":
    calibration_connection = "sqlite:////work/clas12/users/costantini/RICH_alignement/Costantini_script/ccdb_4.3.2.sqlite"
    calibration_table      = '/calibration/rich/misalignments'
    variation              = 'misalignments_test'
    user                   = "Costantini"
    module = [4,201,1]

    provider=cc.connecting_ccdb(calibration_connection)
    pars = cc.reading_ccdb(provider,calibration_table, variation)
    pars = pm.changing_parameters(pars,calibration_table,module[0],module[1],module[2])
    cc.adding_to_ccdb(pars, provider, calibration_table, variation)

    print(pars)
    # ##Reading environment variable
    #
    # MIRAZITAsrc = os.environ()
    # MIRAZITAfil = os.environ()
    #
    # ##executing Mirazita code for filtering
    # if sys.argv[0] == '-f':
    #     subprocess.run([])
    #
    # ##executing Mirazita code for Reconstruction and comparison
    # subprocess.run([])
    #
    # ##execute Costantini code for update ccdb
