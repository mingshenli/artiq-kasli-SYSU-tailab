# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:00:49 2019

@author: 18926
"""
from Main_control_window_import import Main_control_window
import os
import time as t
import logging
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys,copy,re
from DC_set_subwindow import dc_16chan_mainwindow
from PyQt5.QtCore import Qt, QThread,pyqtSignal, QTimer

from artiq.protocols.pc_rpc import (Client)
from hardwarelib import hardwarelist, dc_16chan,SG382
#schedule, exps, datasets = [
#    Client('::1', 3251, 'master_' + i) for i in 'schedule experiment_db dataset_db'.split()
#    ]

class mainprogram(Main_control_window):
    def __init__(self):
        super().__init__()
        self.scan=Scan()
        self.initHardware()
        self.hardware_scan_timeline=[]
        self.TLset.clicked.connect(self.activate_TLset)
        self.DCset.clicked.connect(self.activate_DCset)
        self.Run.clicked.connect(self.run_timeline)
        self.Monitor.clicked.connect(self.activate_pulse_monitor)
        self.pushButton.clicked.connect(self.startcount)
        self.pushButton_2.clicked.connect(self.clear)
        self.hardware_name.currentTextChanged.connect(self.get_parameter)
        self.add.clicked.connect(self.add_hardware_scan)
        self.update_manu.clicked.connect(self.update_manualy)
        
        self.initsubwindow()
        self.timeer=QTimer()
        self.timeer.timeout.connect(self.timerun)
        
    def initsubwindow(self):#子窗口的实例化在这里，硬件列表的初始化在scan里面
        self.DC_16chan_mainwindow=dc_16chan_mainwindow()
    def initHardware(self):
        _translate = QtCore.QCoreApplication.translate#更新硬件列表用的，在自动生成的gui py里面copy的语法
        
        
        print(list(self.scan.HardwareList.keys()))
        hardware_num=len(self.scan.HardwareList)
        hardware=list(self.scan.HardwareList.keys())
        for a in range(hardware_num):
            self.hardware_name.addItem("")
            self.hardware_name.setItemText(a,_translate("MainWindow",hardware[a]))
            print(a)
            print(hardware[a])
        self.get_parameter()
        
    def get_parameter(self):
        _translate = QtCore.QCoreApplication.translate
        current_hardware=self.hardware_name.currentText()
        par=self.scan.HardwareList[current_hardware]
        self.parameter.clear()#要先clear不然上一个仪器的参数不会消失
        for a in range(len(par)):
            self.parameter.addItem("")
            self.parameter.setItemText(a,_translate("MainWindow",par[a]))
            
    def add_hardware_scan(self):
        hardware=self.hardware_name.currentText()
        parameter=self.parameter.currentText()
        startvalue=round(self.start_value.value(),6)
        length=round(self.len.value(),6)
        self.hardware_scan_timeline.append([hardware,parameter,startvalue,length])
        self.showlog()
    def showlog(self):   
         self.textEdit.clear()
         for i in range(len(self.hardware_scan_timeline)):
              self.textEdit.append(str(self.hardware_scan_timeline[i]))
              
    def update_manualy(self):
        i=self.textEdit.toPlainText()
        try:
            s=self.str_to_list(i)
            self.log.append('update success')
        except Exception as e:
            self.log.append(str(e))
            self.log.append('check the format of the timeline')
            return       
        
            self.hardware_scan_timeline=s
            self.showlog()
            
        self.hardware_scan_timeline=s
    def activate_TLset(self):
        try:
            os.popen('activate artiq-kasli && d: && cd D:/artiq-kasli/artiq-master && python timeline_set_gui20.py')
        except Exception as e:
            print(e)
            
    def activate_DCset(self):#######################################################################
#        os.popen('cd D:/artiq-kasli/artiq-master && python DC_set1_1.py')
        
#        self.DC_window.sig.connect(self.data_from_DC)
        self.DC_16chan_mainwindow.show()
#        self.t=test()
#        self.t.start()
#        self.t.wait()
    def data_from_DC(self,list):
        self.log.append('DC:'+str(list))
        
    def activate_pulse_monitor(self):
        os.popen('cd D:/artiq-kasli/artiq-master && python pulse_monitor_window.py')
    def startcount(self):
        expid1 = dict(
        file = 'D:/artiq-kasli/artiq-master/repository/count/input_count_2.1.py',
        class_name = 'inputtest',
        log_level=logging.DEBUG,
        arguments=None
        )
        rid = schedule.submit(
                pipeline_name='main', expid=expid1, priority=0, due_date=None, flush=False)
        
    def clear(self):
        expid1 = dict(
        file = 'D:/artiq-kasli/artiq-master/repository/count/clearfigure.py',
        class_name = 'clearfigure',
        log_level=logging.DEBUG,
        arguments=None
        )
        rid = schedule.submit(
                pipeline_name='main', expid=expid1, priority=0, due_date=None, flush=False)
        
        
        
    def run_timeline(self):
        mode=self.run_mode.currentText()
        if mode=='no artiq hardware scan manual go':
            self.run_without_artiq_manual()
        if mode=='no artiq hardware scan set time go':
            self.run_without_artiq_settime()
        if mode=='artiq with hardware set':
            self.run_with_artiq()
            
            
    def run_without_artiq_manual(self):
        self.log.append('***running:no artiq hardware scan manual go***')
        roundtime=self.Roundtime.value()
        pa_lib=self.hardware_scan_timeline
        
        pam_number=len(pa_lib)
        for cycle in range(roundtime):
            reply = QMessageBox.information(self, 'next?','进行下一步？',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            if reply==QMessageBox.Yes:
                pass
            if reply==QMessageBox.No:
                return
            for pa in range(pam_number):
                    check=getattr(getattr(self,pa_lib[pa][0]+'_mainwindow'),'get_pa_state')(pa_lib[pa][1])
                    if check==2:
                        print('state: ',check)
                        re=getattr(getattr(self.scan,pa_lib[pa][0]),pa_lib[pa][1])(pa_lib[pa][2]+(cycle)*pa_lib[pa][3])
                        print('    ',re)
                        self.log.append('    '+str(re))
    #                    re=getattr(self.scan.DC_16chan,'te')(1)
    #                    print('--------------------------------',re)
    #                    print('---',getattr(self.scan.DC_16chan,'te')(1))
    #                    self.log.append(str(re))
                    if check==0:
                        self.log.append('    current: '+str(pa_lib[pa][0])+'-'+str(pa_lib[pa][1])+' is not activate')
        
            
    def run_without_artiq_settime(self):
        self.log.append('***running:no artiq hardware scan set time go***')
#        roundtime=self.Roundtime.value()
#        pa_lib=self.hardware_scan_timeline
#        t_length=self.time_length.value()
#        pam_number=len(pa_lib)
        
        self.roundtime=self.Roundtime.value()#总循环次数
        self.roundnow=0#当前循环次数
        self.pa_lib=self.hardware_scan_timeline
        self.t_length=self.time_length.value()
        self.pam_number=len(self.pa_lib)
        self.time_control()
        return
        
#        for cycle in range(roundtime):
#            t.sleep(1)
#            for pa in range(pam_number):
#                    check=getattr(getattr(self,pa_lib[pa][0]+'_mainwindow'),'get_pa_state')(pa_lib[pa][1])
#                    if check==2:
#                        print('state: ',check)
#                        re=getattr(getattr(self.scan,pa_lib[pa][0]),pa_lib[pa][1])(pa_lib[pa][2]+(cycle)*pa_lib[pa][3])
#                        print('    ',re)
#                        self.log.append('    '+str(re))
#    #                    re=getattr(self.scan.DC_16chan,'te')(1)
#    #                    print('--------------------------------',re)
#    #                    print('---',getattr(self.scan.DC_16chan,'te')(1))
#    #                    self.log.append(str(re))
#                    if check==0:
#                        self.log.append('    current: '+str(pa_lib[pa][0])+'-'+str(pa_lib[pa][1])+' is not activate')
#                        print('not output')
    def time_control(self):
        t_length=self.time_length.value()
        
        
        self.timeer.setSingleShot(False)
        self.timeer.start(int(t_length*1000))
        
    def timerun(self):
        if self.roundnow<=self.roundtime:
            for pa in range(self.pam_number):
                    check=getattr(getattr(self,self.pa_lib[pa][0]+'_mainwindow'),'get_pa_state')(self.pa_lib[pa][1])
                    if check==2:
#                        print('state: ',check)
                        re=getattr(getattr(self.scan,self.pa_lib[pa][0]),self.pa_lib[pa][1])(self.pa_lib[pa][2]+(self.roundnow)*self.pa_lib[pa][3])
#                        print(' re',re)
                        self.log.append('    '+str(re))
    #                    re=getattr(self.scan.DC_16chan,'te')(1)
    #                    print('--------------------------------',re)
    #                    print('---',getattr(self.scan.DC_16chan,'te')(1))
    #                    self.log.append(str(re))
                    if check==0:
                        self.log.append('    current: '+str(self.pa_lib[pa][0])+'-'+str(self.pa_lib[pa][1])+' is not activate')
                        print('not output',self.roundnow)
            self.roundnow=self.roundnow+1
        else:
            self.timeer.stop()
     




            
    def run_with_artiq(self):
        self.log.append('***running:artiq with hardware set***')
    def run_artiq_timeline(self):
#        roundtime=self.Roundtime.value()
        expid1 = dict(
        file = 'repository/auto_code/output_test02.py',
        class_name = 'code',
        log_level=logging.DEBUG,
        arguments=None
        )
#        expid_test = dict(
#        file = 'repository/example/arguments_demo.py',
#        class_name = 'ArgumentsDemo2',
#        log_level=logging.DEBUG,
#        arguments=None
#        )
        try:
#            for i in range(roundtime):
            rid = schedule.submit(
            pipeline_name='main', expid=expid1, priority=0, due_date=None, flush=False)
        except Exception as e:
            print(e)
            return
        
        
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
         
            rr[0]=rr[0].strip()#移除指定字符
            rr[0]=rr[0].strip(' \'')#'的转译
            rr[1]=rr[1].strip()
            rr[1]=rr[1].strip(' \'')
            rr[2]=float(rr[2])
            rr[3]=float(rr[3])
            
            r.append(rr)
        return r
    
class test(QThread):
    def __init__(self):
        super(test, self).__init__()

        self.w=dc_16chan_mainwindow()
    def run(self):
        for a in range(10):
            t.sleep(1)
            print(a)
        self.terminate()

    
class Scan(object):
    def __init__(self):
        self.hardware=hardwarelist()
        self.HardwareList=self.hardware.hardware
        
        self.DC_16chan=dc_16chan()
        self.SG382=SG382()
#        self.DC16chan.DC1(5)
    def run(self,roundtime=1,pa_lib=None):
        pam_number=len(pa_lib)
        for cycle in range(roundtime):
            for pa in range(pam_number):
                getattr(getattr(self,pa_lib[pa][0]),pa_lib[pa][1])(pa_lib[pa][2]+(cycle)*pa_lib[pa][3])
                   
        
    def re(self):
        print('haaaaaaaaaaaaaaaaaaaaaaaaaaaa')

            
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a = mainprogram()
    a.show()
    sys.exit(app.exec_()) 
