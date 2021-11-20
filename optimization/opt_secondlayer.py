from skopt import Space

from bo_gp import BoRichGp
from objective import obj_gp

if __name__=="__main__":
    SPACE = Space.from_yaml('SPM+202.yaml')
    opt = BoRichGp(obj=obj_gp, space=SPACE, dir='../output/opt', id='layerone')
    opt.optimize(call=20)