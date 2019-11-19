# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 16:50:51 2018

@author: 18926
"""

from artiq.experiment import *
from artiq.protocols.pc_rpc import (Client)
schedule, exps, datasets = [
    Client('::1', 3251, 'master_' + i) for i in 'schedule experiment_db dataset_db'.split()
    ]
class inputtest(EnvExperiment):
    """input_count_test2.1___singal_count"""
    #真正读数的
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
        try:
            self.countt=datasets.get('count_y')
        except:
            self.countt=[]
                
        self.t=1
        ##################################################################选择是否清除循环周期
#        try:
#            self.set_dataset("count_y",[],broadcast=True, save=False)
#            self.set_dataset("count_x",[],broadcast=True, save=False)
#        except:
#            pass
        ##################################################################选择是否清除循环周期
            
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
#        self.core.break_realtime()
        f=0
        i=1
        countt=-1
        
        readtime=30
        delaytime=970
        self.t=readtime+delaytime
        self.set_dataset("count_t",self.t,broadcast=True, save=False)
        with parallel:
#            self.core_dma.playback_handle(pulses_handle)
#            for q in range(2):##################################平行在16口输出脉冲
#                self.ttl16.pulse(2*ms)
#                delay(2*ms)
##            self.ttl16.pulse(10*ns) 
            
            while(i<1000):#控制循环周期，很大时相当于一直开
                try:
                    
                    self.core.reset()
#                    self.core.break_realtime()
                    delay(delaytime*us)#################################################################延时
                    self.ttl1.gate_rising(readtime*us)#################################################读脉冲窗口时间
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
                    
                    print("**********************flow********************************")
        print('fail/total=',f,'/',i)
        print("*************************end*************************")
   
    def setdata(self,count,t):
#        print('________________________')
        self.countt.append(count)
        
        
        self.set_dataset("count_y",self.countt,broadcast=True, save=False)
        














