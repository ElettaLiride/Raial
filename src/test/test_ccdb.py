import pandas as pd

from src.test.test_util import tester

from src.python import ccdb_connection as cc
from src.python.objective import pass_dict_param_to_table
from config import globalpath

@tester
def test_ccdb_adding():

    globalpath.VARIATION = "ccdb_test"
    my_provider = cc.connecting_ccdb(globalpath.CALIBRATION_CONNECTION, globalpath.VARIATION)
    toadd = pd.read_table('config/allzero_python.txt', sep='-').values.tolist()
    cc.adding_to_ccdb(toadd, my_provider, globalpath.CALIBRATION_TABLE, globalpath.VARIATION)
    test_ass = cc.reading_ccdb(my_provider, globalpath.CALIBRATION_TABLE, globalpath.VARIATION)
    test_df = cc.convert_table_in_pd(test_ass)

    return (test_df[test_df.columns[3:]].astype(bool)).sum(axis=0).sum() == 1

@tester
def test_ccdb_reading():
    globalpath.VARIATION = 'misalignments'
    my_provider = cc.connecting_ccdb(globalpath.CALIBRATION_CONNECTION, globalpath.VARIATION)
    test_ass = cc.reading_ccdb(my_provider, globalpath.CALIBRATION_TABLE, globalpath.VARIATION, 9548)
    test_df = cc.convert_table_in_pd(test_ass)
    return not bool((test_df[test_df.columns[3:]].astype(bool)).sum(axis=0).sum())


if __name__ == "__main__":
    test_ccdb_adding()
    test_ccdb_reading()