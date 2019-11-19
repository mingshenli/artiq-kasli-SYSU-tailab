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
import logging
from PyQt5 import QtCore, QtGui, QtWidgets
from timeline_set_gui30_import  import MainWindow,timeline_vi_window
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtCore import pyqtSignal
import time as t
import os
import sys,copy,re
import numpy as np
from artiq.protocols.pc_rpc import (Client)
import pyqtgraph as pg
#from led import LED

schedule, exps, datasets = [
    Client('::1', 3251, 'master_' + i) for i in 'schedule experiment_db dataset_db'.split()
    ]


class timeline_vi(timeline_vi_window):
    def __init__(self):
        super().__init__()
#        self.verticalLayout
#        self.do()
        self.timeline=[]
        self.max_max_chan=0
        self.plot_section=QtGui.QVBoxLayout()
        
        self.centralwidget.setLayout(self.plot_section)
        
        self.pw1=pg.PlotWidget(name='Plot1')
        self.pw1.showGrid(x=True,y=True)
        self.plot_section.addWidget(self.pw1)
      
#        pw2=pg.PlotWidget(name='Plot1')
#        self.verticalLayout.addWidget(pw2)
#        self.pushButton.clicked.connect(self.clean)
        print(type(self.pw1))
#        self.update(1)
#    def update(self,timeline):
#        self.timeline=timeline
#        self.plot()
#    def do(self):
#        print('do')
#        a=mainprogram()
#        a.mySignal.connect(self.plot)
#        a.pushButton_add.clicked.connect(self.plot)
   
    def clearall(self):
        for i in range(1,16):
            try:
                 getattr(self,'p'+str(i)).clear()
            except:
                pass

    def plot(self,timeline):
        if len(timeline)==0:
            self.clearall()
            return
        max_chan=0
        max_t=0
        temp=sorted(timeline,key=lambda timeline:timeline[3]*self.unitchange(timeline[4]))
        max_t=temp[len(temp)-1][3]*self.unitchange(temp[len(temp)-1][4]) 
        #print(max_t)
        temp=sorted(timeline,key=lambda timeline:timeline[0])
        max_chan=temp[len(temp)-1][0]
        
        #print('call')
        #print('chan',max_chan)
        x=np.linspace(0,max_t+1,max_t+1)
        y=np.linspace(0,0,max_t+1)
        ######################################################设置方波数组
        for i in range(1,max_chan+1):
            setattr(self,'y'+str(i),np.linspace(i,i,max_t+1))
       
        for i in range(len(timeline)):
            index_chan=int(timeline[i][0])
            index_start=int(timeline[i][1]*self.unitchange(timeline[i][2]))
            index_stop=int(timeline[i][3]*self.unitchange(timeline[i][4]))
            getattr(self,'y'+str(index_chan))[index_start:index_stop]=index_chan+0.9
#       ######################################################设置方波数组    
        for i in range(1,max(self.max_max_chan,max_chan)+1):
            try:
                 getattr(self,'p'+str(i)).clear()
            except:
                pass
        for i in range(1,max_chan+1):
            try:
                 getattr(self,'p'+str(i)).setData(x,getattr(self,'y'+str(i)),stepMode=False, fillLevel=i, brush='b')
                 getattr(self,'p'+str(i)).showGrid(x=True, y=True)
            except:
                setattr(self,'p'+str(i),self.pw1.plot())
                getattr(self,'p'+str(i)).setData(x,getattr(self,'y'+str(i)),stepMode=False, fillLevel=i, brush='b')
                
            
        self.max_max_chan=max_chan 
#            self.p1.plot(x,getattr(self,'y'+str(i)),fillLeval=i)
#        self.p1=self.pw1.plot()
#        self.p1.setData(x,y)
#    def update(self,timeline):
#        
#        pw2=pg.PlotWidget(name='Plot1')
#        self.verticalLayout.addWidget(pw2)
#        
#        max_chan=0
#        max_t=0
#        temp=sorted(timeline,key=lambda timeline:timeline[3]*self.unitchange(timeline[4]))
#        max_t=temp[len(temp)-1][3]*self.unitchange(temp[len(temp)-1][4]) 
#        print(max_t)
#        temp=sorted(timeline,key=lambda timeline:timeline[0])
#        max_chan=temp[len(temp)-1][0]
#        print(max_chan)
#        for i in range(3):
#            setattr(self,'chan'+str(i),pg.PlotWidget(name='channel'+str(i)))
#            self.verticalLayout.addWidget(getattr(self,'chan'+str(i)))
#            print(type(self.chan0))
#        self.verticalLayout.addWidget(self.chan0)
    def unitchange(self,str):
        if str=='s':
            return 1000000000
        if str=='ms':
            return 1000000
        if str=='us':
            return 1000
        if str=='ns':
            return 1   
        
        
        
        
        
        
        
