# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:36:46 2019

@author: 18926
"""
import serial as s
class hardwarelist(object):
    def __init__(self):
        self.hardware={'DC_16chan':['DC1','DC2','DC3','DC4','DC5','DC6','DC7','DC8','DC9','DC10','DC11','DC12','DC13','DC14','DC15','DC16'],
                       'SG382':['sinwave']}
        
class dc_16chan(object):
    def __init__(self):
 
        for i in range(1,17):
            setattr(self,'DC'+str(i),self.generateDC(i))
    def generateDC(self,port):
        def func(voltage):
            self.sendorder(port,voltage)
            return([port,voltage])
        return func
    def te(self):
        print('***')
        return 'wohahaha'

    
    def sendorder(self,port,v):
        print('port:',port,'  V',v)
        hardware='HV176'
        if port<10:
            CH='CH0'+str(port)
        else:
            CH='CH'+str(port)
        V=0.500000+v/14*0.500000
        if V>=1.000000 or V<0:
            self.textEdit_log.append('wrong voltage')
            return
        V=round(V,6)
        V_str='%.6f'%V
        order=hardware+' '+CH+' '+V_str+'\r'
        print(order)
        r=s.Serial()
        r.port='COM11'
        r.baudrate=115200
        try:
            r.open()
            r.write(order.encode())
            r.close()
        except Exception as e:
           # self.textEdit_log.append('suppose to output'+str(order))
            #self.textEdit_log.append(str(e))
            print('no connect to hardware:suppose to output'+str(order))
            
            
if __name__=="__main__":
    DC=dc_16chan()
    DC.DC1(3)