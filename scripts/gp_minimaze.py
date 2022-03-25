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

from src.python import globalpath

from yaml import load, BaseLoader
from skopt import gp_minimize
from skopt import Space
from skopt.callbacks import CheckpointSaver
from skopt.utils import use_named_args


from src.python.tools import init_opt
from src.python.objective import minimize_chi, obj_chi_and_diff, obj_diff
from src.python.tools import read_check, init_opt, timer, missing_input



if __name__ == "__main__":

    with open(sys.argv[1]) as file:
        inputs = load(file, BaseLoader)

    for key, val in inputs.items():
        missing_input(val, key)

    data_dir = inputs['data_dir']
    yaml_space_file = inputs['space']
    number_of_calls = int(inputs['total_calls'])
    initial_random_calls = int(inputs['random_calls'])
    id_number = inputs['id_number']
    checkpoint_file = inputs['pickle_file']

    init_opt(data_dir, os.path.basename(sys.argv[1]).split('.')[0], id_number)

    x_old, y_old = read_check(checkpoint_file)

    space = list(Space.from_yaml(yaml_space_file))
    dimension = use_named_args(space)
    obj = dimension(minimize_chi)

    checksaver = CheckpointSaver(checkpoint_path='output/opt/' + checkpoint_file + '.pkl', store_objective=False)
    res = gp_minimize(func=obj,
                      dimensions=space,
                      x0=x_old,
                      y0=y_old,
                      n_calls=number_of_calls,
                      n_initial_points=initial_random_calls,
                      callback=[checksaver],
                      acq_optimizer="sampling",
                      initial_point_generator='lhs')