class mainprogram(MainWindow):
    global DCvalue 
    global DCcheck
    global set_timeline #ttl/起始时间/终止时间
    global timeline
    global DClength
    
    DCvalue= [5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00]
    DCcheck=[0,0,0,0,0,0,0,0,0,0,0,0]
    DClength=[0,0,0,0,0,0,0,0,0,0]
    set_timeline=[1,0.0,'s',0.0,'s']
    timeline=[[1,0.0,'s',0.0,'s']]
    mySignal=pyqtSignal(str)
    def __init__(self):
        super().__init__()
        
        
        self.plot=timeline_vi()
        self.plot.show()
        
        
        self.pinbox_begintime.valueChanged.connect(self.starttime)
        self.pinbox_choose.valueChanged.connect(self.ttlchoose)
        self.pinbox_stoptime.valueChanged.connect(self.stoptime)
        self.pushButton_add.clicked.connect(self.addtimeline)
        self.pushButton_delete.clicked.connect(self.deletetimeline)
        self.pushButton_show.clicked.connect(self.show_current_timeline)
        self.pushButton_runtimeline.clicked.connect(self.runtimeline)
        self.load_modual.clicked.connect(self.loadmodual)
        self.open_monitor.clicked.connect(self.openmonitor)
        self.update.clicked.connect(self.update_manualy)
        self.ord_time.clicked.connect(self.ord_by_starttime)
        self.save.clicked.connect(self.savetimeline)
        self.load.clicked.connect(self.loadtimeline)
        self.add_sel.clicked.connect(self.add_at)
        self.del_sel.clicked.connect(self.delete_at)
        self.add_posi.valueChanged.connect(self.add_location)
        self.dele_posi.valueChanged.connect(self.dele_location)
        self.add_position=100000#默认在最尾端
        self.delete_position=100000
        self.comboBox_starttime.currentTextChanged.connect(self.comboxchange)
        self.comboBox_stoptime.currentTextChanged.connect(self.comboxchange)
        self.comboBox_delaytime_unit.currentTextChanged.connect(self.comboxchange)
    def add_location(self,str):
        self.add_position=int(str) 
#        print(self.add_position)
    def dele_location(self,str):
        self.delete_position=int(str)
#        print(self.delete_position)
    def add_at(self): 
#        print(self.add_position)
        add=copy.copy(set_timeline)
        timeline.insert(self.add_position,add)
        self.textEdit_log.append("current timeline:\n  (%s)"%timeline)
    def delete_at(self):
#        print(self.delete_position)
        del timeline[self.delete_position]
        self.textEdit_log.append("current timeline:\n  (%s)"%timeline)
        
 
    def ttlchoose(self,str):
        a=int(str)
        set_timeline[0]=a
       
    def starttime(self,int):
        a=int 
        label=self.comboBox_starttime.currentText()
        set_timeline[2]=label
        set_timeline[1]=int
#        if label=='ns':
#            set_timeline[1]=a  
#        if label=='us':
#            set_timeline[1]=a*1000    
#        if label=='ms':
#            set_timeline[1]=a*1000000
#        if label=='s':
#            set_timeline[1]=a*1000000000

    def stoptime(self,int):
        a=int
        label=self.comboBox_stoptime.currentText()
        set_timeline[4]=label
        set_timeline[3]=int
#        if label=='ns':
#            set_timeline[1]=a  
#        if label=='us':
#            set_timeline[3]=a*1000    
#        if label=='ms':
#            set_timeline[3]=a*1000000
#        if label=='s':
#            set_timeline[3]=a*1000000000
    def plot_timeline(self):
        
        self.plot.plot(timeline)
    def addtimeline(self):
        self.plot_timeline()
        add=copy.copy(set_timeline)
        timeline.append(add)
        self.textEdit_log.append("current timeline:\n  (%s)"%timeline)
        self.showtimeline()
    def deletetimeline(self):
        timeline.pop()
#        print(timeline)
        self.textEdit_log.append("current timeline:\n  (%s)"%timeline)
        self.showtimeline()
    def show_current_timeline(self):
        self.textEdit_log.append("current timeline:\n  (%s)"%timeline)
        self.showtimeline()
    def runtimeline(self):
        self.timeline_client(timeline)
        
    def unitchange(self,str):
        if str=='s':
            return 1000000000
        if str=='ms':
            return 1000000
        if str=='us':
            return 1000
        if str=='ns':
            return 1
    def showtimeline(self):##################################################################################################
        self.textEdit_timeline.clear()
#        self.textEdit_timeline.append('ttl|starttime  |stoptime')
        
        for i in range(len(timeline)):
            self.textEdit_timeline.append(str(timeline[i]))
        self.textEdit_timeline.append('')#######################为了和txt读入格式统一
        self.plot_timeline()
