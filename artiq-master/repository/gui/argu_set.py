# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 08:44:09 2018

@author: 18926
"""
from artiq.experiment import *
class argu_set(HasEnvironment):
    """argu_set,as a sub of timeline's gui"""
    def build(self):
         self.setattr_argument("ttlport_", StringValue("ttl"))
         self.setattr_argument("starttime_", StringValue("starttime"))
         self.setattr_argument("move_", StringValue("move"))
#        pass
    def settime(self):
        print('wohaaaaaaaaaaaaaaaaaaaaaaaaaaa'+self.ttlport_)
        print('wohaaaaaaaaaaaaaaaaaaaaaaaaa'+self.starttime_)
        print('wohaaaaaaaaaaaaaaaaaaaaaaaa'+self.move_)
#        self.ttlport_=a
#        self.starttime_=b
#        self.move_=c
#        print(a,b,c)
        self.set_dataset("ttlport",self.ttlport_,broadcast=True, save=False)
        self.set_dataset("starttime",self.starttime_,broadcast=True, save=False)
        self.set_dataset("move",self.move_,broadcast=True, save=False)