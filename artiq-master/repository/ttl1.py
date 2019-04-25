# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 19:35:36 2018

@author: 18926
"""

from artiq.experiment import *


class B(EnvExperiment):
    '''ttl1'''
    def build(self):
        self.setattr_device("core")
        self.setattr_device("ttl16")
        self.setattr_device("ttl17")
        self.setattr_device("ttl18")
        self.setattr_device("ttl19")
        self.setattr_device("ttl20")
        self.setattr_device("ttl21")
        self.setattr_device("ttl22")
        self.setattr_device("ttl23")
        self.setattr_device("ttl24")
        self.setattr_device("ttl25")
        self.setattr_device("ttl26")
        self.setattr_device("core_dma")
        self.setattr_device('scheduler')
    @kernel  
    def record(self):
        with self.core_dma.record("pulses"):
            # all RTIO operations now go to the "pulses"
            # DMA buffer, instead of being executed immediately.
            for i in range(100):
                self.ttl17.off()
                delay(100*ns)
                self.ttl17.on()
                delay(100*ns)
#                self.aa.a()



    
    @kernel
    def run(self):
        self.core.reset()
#        self.ttl30.output() 
#        for i in range(10000):
#            self.ttl30.on()
#            delay(500*us) 
#            self.ttl30.off()
#            delay(500*us)
        
       
        self.ttl17.output()
        self.record()
        pulses_handle = self.core_dma.get_handle("pulses")
        self.core.break_realtime()
        
#        i=1
#        while i==1:
#        for q in range(100):
#            for i in range(50):    
#                self.ttl16.off()
#                delay(100*ns)
#                self.ttl16.on()
#                delay(100*ns)
#            self.core.break_realtime()
        for i in range(50):    
                self.ttl17.off()
                delay(100*ns)
                self.ttl17.on()
                delay(100*ns)
#        self.core_dma.playback_handle(pulses_handle)
        print('****************************************finish*******************************************')
        self.core.break_realtime()
        self.ttl17.off()    
        
        