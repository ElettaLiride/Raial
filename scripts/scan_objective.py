"""
    this script scan with constant step on a single or a couple of parameter the objective src/python/objective.
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
import yaml
from src.python.objective import obj_gp

def fake_obj(**par):
    print(par)

def build_list_from_space(dict, call):
    list = []
    for c in range(call+1):
        list.append(dict['low'] + c*2*dict['high']/call)
    return dict['name'], list

if __name__ == "__main__":
    yaml_space_file = sys.argv[1]
    number_of_calls = int(sys.argv[2])

    file = open(yaml_space_file)
    code = yaml.load(file, Loader=yaml.FullLoader)

    if len(code) == 2:
        par1, list1 = build_list_from_space(code[0]['Real'], number_of_calls)
        par2, list2 = build_list_from_space(code[1]['Real'], number_of_calls)
        for p1 in list1:
            for p2 in list2:
                d = {par1: p1, par2: p2}
                obj_gp(**d)
    else:
        par1, list1 = build_list_from_space(code[0]['Real'], number_of_calls)
        for p1 in list1:
            d = {par1: p1}
            obj_gp(**d)
