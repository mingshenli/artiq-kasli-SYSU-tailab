# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 21:35:22 2019

@author: 18926
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from gui_window_import.DC_set_import import MainWindow
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

    def dcup1(self):
         s=self.checkBox_DC1.checkState()
         if s==2:
            self.DCUP(1,1)
            self.DCstate_1.setText(str(DCvalue[0]))
    def dcup2(self):
         s=self.checkBox_DC2.checkState()
         if s==2:
            self.DCUP(2,1)
            self.DCstate_2.setText(str(DCvalue[1]))
    def dcup3(self):
         s=self.checkBox_DC3.checkState()
         if s==2:
            self.DCUP(3,1)
            self.DCstate_3.setText(str(DCvalue[2]))
    def dcup4(self):
         s=self.checkBox_DC4.checkState()
         if s==2:
            self.DCUP(4,1)
            self.DCstate_4.setText(str(DCvalue[3]))
    def dcup5(self):
         s=self.checkBox_DC5.checkState()
         if s==2:
            self.DCUP(5,1)
            self.DCstate_5.setText(str(DCvalue[4]))
    def dcup6(self):
         s=self.checkBox_DC6.checkState()
         if s==2:
            self.DCUP(6,1)
            self.DCstate_6.setText(str(DCvalue[5]))
   
    def dcup7(self):
         s=self.checkBox_DC7.checkState()
         if s==2:
            self.DCUP(7,1)
            self.DCstate_7.setText(str(DCvalue[6]))
    def dcup8(self):
         s=self.checkBox_DC8.checkState()
         if s==2:
            self.DCUP(8,1)
            self.DCstate_8.setText(str(DCvalue[7]))
    def dcup9(self):
         s=self.checkBox_DC9.checkState()
         if s==2:
            self.DCUP(9,1)
            self.DCstate_9.setText(str(DCvalue[8]))
    def dcup10(self):
         s=self.checkBox_DC10.checkState()
         if s==2:
            self.DCUP(10,1)
            self.DCstate_10.setText(str(DCvalue[9]))
    def dcup11(self):
         s=self.checkBox_DC11.checkState()
         if s==2:
            self.DCUP(11,1)
            self.DCstate_11.setText(str(DCvalue[10]))
    def dcup12(self):
         s=self.checkBox_DC12.checkState()
         if s==2:
            self.DCUP(12,1)
            self.DCstate_12.setText(str(DCvalue[11]))
    def dcup13(self):
         s=self.checkBox_DC13.checkState()
         if s==2:
            self.DCUP(13,1)
            self.DCstate_13.setText(str(DCvalue[12]))
    def dcup14(self):
         s=self.checkBox_DC14.checkState()
         if s==2:
            self.DCUP(14,1)
            self.DCstate_14.setText(str(DCvalue[13]))
    def dcup15(self):
         s=self.checkBox_DC15.checkState()
         if s==2:
            self.DCUP(15,1)
            self.DCstate_15.setText(str(DCvalue[14]))
    def dcup16(self):
         s=self.checkBox_DC16.checkState()
         if s==2:
            self.DCUP(16,1)
            self.DCstate_16.setText(str(DCvalue[15]))
            
            
    def dcdown1(self):
         s=self.checkBox_DC1.checkState()
         if s==2:
            self.DCUP(1,0)
            self.DCstate_1.setText(str(DCvalue[0]))
    def dcdown2(self):
         s=self.checkBox_DC2.checkState()
         if s==2:
            self.DCUP(2,0)
            self.DCstate_2.setText(str(DCvalue[1]))
    def dcdown3(self):
         s=self.checkBox_DC3.checkState()
         if s==2:
            self.DCUP(3,0)
            self.DCstate_3.setText(str(DCvalue[2]))
    def dcdown4(self):
         s=self.checkBox_DC4.checkState()
         if s==2:
            self.DCUP(4,0)
            self.DCstate_4.setText(str(DCvalue[3]))
    def dcdown5(self):
         s=self.checkBox_DC5.checkState()
         if s==2:
            self.DCUP(5,0)
            self.DCstate_5.setText(str(DCvalue[4]))
    def dcdown6(self):
         s=self.checkBox_DC6.checkState()
         if s==2:
            self.DCUP(6,0)
            self.DCstate_6.setText(str(DCvalue[5]))
   
    def dcdown7(self):
         s=self.checkBox_DC7.checkState()
         if s==2:
            self.DCUP(7,0)
            self.DCstate_7.setText(str(DCvalue[6]))
    def dcdown8(self):
         s=self.checkBox_DC8.checkState()
         if s==2:
            self.DCUP(8,0)
            self.DCstate_8.setText(str(DCvalue[7]))
    def dcdown9(self):
         s=self.checkBox_DC9.checkState()
         if s==2:
            self.DCUP(9,0)
            self.DCstate_9.setText(str(DCvalue[8]))
    def dcdown10(self):
         s=self.checkBox_DC10.checkState()
         if s==2:
            self.DCUP(10,0)
            self.DCstate_10.setText(str(DCvalue[9]))
    def dcdown11(self):
         s=self.checkBox_DC11.checkState()
         if s==2:
            self.DCUP(11,0)
            self.DCstate_11.setText(str(DCvalue[10]))
    def dcdown12(self):
         s=self.checkBox_DC12.checkState()
         if s==2:
            self.DCUP(12,0)
            self.DCstate_12.setText(str(DCvalue[11]))
    def dcdown13(self):
         s=self.checkBox_DC13.checkState()
         if s==2:
            self.DCUP(13,0)
            self.DCstate_13.setText(str(DCvalue[12]))
    def dcdown14(self):
         s=self.checkBox_DC14.checkState()
         if s==2:
            self.DCUP(14,0)
            self.DCstate_14.setText(str(DCvalue[13]))
    def dcdown15(self):
         s=self.checkBox_DC15.checkState()
         if s==2:
            self.DCUP(15,0)
            self.DCstate_15.setText(str(DCvalue[14]))
    def dcdown16(self):
         s=self.checkBox_DC16.checkState()
         if s==2:
            self.DCUP(16,0)
            self.DCstate_16.setText(str(DCvalue[15]))
            
            
    def DC1length(self,int):
        a=int
        DClength[0]=a
        self.textEdit_log.append("set knife1's length to(%s)"%int)
    def DC2length(self,int):
        a=int
        DClength[1]=a
        self.textEdit_log.append("set knife1's length to(%s)"%int)
    def DC3length(self,int):
        a=int
        DClength[2]=a
        self.textEdit_logappend("set knife1's length to(%s)"%int)
    def DC4length(self,int):
        a=int
        DClength[3]=a
        self.textEdit_log.append("set knife1's length to(%s)"%int)
    def DC5length(self,int):
        a=int
        DClength[4]=a
        self.textEdit_log.append("set knife1's length to(%s)"%int)
    def DC6length(self,int):
        a=int
        DClength[5]=a
        self.textEdit_log.append("set knife1's length to(%s)"%int)
    def DC7length(self,int):
        a=int
        DClength[6]=a
        self.textEdit_log.append("set knife1's length to(%s)"%int)
    def DC8length(self,int):
        a=int
        DClength[7]=a
        self.textEdit_log.append("set knife1's length to(%s)"%int)
    def DC9length(self,int):
        a=int
        DClength[8]=a
        self.textEdit_log.append("set knife1's length to(%s)"%int)
    def DC10length(self,int):
        a=int
        DClength[9]=a
        self.textEdit_log.append("set knife1's length to(%s)"%int)
    def DC11length(self,int):
        a=int
        DClength[10]=a
        self.textEdit_log.append("set knife1's length to(%s)"%int)
    def DC12length(self,int):
        a=int
        DClength[11]=a
        self.textEdit_log.append("set knife1's length to(%s)"%int)
    def DC13length(self,int):
        a=int
        DClength[12]=a
        self.textEdit_log.append("set knife1's length to(%s)"%int)
    def DC14length(self,int):
        a=int
        DClength[13]=a
        self.textEdit_log.append("set knife1's length to(%s)"%int)
    def DC15length(self,int):
        a=int
        DClength[14]=a
        self.textEdit_log.append("set knife1's length to(%s)"%int)
    def DC16length(self,int):
        a=int
        DClength[15]=a
        self.textEdit_log.append("set knife1's length to(%s)"%int)
            
    
            
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
    
    def ttlchoose(self,str):
        a=int(str)
        set_timeline[0]=a
       
    def starttime(self,int):
        a=int 
        label=self.comboBox_starttime.currentText()
        set_timeline[2]=label
        if label=='us':
            set_timeline[1]=a    
        if label=='ms':
            set_timeline[1]=a*1000
        if label=='s':
            set_timeline[1]=a*1000000
            
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
            self.textEdit_log.append(e)
            
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a = mainprogram()
    a.show()
    sys.exit(app.exec_()) 