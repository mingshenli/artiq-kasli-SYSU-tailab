# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:34:14 2020

@author: TAILAB
"""


import time as t
import random 
import numpy
import os
import sys
from artiq.experiment import *
from artiq.protocols.pc_rpc import (Client)
schedule, exps, datasets = [
    Client('::1', 3251, 'master_' + i) for i in 'schedule experiment_db dataset_db'.split()
    ]
class inputtest(EnvExperiment):
    """input_count_test34___singal_count"""
    #真正读数的
    def build(self):
        self.setattr_device("core")
        self.setattr_device("core_dma")
        self.setattr_device("ttl16")
        self.setattr_device("ttl17")
        self.setattr_device("ttl18")
        self.setattr_device("ttl24")
        self.setattr_device('scheduler')
        self.setattr_device('ttl1')
        self.setattr_device('ttl2')
        self.setattr_argument("roundtime", 
            NumberValue(default=100)) 
        self.setattr_argument("pump_time", 
            NumberValue(default=200)) 
        self.roundtime=int(self.roundtime)
        print('**',self.roundtime)
       
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
        self.ttl17.output()
        self.ttl18.output()
        f=0
        i=1
        countt=-1
        
        readtime=30
        delaytime=970
        self.t=readtime+delaytime
        self.set_dataset("count_t",self.t,broadcast=True, save=False)
        
        count1=1   
        # self.core.reset()
        # self.roundtime=4
        # self.pump_time=5
        for ind in range(self.roundtime):
            self.core.reset()
            
            with parallel:
                with sequential:
                    delay(self.pump_time+1.1*us)
                    count1=self.ttl1.gate_rising(500*us)#################################################读脉冲窗口时间
                    
                    # delay(200*us) 
                    # delay(200*us)
                    # count2=self.ttl2.gate_rising(100*us)
                    # delay(200*us) 
                    
                with sequential:
                    # delay(100*ns)  
                    self.ttl18.on()        #########打开cooling高电平使cooling光关闭
                    
                    self.ttl16.on()         #######打开pump高电平使pump光工作
                    delay(self.pump_time*us)
                    self.ttl16.off()          ##############关闭pump高电平使pump光停止工作
                    
                    delay(1*us)    
                    self.ttl17.on()        ############打开detection高电平使detection光工作
                    delay(500*us)
                    self.ttl17.off()         ##########关闭detection高电平使detection光停止工作
                    
                    
                    delay(100*us)
                    self.ttl18.off()          #########关闭cooling高电平使cooling开启
                    

              
            number1=self.ttl1.count(count1)
            print("****************************1inout",number1,' ind:',ind,"*********************************")
            self.setdata(number1)
            self.core.break_realtime()
        self.savedata()
        print("*************************end*************************")
   
    def setdata(self,count):
#        print('________________________')
        self.countt.append(count)
        # print(self.countt)
        
        
        # self.set_dataset("count_y",self.countt,broadcast=True, save=False)
    def savedata(self):
        print(self.countt)
        
        datasets.set("count_rabi_single",self.countt)
        
        ##################保存数据
        # f=open("D:/artiq-kasli/artiq-master/result_data/data.txt",'a')
        # f.write(str(number1)+"\n")
        # f.close()
        
        
        














