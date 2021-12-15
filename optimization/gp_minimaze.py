import sys
import time
from matplotlib import pyplot as plt

from skopt import gp_minimize
from skopt import Space
from skopt.plots import plot_convergence
from skopt.callbacks import CheckpointSaver

from optimization.objective import obj_gp as obj
from scripts.tools import read_check

if __name__ == "__main__":

    """
        this script uses gp_minimize to optimize the objective function 
        that are in src/python/objective.
        It choose the right objective function looking at the name of the yaml file. If "ca" or "pb"
        is in the name it takes those funcs, otherwise it chooses the carbon one. 
        It looks for checkpoints given the name and if there are not it creates one. Otherwise
        it overwrites the file.

        It takes as input 
        1) the name of the yaml file for the hyperparameter space
        2) the number of calls for the search
        3) the name of the checkpoint file

    """
    checksaver = CheckpointSaver('opt/' + sys.argv[3] + '.pkl', compress=9)


    s = Space.from_yaml(sys.argv[1])
    x_old, y_old = read_check(sys.argv[3])

    start = time.time()

    res = gp_minimize(func=obj,
                      dimensions=s,
                      x0=x_old,
                      y0=y_old,
                      n_calls=int(sys.argv[2]),
                      callback=[checksaver],
                      acq_optimizer="sampling",
                      initial_point_generator='lhs')

    end = time.time()

    print('time: ', end - start)

    _ = plot_convergence(res)
    plt.show()