from skopt import Space

from optimization.bo_gp import BoRichGp
from optimization.objective import obj_gp

if __name__=="__main__":
    SPACE = Space.from_yaml('SPM+202.yaml')
    opt = BoRichGp(obj=obj_gp, space=SPACE, dir='output/opt', id='layerone', n_call=20)