#        a=timeline_vi()
#        a.update(timeline)
        self.mySignal.emit('a')
    def savetimeline(self):
        
        fileName,ok = QFileDialog.getSaveFileName(self,
                                    "文件保存",
                                    "D:/artiq-kasli/artiq-master/timelinelib",
                                    "Text Files (*.txt)")
        f=open(fileName,"w",encoding="UTF-8-sig")
        for i in range(len(timeline)):
            f.write(str(timeline[i])+'\n')
        f.close()
    def update_manualy(self):
        i=self.textEdit_timeline.toPlainText()
        try:
            s=self.str_to_list(i)
            self.textEdit_log.append('update success')
        except Exception as e:
            self.textEdit_log.append(str(e))
            self.textEdit_log.append('check the format of the timeline')
            return       
        global timeline
        print(len(timeline))
        print(len(s))
        timeline=s
       
        self.showtimeline()
    
    def comboxchange(self):
         set_timeline[2]=self.comboBox_starttime.currentText()
         set_timeline[4]=self.comboBox_stoptime.currentText()
        
    def loadtimeline(self):
        reply = QMessageBox.information(self, 'warning','将清除现有时间轴',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        if reply==QMessageBox.Yes:
            pass
        if reply==QMessageBox.No:
            return
        fileName, filetype = QFileDialog.getOpenFileName(self,
                                    "选取文件",
                                    "D:/artiq-kasli/artiq-master/timelinelib",
                                    "Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔
        try:
            f=open(fileName,"r",encoding="UTF-8-sig")
            i=f.read()
            f.close()
        except Exception as e:
            self.textEdit_log.append(str(e))
            return
        
        global timeline
        try:
            timeline=self.str_to_list(i)#################################################更新时间轴
        except Exception as e:
            self.textEdit_log.append(str(e))
            self.textEdit_log.append('check the format of the timeline')
            return  
        print('**',timeline)
        print(type(timeline))
#        print(timeline)
#        print(len(timeline))
        self.showtimeline()
    def loadmodual(self):
#        reply = QMessageBox.information(self, 'warming','将清除现有时间轴',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
#        if reply==QMessageBox.Yes:
#            pass
#        if reply==QMessageBox.No:
#            return
        fileName, filetype = QFileDialog.getOpenFileName(self,
                                    "选取文件",
                                    "D:/artiq-kasli/artiq-master/timelinelib",
                                    "Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔
        try:
            f=open(fileName,"r",encoding="UTF-8-sig")
            i=f.read()
            f.close()
        except Exception as e:
            self.textEdit_log.append(str(e))
            return
        
        global timeline
        try:
            add=self.str_to_list(i)
        except Exception as e:
            self.textEdit_log.append(str(e))
            self.textEdit_log.append('check the format of the timeline')
            return
        
        delay=self.pinbox_delaytime.value()
        u=self.comboBox_delaytime_unit.currentText()
        for i in range(len(add)):
            
            add[i][1]=add[i][1]+delay*(self.unitchange(u)/self.unitchange(add[i][2]))
            add[i][3]=add[i][3]+delay*(self.unitchange(u)/self.unitchange(add[i][4]))
        
        print('delay',delay)
        timeline=timeline+(add)########
        
        self.showtimeline()
    def str_to_list(self,str):
        i=str
        s=re.split('\n',i)
#        print(s)
        r=[]
        rr=[]
        l=len(s)
#        print(l)
        for i in reversed(range(l-5,l)):
            print('s[i]=',s[i])
            print(s[i]=='')
            if s[i]=='':
                s.pop()
#                print('*********************')
            else:
                break
#        print(s)
        for i in range(len(s)):
            temp=s[i]
            temp=temp.strip()
            temp=temp.strip('[')
            temp=temp.strip(']')
            rr=temp.split(',')
            rr[0]=int(rr[0])
            rr[1]=float(rr[1])
            rr[2]=rr[2].strip()
            rr[2]=rr[2].strip(' \'')
            rr[3]=float(rr[3])
            rr[4]=rr[4].strip(' \'')
            r.append(rr)
        return r
    def openmonitor(self):
        os.popen('activate artiq-kasli && d: && cd D:/artiq-kasli/artiq-master && python pulse_monitor_window.py')
        
    def ord_by_starttime(self):
        timeline.sort(key=lambda timeline:timeline[1]*self.unitchange(timeline[2]))
        self.showtimeline()
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
            startevent=startevent+[[timeline_[i][0],timeline_[i][1]*self.unitchange(timeline_[i][2]),1]]
            stopevent=stopevent+[[timeline_[i][0],timeline_[i][3]*self.unitchange(timeline_[i][4]),0]]#注意全部转换为ns为单位
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
        datasets.set("ttlport",ttl)
        datasets.set("starttime",startt)
        datasets.set("move",event)
        
        expid1 = dict(
        file = 'repository/timeline_CodeGenerate.py',
        class_name = 'A',
        log_level=logging.DEBUG,
        arguments=None
        )
        expid2 = dict(
        file = 'repository/auto_code/output_test02.py',
        class_name = 'code',
        log_level=logging.DEBUG,
        arguments=None
        )
        
        rid = schedule.submit(
           pipeline_name='main', expid=expid1, priority=0, due_date=None, flush=False)
#        rid = schedule.submit(
#           pipeline_name='main', expid=expid2, priority=0, due_date=None, flush=False)
#        print('--------------------\n')
#        t.sleep(3)
#        count=datasets.get('count')
#        self.textEdit_log.append('count:'+str(count))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a = mainprogram()
    a.show()
#    b=timeline_vi()
#    b.show()
   
    sys.exit(app.exec_()) 