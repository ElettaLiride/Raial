import pandas as pd

from src.test.test_util import tester

from src.python import ccdb_connection as cc
from src.python.objective import pass_dict_param_to_table
from config import globalpath

@tester
def test_ccdb_adding():
    globalpath.VARIATION = "ccdb_test"
    my_provider = cc.connecting_ccdb(globalpath.CALIBRATION_CONNECTION, globalpath.VARIATION)
    toadd = pd.read_table('config/ccdb_test.txt', sep='-').values.tolist()
    cc.adding_to_ccdb(toadd, my_provider, globalpath.CALIBRATION_TABLE, globalpath.VARIATION)
    test_df = cc.reading_ccdb()

    return test_df['dthx'][7] == 1 and test_df['dy'][0] == 1 and test_df['dx'][7] == 1

@tester
def test_ccdb_reading():
    globalpath.VARIATION = 'ccdb_test'
    test_df = cc.reading_ccdb()
    return test_df['dthx'][7] == 1 and test_df['dy'][0] == 1 and test_df['dx'][7] == 1


if __name__ == "__main__":
#    test_ccdb_adding()
    test_ccdb_reading()
