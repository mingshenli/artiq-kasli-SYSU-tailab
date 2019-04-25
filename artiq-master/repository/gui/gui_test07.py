# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 15:58:16 2018

@author: 18926
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 18 20:46:45 2018

@author: 18926
"""
from artiq.experiment import *
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow07_import import MainWindow
import sys,copy
import logging
from artiq.protocols.pc_rpc import (Client)
#from artiq.experiment import *
#from led import LED

schedule, exps, datasets = [
    Client('::1', 3251, 'master_' + i) for i in 'schedule experiment_db dataset_db'.split()
    ]

class mainprogram(MainWindow):
    '''gui_test07'''
    global DCvalue 
    global DCcheck
    global set_timeline #ttl/起始时间/终止时间
    global timeline
    global DClength
    DCvalue= [5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00]
    DCcheck=[0,0,0,0,0,0,0,0,0,0,0,0]
    DClength=[0,0,0,0,0,0,0,0,0,0]
    set_timeline=[1,0,'s',0,'s']
    timeline=[[1,0,'s',0,'s']]
    
    def __init__(self):
        super().__init__()
       
        self.pinbox_begintime.valueChanged.connect(self.starttime)
        self.pinbox_choose.valueChanged.connect(self.ttlchoose)
        self.pinbox_stoptime.valueChanged.connect(self.stoptime)
        self.pushButton_add.clicked.connect(self.addtimeline)
        self.pushButton_delete.clicked.connect(self.deletetimeline)
        self.pushButton_show.clicked.connect(self.show_current_timeline)
        self.pushButton_runtimeline.clicked.connect(self.runtimeline)
        
        self.DCup.clicked.connect(self.dcup1)
        self.DCup_2.clicked.connect(self.dcup2)
        self.DCup_3.clicked.connect(self.dcup3)
        self.DCup_4.clicked.connect(self.dcup4)
        self.DCup_5.clicked.connect(self.dcup5)
        self.DCup_6.clicked.connect(self.dcup6)
        self.DCup_7.clicked.connect(self.dcup7)
        self.DCup_8.clicked.connect(self.dcup8)
        self.DCup_9.clicked.connect(self.dcup9)
        self.DCup_10.clicked.connect(self.dcup10)
        self.DCup_11.clicked.connect(self.dcup11)
        self.DCup_12.clicked.connect(self.dcup12)
        
        
        self.DCdown.clicked.connect(self.dcdown1)
        self.DCdown_2.clicked.connect(self.dcdown2)
        self.DCdown_3.clicked.connect(self.dcdown3)
        self.DCdown_4.clicked.connect(self.dcdown4)
        self.DCdown_5.clicked.connect(self.dcdown5)
        self.DCdown_6.clicked.connect(self.dcdown6)
        self.DCdown_7.clicked.connect(self.dcdown7)
        self.DCdown_8.clicked.connect(self.dcdown8)
        self.DCdown_9.clicked.connect(self.dcdown9)
        self.DCdown_10.clicked.connect(self.dcdown10)
        self.DCdown_11.clicked.connect(self.dcdown11)
        self.DCdown_12.clicked.connect(self.dcdown12)
        
        self.doubleSpinBox_1.valueChanged.connect(self.DC1length)
        self.doubleSpinBox_2.valueChanged.connect(self.DC2length)
        self.doubleSpinBox_3.valueChanged.connect(self.DC3length)
        self.doubleSpinBox_4.valueChanged.connect(self.DC4length)
        self.doubleSpinBox_5.valueChanged.connect(self.DC5length)
        self.doubleSpinBox_6.valueChanged.connect(self.DC6length)
        self.doubleSpinBox_7.valueChanged.connect(self.DC7length)
        self.doubleSpinBox_8.valueChanged.connect(self.DC8length)
        self.doubleSpinBox_9.valueChanged.connect(self.DC9length)
        self.doubleSpinBox_10.valueChanged.connect(self.DC10length)
        self.doubleSpinBox_11.valueChanged.connect(self.DC11length)
        self.doubleSpinBox_12.valueChanged.connect(self.DC12length)
        
        self.DCup_sel.clicked.connect(self.dcup_sel)
        self.DCdown_sel.clicked.connect(self.dcdown_sel)
        self.readall.clicked.connect(self.readallselect)
        
        self.DCstate.setText(str(DCvalue[0]))
        self.DCstate_2.setText(str(DCvalue[1]))
        self.DCstate_3.setText(str(DCvalue[2]))
        self.DCstate_4.setText(str(DCvalue[3]))
        self.DCstate_5.setText(str(DCvalue[4]))
        self.DCstate_6.setText(str(DCvalue[5]))
        self.DCstate_7.setText(str(DCvalue[6]))
        self.DCstate_8.setText(str(DCvalue[7]))
        self.DCstate_9.setText(str(DCvalue[8]))
        self.DCstate_10.setText(str(DCvalue[8]))
        self.DCstate_11.setText(str(DCvalue[10]))
        self.DCstate_12.setText(str(DCvalue[11]))
        
        
    def dcup1(self):
         s=self.checkBox_DC1.checkState()
         if s==2:
            self.DCUP(1,1)
            self.DCstate.setText(str(DCvalue[0]))
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
            
            
    def dcdown1(self):
         s=self.checkBox_DC1.checkState()
         if s==2:
            self.DCUP(1,0)
            self.DCstate.setText(str(DCvalue[0]))
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
            
    
            
    def DCUP(self,num,move):
        if move == 1:
          DCvalue[num-1]=DCvalue[num-1]+DClength[num-1]
          DCvalue[num-1]=round(DCvalue[num-1],3)
          self.textEdit_log.append('set DC'+str(num)+' to '+str(DCvalue[num-1])+'V')
        if move == 0:
          DCvalue[num-1]=DCvalue[num-1]-DClength[num-1]
          DCvalue[num-1]=round(DCvalue[num-1],3)
          self.textEdit_log.append('set DC'+str(num)+' to '+str(DCvalue[num-1])+'V')
          
    def dcup_sel(self):
        self.selectDC(1)
        print('1')
    def dcdown_sel(self):
        self.selectDC(0)
        
        
        
    def selectDC(self,move):    
        DCcheck[0]=self.checkBox_DC1.checkState()
        DCcheck[1]=self.checkBox_DC2.checkState()
        DCcheck[2]=self.checkBox_DC3.checkState()
        DCcheck[3]=self.checkBox_DC4.checkState()
        DCcheck[4]=self.checkBox_DC5.checkState()
        DCcheck[5]=self.checkBox_DC6.checkState()
        DCcheck[6]=self.checkBox_DC7.checkState()
        DCcheck[7]=self.checkBox_DC8.checkState()
        DCcheck[8]=self.checkBox_DC9.checkState()
        DCcheck[9]=self.checkBox_DC10.checkState()
        DCcheck[10]=self.checkBox_DC11.checkState()
        DCcheck[11]=self.checkBox_DC12.checkState()
        if move ==1:
          for num in range(0,12):
            if (DCcheck[num]==2):
               DCvalue[num]=DCvalue[num]+0.01
               DCvalue[num]=round(DCvalue[num],3)
               self.textEdit_log.append('set DC'+str(num)+' to '+str(DCvalue[num-1])+'V')
        if move ==0:
          for num in range(0,12):
            if DCcheck[num]==2:
               DCvalue[num]=DCvalue[num]-0.01
               DCvalue[num]=round(DCvalue[num],3)
               self.textEdit_log.append('set DC'+str(num)+' to '+str(DCvalue[num-1])+'V')   
        self.DCstate.setText(str(DCvalue[0]))
        self.DCstate_2.setText(str(DCvalue[1]))
        self.DCstate_3.setText(str(DCvalue[2]))
        self.DCstate_4.setText(str(DCvalue[3]))
        self.DCstate_5.setText(str(DCvalue[4]))
        self.DCstate_6.setText(str(DCvalue[5]))
        self.DCstate_7.setText(str(DCvalue[6]))
        self.DCstate_8.setText(str(DCvalue[7]))
        self.DCstate_9.setText(str(DCvalue[8]))
        self.DCstate_10.setText(str(DCvalue[8]))
        self.DCstate_11.setText(str(DCvalue[10]))
        self.DCstate_12.setText(str(DCvalue[11]))
    
    def readallselect(self):    
         DCcheck[0]=self.checkBox_DC1.checkState()
         DCcheck[1]=self.checkBox_DC2.checkState()
         DCcheck[2]=self.checkBox_DC3.checkState()
         DCcheck[3]=self.checkBox_DC4.checkState()
         DCcheck[4]=self.checkBox_DC5.checkState()
         DCcheck[5]=self.checkBox_DC6.checkState()
         DCcheck[6]=self.checkBox_DC7.checkState()
         DCcheck[7]=self.checkBox_DC8.checkState()
         DCcheck[8]=self.checkBox_DC9.checkState()
         DCcheck[9]=self.checkBox_DC10.checkState()
         DCcheck[10]=self.checkBox_DC11.checkState()
         DCcheck[11]=self.checkBox_DC12.checkState()
         DCvalue_temp=[0,0,0,0,0,0,0,0,0,0,0,0]
         DCvalue_temp[0]=float(self.DCstate.text())
         DCvalue_temp[1]=float(self.DCstate_2.text())
         DCvalue_temp[2]=float(self.DCstate_3.text())
         DCvalue_temp[3]=float(self.DCstate_4.text())
         DCvalue_temp[4]=float(self.DCstate_5.text())
         DCvalue_temp[5]=float(self.DCstate_6.text())
         DCvalue_temp[6]=float(self.DCstate_7.text())
         DCvalue_temp[7]=float(self.DCstate_8.text())
         DCvalue_temp[8]=float(self.DCstate_9.text())
         DCvalue_temp[9]=float(self.DCstate_10.text())
         DCvalue_temp[10]=float(self.DCstate_11.text())
         DCvalue_temp[11]=float(self.DCstate_12.text())
         for num in range(0,12):
             if DCcheck[num] == 2:
                 DCvalue[num]=DCvalue_temp[num]
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
            
# ！！！！！！！！！！！！！！ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2上次写到这里
    
    def stoptime(self,int):
        a=int
        label=self.comboBox_stoptime.currentText()
        set_timeline[4]=label
        if label=='us':
            set_timeline[3]=a    
        if label=='ms':
            set_timeline[3]=a*1000
        if label=='s':
            set_timeline[3]=a*1000000
    def addtimeline(self):
        add=copy.copy(set_timeline)
        timeline.append(add)
        self.textEdit_log.append("current timeline:\n  (%s)"%timeline)
    def deletetimeline(self):
        try:
            timeline.pop()
            self.textEdit_log.append("current timeline:\n  (%s)"%timeline)
        except:
            self.textEdit_log.append("no more to delete,current timeline:\n  (%s)"%timeline)
    def show_current_timeline(self):
        self.textEdit_log.append("current timeline:\n  (%s)"%timeline)
    def runtimeline(self):
        self.timeline_client(timeline)
         
    def ttl_client(self,port):##没有设置时间，时间直接在ttl的对应文件里面
        file = 'repository/led'+str(port)+'.py',
        print(file)
#        expid = dict(
#        file = 'repository/led'+str(port)+'.py',
#        class_name = 'ttl'+str(port),
#        log_level=logging.DEBUG,
#        # 如果有参数，就利用下面的方式传递参数
##        arguments = dict(
##        state = True,
##        count =  5000000 )
#    )
#rid = schedule.submit(
#    pipeline_name='main', expid=expid, priority=0, due_date=None, flush=False)
#print('--------------------\n')
        
    def timeline_client(self,timeline):
        timeline_=timeline
        startevent=[]
        stopevent=[]
        for i in range(len(timeline_)):
            startevent=startevent+[[timeline_[i][0],timeline_[i][1],1]]
            stopevent=stopevent+[[timeline_[i][0],timeline_[i][3],0]]
#        print(startevent)
#        print(stopevent)
        timeline_=startevent+stopevent
        for i in range(len(timeline_)-1):
           for j in range(len(timeline_)-i-1):
              if (timeline_[j][1]>timeline_[j+1][1]):
                 temp=timeline_[j+1]
                 timeline_[j+1]=timeline_[j]
                 timeline_[j]=temp
        print(timeline_)
        ttl=startt=event=''
        for i in range(len(timeline_)):
            ttl=ttl+str(timeline_[i][0])+'/'
        for i in range(len(timeline_)):
            startt=startt+str(timeline_[i][1])+'/'
        for i in range(len(timeline_)):
            event=event+str(timeline_[i][2])+'/'
        print(ttl)
        print(startt)
        print(event)
        
        expid = dict(
        file = 'repository/argu_set.py',
        class_name = 'argu_set',
        log_level=logging.DEBUG,
        # 如果有参数，就利用下面的方式传递参数
        arguments = dict(
            ttlport_=ttl,
            starttime_=startt,
            move_=event)
        )
        rid = schedule.submit(
            pipeline_name='main', expid=expid, priority=0, due_date=None, flush=False)
print('--------------------\n')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a = mainprogram()
    a.show()
    sys.exit(app.exec_()) 