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
import os

from config import globalpath

data_dir = sys.argv[1]
yaml_space_file = sys.argv[2]
number_of_calls = int(sys.argv[3])

from src.python.tools import init_opt
init_opt(data_dir, os.path.basename(yaml_space_file).split('.')[0], 1, globalpath.VARIATION)
from src.python.objective import obj_cluster_chi_square, obj_chi_and_diff, obj_diff
from src.python.tools import read_check, init_opt, timer


from skopt import gp_minimize
from skopt import Space
from skopt.callbacks import CheckpointSaver
from skopt.utils import use_named_args


if __name__ == "__main__":

    if len(sys.argv) < 5:
        checkpoint_file = 'tt'
    elif len(sys.argv) == 5:
        checkpoint_file = sys.argv[4]
    else:
        print('Too many arguments')
        sys.exit()

    x_old, y_old = read_check(checkpoint_file)

    space = list(Space.from_yaml(yaml_space_file))
    print(space)
    dimension = use_named_args(space)
    obj = dimension(obj_cluster_chi_square)

    checksaver = CheckpointSaver(checkpoint_path='output/opt/' + checkpoint_file + '.pkl', store_objective=False)
    res = gp_minimize(func=obj,
                      dimensions=space,
                      x0=x_old,
                      y0=y_old,
                      n_calls=number_of_calls,
                      n_initial_points=1,
                      #callback=[checksaver],
                      acq_optimizer="sampling",
                      initial_point_generator='lhs')

