import numpy as np
import time
import os
import re

import matplotlib.pyplot as plt

#from joblib import Parallel, delayed

from skopt.plots import plot_objective, plot_convergence, plot_evaluations
from skopt import  Optimizer
from skopt import Space
from skopt import dump, load

from objective import obj_gp

np.random.seed(1234)

class BoRichGp:
    def __init__(self, obj, space, dir='.', n_call=10, id="test"):
        """
        Class for applying bayesian optimization.

        :param obj:
        :param space:
        :param dir:
        :param n_call:
        :param id:

        """
        self.obj = obj
        self.dir = dir
        self.n_call = n_call
        self.space = space
        self.id = id
        self.res = None

        self.opt = Optimizer(space, "GP",
                             n_initial_points=3,
                             acq_optimizer="sampling",
                             initial_point_generator='lhs')

        if not os.path.isdir(self.dir):
            _, _ = runcommand('mkdir ' + dir)

    def optimize(self, keep=True, call=None):
        """
        make a optimization cicle. If keep is true it saves avery step in a checkpoint file. If Call is given
        it modified n_call in order to make n call in the cicle. Before optimizing it check if there is already a
        checkpoint with the same id and if there is, it load it.

        :param keep: bool for saving the cicle
        :param call: int number of call in the cicle
        :return:
        """

        if call is not None:
            self.n_call = call
        else:
            ex = ValueError()
            ex.strerror = 'No number of call given'
            raise ex

        old, file, number = self._chek_last_checkpoint()
        if old:
            self.load_last_checkpoint(file)

        start = time.time()
        for i in range(int(self.n_call)):
            x = self.opt.ask()
            y = self.obj(x, self.space.dimension_names)
            self.opt.tell(x, y)
            if keep:
                dump(self.opt.get_result(), self.dir + '/' + f'checkpoint_{self.id}_{number}')
        stop = time.time()
        print(f'time spent for {self.n_call} calls of {self.id}: ', stop-start, ' seconds')
        self.res = self.opt.get_result()

    def init_optimizer(self, arg):
        self.opt = Optimizer(**arg)

    def plot_conv(self):
        _ = plot_convergence(self.res)
        plt.savefig(self.dir + '/' + f'conv_{self.id}.png')
        plt.show()

    def plot_depend(self):
        _ = plot_objective(self.res)
        plt.savefig(self.dir + '/' + f'obj_{self.id}.png')
        plt.show()

    def plot_eval(self):
        _ = plot_evaluations(self.res)
        plt.savefig(self.dir + '/' + f'eval_{self.id}.png')
        plt.show()

    def load_last_checkpoint(self, file_name):
        res = load(self.dir + '/' + file_name)
        self.opt.Xi = res.x_iters
        self.opt.Yi = res.func_vals

    def read_last_checkpoint(self, file_name):
        self.res = load(self.dir + '/' + file_name)
        return self.res

    def _chek_last_checkpoint(self):
        file_number = 0
        check = False
        file_name = ""
        regex = re.compile(r'\d+')

        for file in os.listdir(self.dir):
            if ('checkpoint_' + self.id) in file:
                cur_file_number = int(regex.findall(file)[0])
                if cur_file_number >= file_number:
                    file_number = cur_file_number
                    file_name = file
                check = True

        return check, file_name, file_number + 1

class BoRichGp1:
    def __init__(self, obj, space, dir='.', n_call=10, id="test"):
        self.obj = obj
        self.dir = dir
        self.n_call = n_call
        self.space = space
        self.id = id

        self.opt = Optimizer(space,
                "GP",
                n_initial_points=3,
                acq_optimizer="sampling",
                initial_point_generator='lhs')

    def optimize(self, keep=True):
        old, file, number = self._chek_last_checkpoint()
        if old:
            _ = self.load_last_checkpoint(file)

        start = time.time()
        for i in range(int(self.n_call)):
            x = self.opt.ask()
            y = self.obj(x, self.space.dimension_names)
            self.opt.tell(x, y)
            if keep:
                dump(self.opt.get_result(), self.dir + '/' + f'checkpoint_{self.id}_{number}')
        stop = time.time()
        print(f'time spent for {self.n_call} calls of {self.id}: ', stop-start, ' seconds')


    def plot_conv(self):
        _ = plot_convergence(self.opt.get_result())
        plt.savefig(self.dir + '/' + f'conv_{self.id}.png')
        plt.show()

    def plot_depend(self):
        _ = plot_objective(self.opt.get_result())
        plt.savefig(self.dir + '/' + f'obj_{self.id}.png')
        plt.show()

    def plot_eval(self):
        _ = plot_evaluations(self.opt.get_result())
        plt.savefig(self.dir + '/' + f'eval_{self.id}.png')
        plt.show()

    def load_last_checkpoint(self, file_name):
        res = load(self.dir + '/' + file_name)
        self.opt.Xi = res.x_iters
        self.opt.Yi = res.func_vals

        return res

    def _chek_last_checkpoint(self):
        file_number = 0
        check = False
        file_name = ""
        regex = re.compile(r'\d+')

        for file in os.listdir(self.dir):
            if ('checkpoint_' + self.id) in file:
                cur_file_number = int(regex.findall(file)[0])
                if cur_file_number >= file_number:
                    file_number = cur_file_number
                    file_name = file
                check = True

        return check, file_name, file_number + 1




if __name__=="__main__":

    SPACE = Space.from_yaml('SPM+201.yaml')
    opt = BoRichGp(obj=obj_gp, space=SPACE, dir='output/opt', id='firstlayer', n_call=10)

    opt.optimize()
    opt.plot_conv()

    opt.load_last_checkpoint('checkpoint_namedim_test_3')
    opt.plot_depend()
