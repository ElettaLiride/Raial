from TPE_opt import *


if __name__=="__main__":

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