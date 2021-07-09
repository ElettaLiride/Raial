import inspect
import subprocess


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
