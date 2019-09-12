# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 16:50:51 2018

@author: 18926
"""

from artiq.experiment import *
import time as t
import math as m
#class A(HasEnvironment):
#    def bulid(self):
#        self.setattr_device("core")
#        self.setattr_device("ttl16")
#        pass
#    @kernel
#    def ttl1on(self):
#        self.ttl16.on()
#        delay(10*ns)
#        self.ttl16.off()
#        delay(10*ns)
from artiq.protocols.pc_rpc import (Client)
schedule, exps, datasets = [
    Client('::1', 3251, 'master_' + i) for i in 'schedule experiment_db dataset_db'.split()
    ]       
class inputtest(EnvExperiment):
    """sig_simulate"""
    def build(self):
        self.setattr_device("core")
        self.setattr_device("core_dma")
        self.setattr_device("ttl16")
        self.setattr_device('scheduler')
        self.setattr_device('ttl1')
        self.setattr_argument("tion", # PMT 采集时间 
            NumberValue(default=0.2, unit='ms', ndecimals=3, step=0.1)) 
        print("set the argument carefuly by open the py document,not through the gui")
        self.pulse=[]
        self.pulse=datasets.get('count_y')
        try:
            self.pulse=datasets.get('count_y')
        except:
            pass
#        self.aa=A(self)
#    @kernel  
#    def record(self):
#        with self.core_dma.record("pulses"):
#            # all RTIO operations now go to the "pulses"
#            # DMA buffer, instead of being executed immediately.
#            for i in range(15):
#                self.ttl16.on()
#                delay(10*ns)
#                self.ttl16.off()
#                delay(10*ns)
##                self.aa.a()


#    @kernel    
#    def run(self): 
#        self.core.reset()
#        self.ttl1.input()
#        self.ttl16.output()
#        self.record()
#        pulses_handle = self.core_dma.get_handle("pulses")
#        self.core.break_realtime()
#
#        i=1
#        
#        with parallel:
##            self.core_dma.playback_handle(pulses_handle)
##            for i in range(10):
##                self.aa.ttl1on()
#            self.ttl16.pulse(10*ns)   
#            while(i>0):
#                try:
#                    delay(100*ms)
#                    self.ttl1.gate_rising(500*ns)
#                    count = float(self.ttl1.count())
##                    delay(1*us)
#                    print("****************************",count,"*********************************")
##                    i=0
#                except RTIOUnderflow:
#                    self.core.break_realtime()
#                    print("**********************flow********************************")
#        print("*************************end*************************")
    def run(self):
                    i=1
                    roundd=0
                   
                   
                    while i!=0 and roundd<100:
                        self.pulse.append(m.sin(roundd))
#                        self.x.append(roundd)
#                        if len(x)!=len(pulse):
#                            print("*******************************************error*********************************************")
#                            print(sin(roundd))
                        roundd+=1
                       
#                        self.set_dataset("count_x",self.x,broadcast=True, save=False)
                        self.set_dataset("count_y",self.pulse,broadcast=True, save=False)
                        t.sleep(0.005)
                    
                        
                    
