import inspect
import subprocess
import os

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


def look_for_check(name, dir="opt/"):
    res = None
    for file in os.listdir(dir):
        if file == name:
            res = load(dir + file)
    return res


def read_check(name, dir="opt/"):
    old = look_for_check(name + '.pkl', dir=dir)
    x_old = None
    y_old = None
    if old is not None:
        x_old = old.x_iters
        y_old = old.func_vals
    return x_old, y_old


