# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:53:25 2018

@author: 18926
"""

from artiq.experiment import *


        
class A(EnvExperiment):
    """timeline_exc_1.0"""
#    global ttlport
#    global starttime
#    global move
#    global length
    
    def build(self):
        # change the "foo" dataset and click the "recompute argument"
        # buttons.
        self.setattr_device("core")
        self.setattr_device("ttl16")
#        self.setattr_device("ttl17")
#        self.setattr_device("ttl18")
#        self.setattr_device("ttl19")
#        self.setattr_device("ttl20")
#        self.setattr_device("ttl21")
#        self.setattr_device("ttl22")
#        self.setattr_device("ttl23")
#        self.setattr_device("ttl24")
#        self.setattr_device("ttl25")
#        self.setattr_device("ttl26")
#        ttlport_temp='1/2/1/2/'
#        starttime_temp='2000000.0/3000000.0/6000000.0/8000000.0/'
#        move_temp='1/1/0/0/'
#        ttlport_temp=self.get_dataset("ttl")
#        starttime_temp=self.get_dataset("starttime")
#        move_temp=self.get_dataset("move")
#        self.ttlport=ttlport_temp.split('/')
#        self.starttime=starttime_temp.split('/')
#        self.move=move_temp.split('/')
#        self.length=len(self.move)-1
#        self.starttime[self.length]=str(float(self.starttime[self.length-1])+1000000)
#        for stp in range(self.length+1):
#            self.starttime[stp]=float(self.starttime[stp])
    
    @kernel
    def run(self):
        
        
#        print(ttlport)
#        print(type(starttime))
#        print(move)
       
       
#        for stp in range(self.length):
#            if self.ttlport[stp]=='1':
#                if self.move[stp]=='1':
#                    self.ex.ttl1on((self.starttime[stp+1])-(self.starttime[stp]))
#                if self.move[stp]=='0':
#                    self.ex.ttl1off((self.starttime[stp+1])-(self.starttime[stp]))
#            if self.ttlport[stp]=='2':
#                if self.move[stp]=='1':
#                    self.ex.ttl2on((self.starttime[stp+1])-(self.starttime[stp]))
#                if self.move[stp]=='0':
#                    self.ex.ttl2off((self.starttime[stp+1])-(self.starttime[stp]))
        
        
        def ttl1on(self):
            self.ttl16.on()
            delay(5000000*us)
        def ttl2on(self):
            self.ttl16.off()
            delay(5000000*us)
        self.core.reset()
        ttl1on(self)
        ttl2on(self)
                
        
       
                    
                    
            
        

        
        
        