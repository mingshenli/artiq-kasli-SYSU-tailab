# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 08:44:09 2018

@author: 18926
"""
from artiq.experiment import *
class argu_set(EnvExperiment):
    """argu_set"""
    def build(self):
         self.setattr_argument("ttlport_", StringValue("ttl"))
         self.setattr_argument("starttime_", StringValue("starttime"))
         self.setattr_argument("move_", StringValue("move"))
    def run(self):
        print('ttl:'+self.ttlport_)
        print('starttime:'+self.starttime_)
        print('move'+self.move_)
        self.set_dataset("ttlport",self.ttlport_,broadcast=True, save=False)
        self.set_dataset("starttime",self.starttime_,broadcast=True, save=False)
        self.set_dataset("move",self.move_,broadcast=True, save=False)
        
    def dataset(self,ttl,start,move):
        self.set_dataset("ttlport",ttl,broadcast=True, save=False)
        self.set_dataset("starttime",start,broadcast=True, save=False)
        self.set_dataset("move",self.move,broadcast=True, save=False)