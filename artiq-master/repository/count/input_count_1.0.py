# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 11:08:37 2018

@author: 18926
"""

from artiq.experiment import *
class inputtest(EnvExperiment):
    """input_count_test1.0___singal_count"""
    def build(self):
        self.setattr_device("core")
        self.setattr_device('scheduler')
        self.setattr_device('ttl1')
        self.setattr_argument("tion", # PMT 采集时间 
            NumberValue(default=0.2, unit='ms', ndecimals=3, step=0.1)) 
        print("set the argument carefuly by open the py document,not through the gui")
    @kernel    
    def run(self): 
        self.core.reset()
        self.ttl1.input()
        i=1
        stop=20
        roundtime=0
        while(stop!=roundtime):
            roundtime+=1
            delay(100*ms)
            try:
                
                self.ttl1.gate_rising(1000*ns)
                count = float(self.ttl1.count())
                delay(1*us)
                print("****************************",count,"*********************************")
                i=0
            except RTIOUnderflow:
                self.core.break_realtime()
                print("**********************flow********************************")

    
    