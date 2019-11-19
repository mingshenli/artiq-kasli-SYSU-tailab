# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 17:36:01 2019

@author: 18926
"""

from artiq.experiment import *
from artiq.protocols.pc_rpc import (Client)
schedule, exps, datasets = [
    Client('::1', 3251, 'master_' + i) for i in 'schedule experiment_db dataset_db'.split()
    ]
class clearfigure(EnvExperiment):
    """clearfigure"""
    def build(self):
        self.setattr_device("core")
#        self.setattr_device("core_dma")
#        self.setattr_device("ttl16")
#        self.setattr_device('scheduler')
#        self.setattr_device('ttl1')
#        self.setattr_argument("tion", # PMT 采集时间 
#            NumberValue(default=0.2, unit='ms', ndecimals=3, step=0.1)) 
        print("set the argument carefuly by open the py document,not through the gui")
#        self.aa=A(self)
        try:
#            self.set_dataset("count_y",[0],broadcast=True, save=False)
            datasets.set("count_y",[0])
        except:
            pass
