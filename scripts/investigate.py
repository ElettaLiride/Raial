import sys
from skopt import Space

from objective import obj_gp

from bo_gp import BoRichGp

if __name__ == "__main__":
    SPACE = Space.from_yaml(sys.argv[1])
    opt = BoRichGp(obj=obj_gp, space=SPACE)
    res = opt.read_last_checkpoint(sys.argv[2])

    print(res.x)
    print(res.fun)
    #print(res.nfev)

    opt.plot_conv()
    opt.plot_eval()
    opt.plot_depend()