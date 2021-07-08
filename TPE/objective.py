from TPE_opt import *


if __name__=="__main__":
    filterdir = "output/filter/"
    plotdir = "output/plots/"
    recodir = "output/reco/"
    fileforreco = filterdir + "rec_clas_5206_AIskim1_-1.hipo"
    fileforplot = recodir + "rec_clas_5206_AIskim1_-1.hipo"
    filefromplot = plotdir + "RichPlots_5206.out"
    calibration_connection = "sqlite:///../ccdb_4.3.2.sqlite"
    calibration_table = "/calibration/rich/misalignments"
    variation = "misalignments"
    user = "Costantini"

    provider = cc.connecting_ccdb(calibration_connection, variation)
    space = {
        'dx_401': 0.,
        'dy_401': 0.,
        'dz_401': 0.,
        'dthx_401': 0.,
        'dthy_401': 0.,
        'dthz_401': 0.,
        'dx_201': 0.,
        'dy_201': 0.,
        'dz_201': 0.,
        'dthx_201': 0.,
        'dthy_201': 0.,
        'dthz_201': 0.,
        'dx_202': 0.,
        'dy_202': 0.,
        'dz_202': 0.,
        'dthx_202': 0.,
        'dthy_202': 0.,
        'dthz_202': 0.
    }

    score=objective(space)
    print("SCORE: ", score)