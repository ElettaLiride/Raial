import sys
import functools

from config import globalpath
from src.test.test_util import tester


@tester
def test_richgeoal_onfarm():
    return globalpath.RICHGEOAL == '/work/clas12/users/costantini/Raial'


@tester
def test_ccdbconnection_onfarm():
    return globalpath.CALIBRATION_CONNECTION == 'sqlite:////work/clas12/users/costantini/Raial/config/ccdb_4.3.2.sqlite'


@tester
def test_richgeoal_local():
    return globalpath.RICHGEOAL == '/mnt/c/Users/gcost/Desktop/progetti/Raial'


@tester
def test_ccdbconnection_local():
    return globalpath.CALIBRATION_CONNECTION == 'sqlite:////mnt/c/Users/gcost/Desktop/progetti/Raial/config/ccdb_4.3.2.sqlite'


@tester
def test_reco():
    pass


@tester
def test_plot():
    pass


@tester
def test_obj_chi2():
    pass



if __name__=="__main__":
    test_richgeoal_onfarm()
    test_ccdbconnection_onfarm()
