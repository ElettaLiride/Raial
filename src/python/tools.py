import inspect
import subprocess
import os
import functools
import time

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


def runcommand(bashCommand):
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return [output, error]


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


def mkdir(path):
    _ = runcommand(f'mkdir {path}')

def init_opt(file_name, RN):
    globalpath.PLOTDIR = f'{globalpath.PLOTDIR}/{file_name}'
    globalpath.RECODIR = f'{globalpath.RECODIR}/{file_name}'
    globalpath.FILTDIR = f'{globalpath.FILTDIR}/{file_name}'

    mkdir(globalpath.FILTDIR)
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
