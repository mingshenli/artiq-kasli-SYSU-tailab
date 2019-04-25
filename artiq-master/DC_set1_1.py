# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 21:35:22 2019

@author: 18926
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from DC_set_import import MainWindow
import sys,copy
import serial as s 

#from artiq.protocols.pc_rpc import (Client)
#from led import LED

#schedule, exps, datasets = [
#    Client('::1', 3251, 'master_' + i) for i in 'schedule experiment_db dataset_db'.split()
#    ]

class mainprogram(MainWindow):
    global DCvalue 
    global DCcheck
    global set_timeline #ttl/起始时间/终止时间
    global timeline
    global DClength
    DCvalue= [5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00]
    DCcheck=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    DClength=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    
    def __init__(self):
        super().__init__()
        for i in range(1,17):
            setattr(self,'dcup'+str(i),self.generateDC(i,1))
        for i in range(1,17):
            setattr(self,'dcdown'+str(i),self.generateDC(i,0))
        for i in range(1,17):
            setattr(self,'DC'+str(i)+'length',self.generateLen(i))
            
        for i in range(1,17):
            getattr(self,'DCup_'+str(i)).clicked.connect(getattr(self,'dcup'+str(i)))
        for i in range(1,17):
            getattr(self,'DCdown_'+str(i)).clicked.connect(getattr(self,'dcdown'+str(i)))
        for i in range(1,17):
            getattr(self,'doubleSpinBox_'+str(i)).valueChanged.connect(getattr(self,'DC'+str(i)+'length'))
        for i in range(1,17):
            getattr(self,'DCstate_'+str(i)).setText(str(DCvalue[i-1]))
    
        self.DCup_sel.clicked.connect(self.dcup_sel)
        self.DCdown_sel.clicked.connect(self.dcdown_sel)
        self.readall.clicked.connect(self.readallselect)
    def generateDC(self,num,move):
        def func():
            s=getattr(self,'checkBox_DC'+str(num)).checkState()
            if s==2:
                self.DCUP(num,move)
                getattr(self,'DCstate_'+str(num)).setText(str(DCvalue[num-1]))
        return func
    
    def generateLen(self,num):
        def func(int):
            a=int
            DClength[num-1]=a
            getattr(self,'textEdit_log').append('set knife'+str(num)+'s length to(%s)'%int)
        return func
    
            
    def DCUP(self,num,move):
        if move == 1:
          DCvalue[num-1]=DCvalue[num-1]+DClength[num-1]
          DCvalue[num-1]=round(DCvalue[num-1],3)
          self.textEdit_log.append('set DC'+str(num)+' to '+str(DCvalue[num-1])+'V')
          self.sendorder(num,DCvalue[num-1])
        if move == 0:
          DCvalue[num-1]=DCvalue[num-1]-DClength[num-1]
          DCvalue[num-1]=round(DCvalue[num-1],3)
          self.textEdit_log.append('set DC'+str(num)+' to '+str(DCvalue[num-1])+'V')
          self.sendorder(num,DCvalue[num-1])
    def dcup_sel(self):
        self.selectDC(1)
    def dcdown_sel(self):
        self.selectDC(0)
  
    def selectDC(self,move):    
        for i in range(16):
            DCcheck[i]=getattr(self,'checkBox_DC'+str(i+1)).checkState()
        if move ==1:
          for num in range(16):
            if (DCcheck[num]==2):
               DCvalue[num]=DCvalue[num]+DClength[num]
               DCvalue[num]=round(DCvalue[num],3)
               self.textEdit_log.append('set DC'+str(num+1)+' to '+str(DCvalue[num])+'V')
               self.sendorder(num+1,DCvalue[num])#注意这里比上面的num错位了1
        if move ==0:
          for num in range(16):
            if DCcheck[num]==2:
               DCvalue[num]=DCvalue[num]-DClength[num]
               DCvalue[num]=round(DCvalue[num],3)
               self.textEdit_log.append('set DC'+str(num+1)+' to '+str(DCvalue[num])+'V') 
               self.sendorder(num+1,DCvalue[num])
        
        for i in range(16):
            getattr(self,'DCstate_'+str(i+1)).setText(str(DCvalue[i]))

    def readallselect(self):  
        for i in range(16):
           DCcheck[i]=getattr(self,'checkBox_DC'+str(i+1)).checkState()
        DCvalue_temp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in range(16):
           DCvalue_temp[i]=float(getattr(self,'DCstate_'+str(i+1)).text())
        for num in range(0,16):
             if DCcheck[num] == 2:
                 DCvalue[num]=DCvalue_temp[num]
                 self.sendorder(num+1,DCvalue[num])
        self.textEdit_log.append('succeed in reading current DC value at'+str(DCvalue))
    
    
      
    def sendorder(self,port,v):
        print('port:',port,'V',v)
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
            self.textEdit_log.append('suppose to output'+str(order))
            self.textEdit_log.append(str(e))
            
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a = mainprogram()
    a.show()
    sys.exit(app.exec_()) 