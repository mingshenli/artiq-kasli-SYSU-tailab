# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 16:50:51 2018

@author: 18926
"""

from artiq.experiment import *

class inputtest(EnvExperiment):
    """input_count_test2.1___singal_count"""
    def build(self):
        self.setattr_device("core")
        self.setattr_device("core_dma")
        self.setattr_device("ttl16")
        self.setattr_device('scheduler')
        self.setattr_device('ttl1')
#        self.setattr_argument("tion", # PMT 采集时间 
#            NumberValue(default=0.2, unit='ms', ndecimals=3, step=0.1)) 
        print("set the argument carefuly by open the py document,not through the gui")
#        self.aa=A(self)
        self.countt=[]
        self.t=[]
#        print(help([self.ttl1.count]))
#        print(dir([self.ttl16]))
#    @kernel  
#    def record(self):
#        with self.core_dma.record("pulses"):
#            # all RTIO operations now go to the "pulses"
#            # DMA buffer, instead of being executed immediately.
#            for i in range(3000):
#                self.ttl16.on()
#                delay(5*ms)
#                self.ttl16.off()
#                delay(5*ms)
##                self.aa.a()


    @kernel    
    def run(self): 
        self.core.reset()
        self.ttl1.input()
        self.ttl16.output()
#        self.record()
#        pulses_handle = self.core_dma.get_handle("pulses")
        self.core.break_realtime()
        f=0
        i=1
        countt=-1
        with parallel:
#            self.core_dma.playback_handle(pulses_handle)
            for q in range(2):
                self.ttl16.pulse(2*ms)
                delay(2*ms)
#            self.ttl16.pulse(10*ns) 
            
            while(i<2):
                try:
#                    delay(1000*ms)
#                    self.core.reset()
                    self.core.break_realtime()
                    self.ttl1.gate_rising(30*ms)
                    countt=((self.ttl1.count()))
#                    print("****************************",countt,"*********************************")
                    i=i+1
                    self.setdata(countt,i)
                    
                except RTIOUnderflow:
#                    a=self.ttl1.count()
#                    print('error info:',a)
                    self.core.break_realtime()
#                    self.core.reset()
                    i=i+1
                    f+=1
                    self.setdata(-1,i)
                    
#                    print("**********************flow********************************")
        print(f,'/',i)
        print("*************************end*************************")
   
    def setdata(self,count,t):
#        print('________________________')
        self.countt.append(count)
        self.t.append(t)
        self.set_dataset("count_y",self.countt,broadcast=True, save=False)
        self.set_dataset("count_x",self.t,broadcast=True, save=False)














