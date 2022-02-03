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
    3) the name of the checkpoint file (optional)

"""

import sys
from matplotlib import pyplot as plt

from skopt import gp_minimize
from skopt import Space
from skopt.plots import plot_convergence
from skopt.callbacks import CheckpointSaver
from skopt.utils import use_named_args
from src.python.objective import obj_gp as obj
from src.python.tools import read_check
from src.python.tools import timer

if __name__ == "__main__":
    yaml_space_file = sys.argv[1]
    number_of_calls = int(sys.argv[2])

    if len(sys.argv) < 4:
        checkpoint_file = 'Test'
    elif len(sys.argv) == 4:
        checkpoint_file = sys.argv[3]
    else:
        print('Too many arguments')
        sys.exit()

    x_old, y_old = read_check(checkpoint_file)

    space = list(Space.from_yaml(yaml_space_file))
    dimension = use_named_args(space)
    obj = dimension(obj)

    gp_minimize = timer(gp_minimize)
    checksaver = CheckpointSaver(checkpoint_path='output/opt/' + checkpoint_file + '.pkl', store_objective=False)
    res = gp_minimize(func=obj,
                      dimensions=space,
                      x0=x_old,
                      y0=y_old,
                      n_calls=number_of_calls,
                      callback=[checksaver],
                      acq_optimizer="sampling",
                      initial_point_generator='lhs')

