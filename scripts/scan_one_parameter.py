"""
    this script scan with constant step on a single or a couple of parameter the objective src/python/objective.
    It choose the right objective function looking at the name of the yaml file. If "ca" or "pb"
    is in the name it takes those funcs, otherwise it chooses the carbon one.
    It looks for checkpoints given the name and if there are not it creates one. Otherwise
    it overwrites the file.

    It takes as input
    1) data direcotory for the score calculation
    2) name of the parameter
    3) minum value of parameter
    4) maximum value of parameter
    5) number of steps

"""
import sys
import time

import numpy as np

from src.python import globalpath
from src.python.tools import init_opt
from src.python.objective import minimize_chi


if __name__ == "__main__":
    if len(sys.argv) < 7:
        print('Not enough input parameter')
        exit
    else:
        data_dir = sys.argv[1]
        param = sys.argv[2]
        min = float(sys.argv[3])
        max = float(sys.argv[4])
        steps = int(sys.argv[5])
        RN = int(sys.argv[6])
        init_opt(data_dir, f'scan_{param}', RN)

        list = np.linspace(min, max, steps)

        for p1 in list:
            d = {param: p1}
            time.sleep(2)
            minimize_chi(d)
