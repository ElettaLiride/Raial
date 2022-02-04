import sys
import functools

from config import globalpath


def tester(func):
    """Print if test is passed or not"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        if func(*args, **kwargs):
            print(f"Test: {func.__name__!r}  passed")
        else:
            print(f"Test: {func.__name__!r} failed")
    return wrapper_timer


@tester
def test_richgoal_onfarm():
    return globalpath.RICHGEOAL == '/work/clas12/users/costantini/Raial'


@tester
def test_ccdbconnection_onfarm():
    return globalpath.CALIBRATION_CONNECTION == '/work/clas12/users/costantini/Raial/config/ccdb_4.3.2.sqlite'


@tester
def test_richgeoal_local():
    return globalpath.RICHGEOAL == '/mnt/c/Users/gcost/Desktop/progetti/Raial'


@tester
def test_ccdbconnection_local():
    return globalpath.CALIBRATION_CONNECTION == 'sqlite:////mnt/c/Users/gcost/Desktop/progetti/Raial/config/ccdb_4.3.2.sqlite'