# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\18926\Desktop\qtsesigner\main_control_gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import os
import time
import logging
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,copy
from artiq.protocols.pc_rpc import (Client)
schedule, exps, datasets = [
    Client('::1', 3251, 'master_' + i) for i in 'schedule experiment_db dataset_db'.split()
    ]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TLset = QtWidgets.QPushButton(self.centralwidget)
        self.TLset.setGeometry(QtCore.QRect(60, 70, 191, 101))
        self.TLset.setObjectName("TLset")
        self.Monitor = QtWidgets.QPushButton(self.centralwidget)
        self.Monitor.setGeometry(QtCore.QRect(260, 70, 211, 101))
        self.Monitor.setObjectName("Monitor")
        self.DCset = QtWidgets.QPushButton(self.centralwidget)
        self.DCset.setGeometry(QtCore.QRect(480, 70, 211, 101))
        self.DCset.setObjectName("DCset and monitor")
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setGeometry(QtCore.QRect(50, 220, 251, 141))
        self.Run.setObjectName("Run")
        self.Roundtime = QtWidgets.QSpinBox(self.centralwidget)
        self.Roundtime.setGeometry(QtCore.QRect(510, 230, 191, 141))
        self.Roundtime.setMaximum(100000)
        self.Roundtime.setProperty("value", 1)
        self.Roundtime.setObjectName("Roundtime")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 210, 221, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TLset.setText(_translate("MainWindow", "activate timelineSet"))
        self.Monitor.setText(_translate("MainWindow", "activate pulse_monitor "))
        self.DCset.setText(_translate("MainWindow", "activate DCset"))
        self.Run.setText(_translate("MainWindow", "run timeline"))
        self.label.setText(_translate("MainWindow", "round time"))
        
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)  
class mainprogram(MainWindow):
    def __init__(self):
        super().__init__()
        self.TLset.clicked.connect(self.activate_TLset)
        self.DCset.clicked.connect(self.activate_DCset)
        self.Run.clicked.connect(self.run_timeline)
        self.Monitor.clicked.connect(self.activate_pulse_monitor)
    def activate_TLset(self):
        try:
            os.popen('activate artiq-kasli && d: && cd D:/artiq-kasli/artiq-master && python timeline_set_gui20.py')
        except Exception as e:
            print(e)
    def activate_DCset(self):
        os.popen('cd D:/artiq-kasli/artiq-master && python DC_set1_1.py')
    def activate_pulse_monitor(self):
        os.popen('cd D:/artiq-kasli/artiq-master && python pulse_monitor_window.py')
    def run_timeline(self):
        roundtime=self.Roundtime.value()
        expid1 = dict(
        file = 'repository/auto_code/output_test02.py',
        class_name = 'code',
        log_level=logging.DEBUG,
        arguments=None
        )
        expid_test = dict(
        file = 'repository/example/arguments_demo.py',
        class_name = 'ArgumentsDemo2',
        log_level=logging.DEBUG,
        arguments=None
        )
        try:
            for i in range(roundtime):
                rid = schedule.submit(
                pipeline_name='main', expid=expid1, priority=0, due_date=None, flush=False)
        except Exception as e:
            print(e)
            return
            
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a = mainprogram()
    a.show()
    sys.exit(app.exec_()) 

