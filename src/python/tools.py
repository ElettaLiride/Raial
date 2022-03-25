import inspect
import subprocess
import os
import functools
import time
import yaml

from skopt.utils import load
from src.python import globalpath


def line_numb():
    '''Returns the current line number in our program'''
    return inspect.currentframe().f_back.f_lineno


def runcommand(bashCommand, output=False):
    if output:
        subprocess.run(bashCommand.split())
    else:
        subprocess.run(bashCommand.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


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


def missing_input(inp, key):
    if inp == '':
        print(f'MISSING {key} input')
        exit()


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


def init_opt(data_dir, yaml_file_name, RN):
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


def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug


def save_result(func):
    """decorator for saving result of the function"""
    @functools.wraps(func)
    def wrapper_saver(*args, **kwargs):
        pass
