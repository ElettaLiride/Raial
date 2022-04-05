from src.python import globalpath, tools
from src.python.ccdb_connection import connecting_ccdb, adding_to_ccdb, reading_ccdb
from src.python.run_reco import runcommand as reco
from src.python.run_plots import runcommand as plots
from src.python.objective import pass_dict_param_to_table


if __name__ == "__main__":
    data_dir = sys.argv[1]
    param = sys.argv[2]

    tools.init_opt(data_dir, )
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