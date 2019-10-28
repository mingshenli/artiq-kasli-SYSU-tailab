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

class B(object):
#    def build(self):
#        pass
    def __init__(self):
        self.f=open("D:/artiq-kasli/artiq-master/repository/auto_code/output_test02.py","w",encoding="UTF-8-sig")#不知道为什么估计是artiq的机制，不注明路径就被存到result里面了
        for i in range(1,6):
            setattr(self,'ttl'+str(i)+'on',self.generateOn(i+15))
            setattr(self,'ttl'+str(i)+'off',self.generateOff(i+15))
    def generateOn(self,port):
        def func(delaytime):
            self.print5('self.ttl'+str(port)+'.on()')
            self.print5('delay('+str(delaytime)+'*ns)')
        return func
    def generateOff(self,port):
        def func(delaytime):
            self.print5('self.ttl'+str(port)+'.off()')
            self.print5('delay('+str(delaytime)+'*ns)')
        return func
    def initcode(self):
        self.print1('from artiq.experiment import*')
        self.print1('class code(EnvExperiment):')
        self.print2('def build(self):')
        self.print3("self.setattr_device('core')")
        for i in range(6):
            self.print3("self.setattr_device('ttl"+str(i+16)+"')")
        self.print3("self.setattr_device('ttl1')")   
        self.print2('@kernel')
        self.print2('def run(self):')
        self.print3("self.core.reset()")
        self.print3('with parallel:')
#        self.print4('self.ttl1.gate_rising(2*ms)')
        self.print4('with sequential:')
            
    def print1(self,str):
        self.f.write(str+'\n')
#        print(str)
    def print2(self,str):
        self.f.write('    '+str+'\n')
    def print3(self,str):
        self.f.write('        '+str+'\n')
    def print4(self,str):
        self.f.write('            '+str+'\n')
    def print5(self,str):
        self.f.write('                '+str+'\n')
        
#    def ttl1on(self,delaytime):
#        self.ttl16.on()
#        delay(delaytime*ns)
#        
#   
#    
#   
#    def ttl1off(self,delaytime):
#        self.ttl16.off()
#        delay(delaytime*ns)    
#    
        
class A(EnvExperiment):
    """timeline_CodeGenerate"""
    global ttlport
    global starttime
    global move
    global length
    
    def build(self):
        # change the "foo" dataset and click the "recompute argument"
        # buttons.
        self.setattr_device("core")
        self.setattr_device("core_dma")
        self.setattr_device('ttl1')
        ttlport_temp='1/2/1/2/'
        starttime_temp='2000.0/3000.0/6000.0/8000.0/'
        move_temp='1/1/0/0/'
        try:
            ttlport_temp=self.get_dataset("ttlport")
            starttime_temp=self.get_dataset("starttime")
            move_temp=self.get_dataset("move")
            print(ttlport_temp)
        except:
            print('unable to get the timeline')
            print('useing the test timeline:ttl16 ttl17')
            ttlport_temp='1/2/1/2/'
            starttime_temp='2000.0/4000.0/6000.0/8000.0/'
            move_temp='1/1/0/0/'
        self.ttlport=ttlport_temp.split('/')
        self.starttime=starttime_temp.split('/')
        self.move=move_temp.split('/')
        self.length=len(self.move)-1
        self.starttime[self.length]=str(float(self.starttime[self.length-1])+500)
        self.ex=B()
        for stp in range(self.length+1):
            self.starttime[stp]=float(self.starttime[stp])
    
   
    def run(self):
        
        
#        print(ttlport)
#        print(type(starttime))
#        print(move)
       
        
       
#        with parallel:
##            with sequential:
##                delay(100*ms)
#            self.ttl1.gate_rising(2000*ns)
##            delay(40*ms)
##            count=self.ttl0.count()
            self.ex.initcode()
#            for i in range(100):
##                self.ex.ttl1on(10)
##                self.ex.ttl1off(10)
#                getattr(self.ex,'ttl'+str(i%2+1)+'on')(10)
#                getattr(self.ex,'ttl'+str(i%2+1)+'off')(10)
##            return
            for stp in range(self.length):
                if self.ttlport[stp]=='1':
                    if self.move[stp]=='1':
                        self.ex.ttl1on((self.starttime[stp+1])-(self.starttime[stp]))
                    if self.move[stp]=='0':
                        self.ex.ttl1off((self.starttime[stp+1])-(self.starttime[stp]))
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
            self.ex.print3("count=self.ttl1.count()")
            self.ex.print3("self.set_dataset('count',count,broadcast=True, save=False)")
            self.ex.print3("print('*******************',count,'***************************')")
            self.ex.print3("print('finish')")  
            
            self.ex.f.close()  
        
#        self.ex.ttl1on()
#        self.ex.ttl2on()
#        self.ex.ttl1on(5000000)
#        self.ex.ttl1off(5000000)
                
        
       
                    
                    
            
        

        
        
        