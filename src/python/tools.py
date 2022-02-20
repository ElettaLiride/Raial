import inspect
import subprocess
import os
import functools
import time
import yaml

from skopt.utils import load
from config import globalpath


def line_numb():
    '''Returns the current line number in our program'''
    return inspect.currentframe().f_back.f_lineno


def getrunnumber(file):
    r = file.split("_")[2]
    r = int(r)
    r = str(r)
    return r


def runcommand(bashCommand, output=False, error=True):
    _ = subprocess.run(bashCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #if output:
    #    output, _ = process.communicate()
    #if error:
    #    _, error = process.communicate()
    #return [output, error]


def look_for_check(name, dir="output/opt/"):
    res = None
    for file in os.listdir(dir):
        if file == name:
            res = load(dir + file)
    return res


def read_check(name, dir="output/opt/"):
    old = look_for_check(name + '.pkl', dir=dir)
    x_old = None
    y_old = None
    if old is not None:
        x_old = old.x_iters
        y_old = old.func_vals
    return x_old, y_old


def check_if_dir():
    pass


def mkdir(path):
    if not os.path.exists(path):
        runcommand(f'mkdir {path}')


def change_variation_for_reco(variation):
    with open(globalpath.RICHYAML, 'r') as file:
        code = yaml.load(file, Loader=yaml.FullLoader)

    code['configuration']['services']['RICH']['variation'] = variation

    with open(f'{globalpath.VARIATION}.yml', 'w') as outfile:
        yaml.dump(code, outfile, default_flow_style=False)

    globalpath.RICHYAML = f'{globalpath.VARIATION}.yml'


def init_opt(data_dir, yaml_file_name, RN, variation):
    globalpath.PLOTDIR = f'{globalpath.PLOTDIR}/{yaml_file_name}'
    globalpath.RECODIR = f'{globalpath.RECODIR}/{yaml_file_name}'
    globalpath.FILTDIR = f'{globalpath.FILTDIR}/{data_dir}'

    #change_variation_for_reco(globalpath.VARIATION)
    mkdir(globalpath.RECODIR)
    mkdir(globalpath.PLOTDIR)

    globalpath.RN = RN


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

def save_result(func):
    """decorator for saving result of the function"""
    @functools.wraps(func)
    def wrapper_saver(*args, **kwargs):
        pass
