# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 09:36:51 2018

@author: 18926
"""

from artiq.experiment import *


class LED(EnvExperiment):
    '''led02'''
    def build(self):
        self.setattr_device("core")
        self.setattr_device("ttl16")
        

    @kernel
    def run(self):
        def a(self):
             self.ttl16.on()
             delay(3000000*us)
        def b(self):
             self.ttl16.off()
             delay(3000000*us)
        self.core.reset()
        a(self)
        b(self)
        a(self)
        b(self)
   

           
          
           