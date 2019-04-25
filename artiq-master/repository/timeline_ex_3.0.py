# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:56:42 2019

@author: 18926
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:53:25 2018

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
        delay(delaytime*ns)
        
    @kernel
    def ttl2on(self,delaytime):
        self.ttl17.on()
        delay(delaytime*ns)
    @kernel
    def ttl3on(self,delaytime):
        self.ttl18.on()
        delay(delaytime*ns)
    @kernel
    def ttl4on(self,delaytime):
        self.ttl19.on()
        delay(delaytime*ns)
    @kernel
    def ttl5on(self,delaytime):
        self.ttl20.on()
        delay(delaytime*ns)

    @kernel
    def ttl1off(self,delaytime):
        self.ttl16.off()
        delay(delaytime*ns)    
    @kernel
    def ttl2off(self,delaytime):
        self.ttl17.off()
        delay(delaytime*ns)
    @kernel
    def ttl3off(self,delaytime):
        self.ttl18.off()
        delay(delaytime*ns)
    @kernel
    def ttl4off(self,delaytime):
        self.ttl19.off()
        delay(delaytime*ns)
    @kernel
    def ttl5off(self,delaytime):
        self.ttl20.off()
        delay(delaytime*ns)
        
class A(EnvExperiment):
    """timeline_exc_3.0"""
    global ttlport
    global starttime
    global move
    global length
    
    def build(self):
        # change the "foo" dataset and click the "recompute argument"
        # buttons.
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
        self.setattr_device('ttl1')
        ttlport_temp='1/2/1/2/'
        starttime_temp='2000.0/3000.0/6000.0/8000.0/'
        move_temp='1/1/0/0/'
        try:
            ttlport_temp=self.get_dataset("ttlport")
            print(ttlport_temp)
            starttime_temp=self.get_dataset("starttime")
            move_temp=self.get_dataset("move")
        except:
            print('unable to get the timeline')
            print('useing the test timeline:ttl16 ttl17')
            ttlport_temp='1/2/1/2/'
            starttime_temp='2000.0/4000.0/9000.0/8000.0/'
            move_temp='1/1/0/0/'
        self.ttlport=ttlport_temp.split('/')
        self.starttime=starttime_temp.split('/')
        self.move=move_temp.split('/')
        self.length=len(self.move)-1
        self.starttime[self.length]=str(float(self.starttime[self.length-1])+100)
        self.ex=B(self)
        for stp in range(self.length+1):
            self.starttime[stp]=float(self.starttime[stp])
    
    @kernel
    def run(self):
        
        
#        print(ttlport)
#        print(type(starttime))
#        print(move)
        print("**************************running**************************")
        
        self.core.reset()
#        self.ttl1.input()
#        self.ttl16.output()
#        self.core.break_realtime()

#        with parallel:
##            with sequential:
##                delay(100*ms)
#            self.ttl1.gate_rising(2*ms)
##            delay(40*ms)
##            count=self.ttl0.count()
        for stp in range(self.length):
                if self.ttlport[stp]=='1':
                    if self.move[stp]=='1':
                        self.ex.ttl1on((self.starttime[stp+1])-(self.starttime[stp]))
                    if self.move[stp]=='0':
                        self.ex.ttl1off((self.starttime[stp+1])-(self.starttime[stp]))
#                break
                if self.ttlport[stp]=='2':
                    if self.move[stp]=='1':
                        self.ex.ttl2on((self.starttime[stp+1])-(self.starttime[stp]))
                    if self.move[stp]=='0':
                        self.ex.ttl2off((self.starttime[stp+1])-(self.starttime[stp]))
                if self.ttlport[stp]=='3':
                    if self.move[stp]=='1':
                        self.ex.ttl3on((self.starttime[stp+1])-(self.starttime[stp]))
                    if self.move[stp]=='0':
                        self.ex.ttl3off((self.starttime[stp+1])-(self.starttime[stp]))
                if self.ttlport[stp]=='4':
                    if self.move[stp]=='1':
                        self.ex.ttl4on((self.starttime[stp+1])-(self.starttime[stp]))
                    if self.move[stp]=='0':
                        self.ex.ttl4off((self.starttime[stp+1])-(self.starttime[stp]))
                if self.ttlport[stp]=='5':
                    if self.move[stp]=='1':
                        self.ex.ttl5on((self.starttime[stp+1])-(self.starttime[stp]))
                    if self.move[stp]=='0':
                        self.ex.ttl5off((self.starttime[stp+1])-(self.starttime[stp]))
           
#        print('************************finish*******************************')
#        count=float(self.ttl1.count())
#        print('*************count:',count)
#        self.ex.ttl1on()
#        self.ex.ttl2on()
#        self.ex.ttl1on(5000000)
#        self.ex.ttl1off(5000000)
                
        
       
                    
                    
            
        

        
        
        