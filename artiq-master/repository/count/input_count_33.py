# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:19:50 2020

@author: 18926
"""

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
import time as t
import random 
from artiq.experiment import *
from artiq.protocols.pc_rpc import (Client)
schedule, exps, datasets = [
    Client('::1', 3251, 'master_' + i) for i in 'schedule experiment_db dataset_db'.split()
    ]
class inputtest(EnvExperiment):
    """input_count_test32___singal_count_simulator"""
    #真正读数的
    def build(self):
        self.setattr_device("core")
        self.setattr_device("core_dma")
        self.setattr_device("ttl16")
        self.setattr_device("ttl17")
        self.setattr_device('scheduler')
        self.setattr_device('ttl1')
        self.setattr_device('ttl2')

        print("set the argument carefuly by open the py document,not through the gui")

        self.t=1
        self.count_previous=[]
        try:
            self.count_previous=datasets.get("count_y")
            
        except:
            print("no init")
            return
                
        
        


    @kernel      ##机箱代码添加此修饰 
    def run(self):
        self.core.reset()
        self.ttl1.input()
        
        readtime=10
        delaytime=990
        self.t=readtime+delaytime
        self.set_dataset("count_t",self.t,broadcast=True, save=False)
        

        self.core.reset()
        delay(200*us)
        count1=self.ttl1.gate_rising(1000*us)#################################################读脉冲窗口时间
                
#        delay(200*us) 
#        delay(200*us)
#        count2=self.ttl2.gate_rising(100*us)
#        delay(200*us) 
                

        number1=self.ttl1.count(count1)
#        number2=self.ttl2.count(count2)
        print("****************************1inout",number1,"*********************************")
#        print("****************************2input",number2,"*********************************")
        print("*************************end*************************")

        data_now=number1
        self.setdata(data_now)
        
        
    def setdata(self,data_now):
        self.count_previous.append(data_now)
        data=self.count_previous
        self.set_dataset("count_y",data,broadcast=True, save=False)
        
        
       
   
    













