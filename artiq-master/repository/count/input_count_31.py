# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 12:51:12 2020

@author: 18926
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 12:25:50 2020

@author: 18926
"""

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
    """input_count_test31___singal_count"""
    #真正读数的
    def build(self):
        self.setattr_device("core")
        self.setattr_device("core_dma")
        self.setattr_device("ttl16")
        self.setattr_device("ttl17")
        self.setattr_device('scheduler')
        self.setattr_device('ttl1')
        self.setattr_device('ttl2')
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
        
           
        self.core.reset()
        with parallel:
            with sequential:
                delay(200*us)
                self.ttl1.gate_rising(5000*ns)#################################################读脉冲窗口时间
                delay(200*us) 
                delay(200*us)
                self.ttl2.gate_rising(100*us)#################################################读脉冲窗口时间
                delay(200*us) 
                
            with sequential:
                delay(20*us)    
                self.ttl16.on()
                delay(20000000*us)
        #        self.ttl16.off()
       #        delay(20*us)
         
                delay(20*us)    
                self.ttl17.on()
                delay(20*us)
                self.ttl17.off()
                delay(20*us)
                self.ttl16.off()
     
        count1=((self.ttl1.count()))
        count2=((self.ttl2.count()))
        print("****************************1inout",count1,"*********************************")
        print("****************************2input",count2,"*********************************")
        print("*************************end*************************")
   
    def setdata(self,count,t):
#        print('________________________')
        self.countt.append(count)
        
        
        self.set_dataset("count_y",self.countt,broadcast=True, save=False)
        














