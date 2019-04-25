# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 17:16:37 2018

@author: 18926
"""



from artiq.experiment import *

class B(HasEnvironment):
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
        pass
    @kernel
    def ttl1on(self,delaytime):
        self.ttl16.on()
        delay(delaytime*ns)           ##############################注意这里测试时把单位改了！！！！！！！！！！！！

    @kernel
    def ttl2on(self,delaytime):
        self.ttl17.on()
        delay(delaytime*us)
    @kernel
    def ttl3on(self,delaytime):
        self.ttl18.on()
        delay(delaytime*us)
    @kernel
    def ttl4on(self,delaytime):
        self.ttl19.on()
        delay(delaytime*us)
    @kernel
    def ttl5on(self,delaytime):
        self.ttl20.on()
        delay(delaytime*us)

    @kernel
    def ttl1off(self,delaytime):
        self.ttl16.off()
        delay(delaytime*ns)    
    @kernel
    def ttl2off(self,delaytime):
        self.ttl17.off()
        delay(delaytime*us)
    @kernel
    def ttl3off(self,delaytime):
        self.ttl18.off()
        delay(delaytime*us)
    @kernel
    def ttl4off(self,delaytime):
        self.ttl19.off()
        delay(delaytime*us)
    @kernel
    def ttl5off(self,delaytime):
        self.ttl20.off()
        delay(delaytime*us)
        
class A(EnvExperiment):
    """timeline_exc_2.1"""
    global ttlport
    global starttime
    global move
    global length
    
    def build(self):
        # change the "foo" dataset and click the "recompute argument"
        # buttons.
        self.setattr_device("core")
        self.setattr_device("core_dma")
        self.setattr_device('scheduler')
        self.setattr_device("ttl0")
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
#        ttlport_temp='1/1/1/1/'
#        starttime_temp='10/10/10/10/'
#        move_temp='1/0/1/0/'
        try:
            ttlport_temp=self.get_dataset("ttlport")
            starttime_temp=self.get_dataset("starttime")
            move_temp=self.get_dataset("move")
        except:
            print('unable to get the timeline')
            ttlport_temp='1/1/1/1/'
            starttime_temp='10000/10000/10000/10000/'
            move_temp='1/0/1/0/'
        print(starttime_temp)
        self.ttlport=ttlport_temp.split('/')
        self.starttime=starttime_temp.split('/')
        self.move=move_temp.split('/')
        self.length=len(self.move)-1
        self.starttime[self.length]=str(float(self.starttime[self.length-1])+1000000)
        self.ex=B(self)
        for stp in range(self.length+1):
            self.starttime[stp]=float(self.starttime[stp])
    
#    @kernel
#    def record(self):
##        self.core.reset()
#        with self.core_dma.record("pulses"):
#            for stp in range(self.length):
#                if self.ttlport[stp]=='1':
#                    if self.move[stp]=='1':
#                        self.ex.ttl1on((self.starttime[stp+1])-(self.starttime[stp]))
#                    if self.move[stp]=='0':
#                        self.ex.ttl1off((self.starttime[stp+1])-(self.starttime[stp]))
#                if self.ttlport[stp]=='2':
#                    if self.move[stp]=='1':
#                        self.ex.ttl2on((self.starttime[stp+1])-(self.starttime[stp]))
#                    if self.move[stp]=='0':
#                        self.ex.ttl2off((self.starttime[stp+1])-(self.starttime[stp]))
#                if self.ttlport[stp]=='3':
#                    if self.move[stp]=='1':
#                        self.ex.ttl3on((self.starttime[stp+1])-(self.starttime[stp]))
#                    if self.move[stp]=='0':
#                        self.ex.ttl3off((self.starttime[stp+1])-(self.starttime[stp]))
#                if self.ttlport[stp]=='4':
#                    if self.move[stp]=='1':
#                        self.ex.ttl4on((self.starttime[stp+1])-(self.starttime[stp]))
#                    if self.move[stp]=='0':
#                        self.ex.ttl4off((self.starttime[stp+1])-(self.starttime[stp]))
#                if self.ttlport[stp]=='5':
#                    if self.move[stp]=='1':
#                        self.ex.ttl5on((self.starttime[stp+1])-(self.starttime[stp]))
#                    if self.move[stp]=='0':
#                        self.ex.ttl5off((self.starttime[stp+1])-(self.starttime[stp]))
       
    @kernel    
    def run(self): 
        self.core.reset()
        self.ttl0.input()
        self.ttl16.output()
#        self.record()
#        pulses_handle = self.core_dma.get_handle("pulses")
        self.core.break_realtime()

        i=1
        
        with parallel:
#            self.core_dma.playback_handle(pulses_handle)
#            for i in range(10):
#                self.aa.ttl1on()
            for i in range(5):
#            with sequential:
                
                self.ex.ttl1on(10) 
                self.ex.ttl1off(10) 
               
            while(i>0):
                try:
#                    delay(40*ms)
                    self.ttl0.gate_rising(3000*ns)
                    count = float(self.ttl0.count())
#                    delay(1*us)
                    print("****************************",count,"*********************************")
                    i=0
                except RTIOUnderflow:
                    self.core.break_realtime()
                    print("**********************flow********************************")

#                    
                    
            
        

        
        
        