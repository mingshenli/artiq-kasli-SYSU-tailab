# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 19:56:04 2020

@author: 18926
"""
from socket import *
from demons_gui_import import MainWindow
import logging
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtCore import pyqtSignal
import time as t
import os
import sys,copy,re,math
import numpy as np
import pyqtgraph as pg
import time

from artiq.protocols.pc_rpc import (Client)
schedule, exps, datasets = [
    Client('::1', 3251, 'master_' + i) for i in 'schedule experiment_db dataset_db'.split()
    ]

class mainprogram(MainWindow):
    
    
    def __init__(self):
        super().__init__()
        #################################################初始化全局参数
        self.roundtime=0
        self.sleepingtime=2
        self.startfre=0
        self.stopfre=0
        self.lenthfre=0
        self.count=[0,1]
        self.frelist=[0,2]
        #################################################初始化全局参数
        #################################################设定控件回调
        self.Manual_input.clicked.connect(self.manualinput)
        self.Start_scan.clicked.connect(self.startscan)
        self.Save.clicked.connect(self.save)
        
#        self.Start_fre.valueChanged.connect(self.set_startfre)
#        self.Stop_fre.valueChanged.connect(self.set_stopfre)
#        self.Len_fre.valueChanged.connect(self.set_lenfre)
#        self.Round_time.valueChanged.connect(self.set_roundtime)
#        self.Sleeping_time.valueChanged.connect(self.set_stopfre)
        #################################################设定控件回调
        #############################################设定画图
        self.l = QtGui.QVBoxLayout()#布局方式，layout是widget下面的布局方式
        self.Plot_area.setLayout(self.l)
        
        self.pw=pg.PlotWidget(name='Plot1')
        self.pw.setTitle('a')
        self.pw.showGrid(x=True,y=True)
        self.l.addWidget(self.pw)
        
        
        
        #############################################设定画图
    
    def manualinput(self):
        self.roundtime=self.Round_time.value()
        self.sleepingtime=self.Sleeping_time.value()
        self.startfre=self.Stop_fre.value()
        self.stopfre=self.Stop_fre.value()
        self.lenthfre=self.Len_fre.value()
        
    
    def startscan(self):
        print("执行scan代码")
        start_fre=self.startfre
        stop_fre=self.stopfre
        step_fre=self.lenthfre
        fre=[]
        for i in np.arange(start_fre,stop_fre,step_fre):             #修改扫描频率范围和步长
            fr="FREQ"+str(i)+"MHZ\n"
            fre.append(fr.encode())
        host="192.168.1.114"
        port=5025
        s=socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        s.send(b'AMPR -7\n')                     #控制幅度
        s.close()
        s=socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        s.send(b'ENBR1\n')                         #0表示不输出，1表示输出信号
        s.close()
        ##############################################################################扫频初始化
        ########################################################################计数初始化
        datasets.set("count_y",[])
        
        
        scanlength=self.roundtime
        scan_point_length=20
        for j in np.arange(0,scanlength,1):                #控制扫描次数和扫描时间
            for i in np.arange(0,scan_point_length,1):           #控制扫描点数和步长对应
                #############################################################################变频
                s=socket(AF_INET,SOCK_STREAM)
                s.connect((host,port))
                s.send(fre[i])
                s.close()
                start=time.clock()
                expid1 = dict(
                file = 'repository/count/input_count_33.py',
                class_name = 'inputtest',
                log_level=logging.DEBUG,
                arguments=None
                )
                                    
                rid = schedule.submit(
                pipeline_name='main', expid=expid1, priority=0, due_date=None, flush=False)
                ###################################################################################count
                time.sleep(self.sleepingtime)############################################要留足够长的时间给count执行和写数据_也是频率停留时间
                print('now scan at',i)
        #        #############################################################################变频
        #        #################################################################################等待
        #        t=0                                     #控制每个频率停留时间
        #        while True:
        #            end=time.clock ()
        #            if  float(end-start)>=t:
        #                break
                #################################################################################等待
                ##################################################################################count
                
                
        #################################################关闭网口        
        s=socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        s.send(b'ENBR0\n')
        s.close()
        #################################################关闭网口  
                
                
        ############################################读取数据
        time.sleep(0)############################################要留足够长的时间给count执行和写数据
        count=datasets.get("count_y")
        print(count)
        self.count=count
        self.frelist=list(np.arange(start_fre,stop_fre,step_fre))
        
        self.plot()
    
    def save(self):
        print("执行save代码")
        #################################################################弹出路径选择对话框
        try:
            fileName,ok = QFileDialog.getSaveFileName(self,
                                        "文件保存",
                                        "D:/artiq-kasli/artiq-master", #改成默认存储路径，不要乱放
                                        "Text Files (*.txt)")
        except:
            print("获取路径失败")
            
            
        f=open(fileName,"w",encoding="UTF-8-sig")           
        for i in range(len(self.frelist)):
            f.write(str(self.frelist[i])+' '+str(self.count[i])+'\n')
        f.close()
        #################################################################弹出路径选择对话框
    def plot(self):
        y=np.array(self.count)
        x=np.array(self.frelist)
        self.p1=self.pw.plot(x,y,stepMode=False,brush='b')
        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a = mainprogram()
    a.show()
#    b=timeline_vi()
#    b.show()
   
    sys.exit(app.exec_()) 
    
    
    
    
    
    
    
    
    
    
    
    