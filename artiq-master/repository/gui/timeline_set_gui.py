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
from timeline_set_gui_import  import MainWindow
import sys,copy
from artiq.protocols.pc_rpc import (Client)
#from led import LED

schedule, exps, datasets = [
    Client('::1', 3251, 'master_' + i) for i in 'schedule experiment_db dataset_db'.split()
    ]

class mainprogram(MainWindow):
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
        self.add_sel.clicked.connect(self.add_at)
        self.del_sel.clicked.connect(self.delete_at)
        self.add_posi.valueChanged.connect(self.add_location)
        self.dele_posi.valueChanged.connect(self.dele_location)
        self.add_position=100000#默认在最尾端
        self.delete_position=100000
    def add_location(self,str):
        self.add_position=int(str) 
        print(self.add_position)
    def dele_location(self,str):
        self.delete_position=int(str)
        print(self.delete_position)
    def add_at(self): 
        print(self.add_position)
        add=copy.copy(set_timeline)
        timeline.insert(self.add_position,add)
        self.textEdit_log.append("current timeline:\n  (%s)"%timeline)
    def delete_at(self):
        print(self.delete_position)
        del timeline[self.delete_position]
        self.textEdit_log.append("current timeline:\n  (%s)"%timeline)
        
 
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
        timeline.pop()
#        print(timeline)
        self.textEdit_log.append("current timeline:\n  (%s)"%timeline)
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