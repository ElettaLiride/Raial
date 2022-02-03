from src.python.ccdb_connection import connecting_ccdb, adding_to_ccdb, reading_ccdb
from src.python.run_reco import runcommand as reco
from src.python.run_plots import runcommand as plots
from src.python.objective import pass_dict_param_to_table

path_to_ccdb = "sqlite:////mnt/c/Users/gcost/Desktop/progetti/Raial/config/ccdb_4.3.2.sqlite"
calibration_table = "/calibration/rich/misalignments"
fileforreco1 = 'output/filter/rec_clas_5206_AIskim1.hipo'
fileforreco2 = 'output/filter/rec_clas_5424_AIskim1.hipo'
dirforplot='output/reco/'
variation = "subtest"
comment = 'test changin one par from realtime ccdb value'
N = 10
par_to_change = 'dz_201'


if __name__ == "__main__":
    prov = connecting_ccdb(path_to_ccdb, variation)
    table = reading_ccdb(prov, calibration_table, variation)

    for i in range(N+1):
        value = -4. + float(8*i/N)
        dict = {par_to_change: value}
        temp = pass_dict_param_to_table(dict, table)
        to_add = temp.values.tolist()
        adding_to_ccdb(to_add, prov, calibration_table, variation, comment)
        reco(fileforreco1)
        reco(fileforreco2)
        plots(dirforplot, f'1000{i}')