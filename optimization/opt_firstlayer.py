from skopt import Space

from bo_gp import BoRichGp
from objective import obj_gp

if __name__=="__main__":
    SPACE = Space.from_yaml('/work/clas12/users/costantini/RICH_alignment/SPM+201.yaml')
    opt = BoRichGp(obj=obj_gp, space=SPACE, dir='/work/clas12/users/costantini/RICH_alignment/output/opt', id='layerone')
    opt.optimize(call=1)
