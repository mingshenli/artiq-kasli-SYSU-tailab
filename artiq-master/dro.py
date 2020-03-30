# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 16:40:07 2019

@author: 18926
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QSpinBox,QDialog,QMainWindow
import sys
import pyqtgraph as pg
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(619, 182)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.check_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_1.setObjectName("check_1")
        self.verticalLayout.addWidget(self.check_1)
        self.Button_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_1.setObjectName("Button_1")
        self.verticalLayout.addWidget(self.Button_1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.check_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_2.setObjectName("check_2")
        self.verticalLayout_2.addWidget(self.check_2)
        self.Button_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_2.setObjectName("Button_2")
        self.verticalLayout_2.addWidget(self.Button_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.check_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_3.setObjectName("check_3")
        self.verticalLayout_3.addWidget(self.check_3)
        self.Button_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_3.setObjectName("Button_3")
        self.verticalLayout_3.addWidget(self.Button_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.check_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_4.setObjectName("check_4")
        self.verticalLayout_4.addWidget(self.check_4)
        self.Button_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_4.setObjectName("Button_4")
        self.verticalLayout_4.addWidget(self.Button_4)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.check_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_5.setObjectName("check_5")
        self.verticalLayout_5.addWidget(self.check_5)
        self.Button_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_5.setObjectName("Button_5")
        self.verticalLayout_5.addWidget(self.Button_5)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_12.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.check_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_6.setObjectName("check_6")
        self.verticalLayout_6.addWidget(self.check_6)
        self.Button_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_6.setObjectName("Button_6")
        self.verticalLayout_6.addWidget(self.Button_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.check_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_7.setObjectName("check_7")
        self.verticalLayout_7.addWidget(self.check_7)
        self.Button_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_7.setObjectName("Button_7")
        self.verticalLayout_7.addWidget(self.Button_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.check_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_8.setObjectName("check_8")
        self.verticalLayout_8.addWidget(self.check_8)
        self.Button_8 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_8.setObjectName("Button_8")
        self.verticalLayout_8.addWidget(self.Button_8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.check_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_9.setObjectName("check_9")
        self.verticalLayout_9.addWidget(self.check_9)
        self.Button_9 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_9.setObjectName("Button_9")
        self.verticalLayout_9.addWidget(self.Button_9)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.check_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_10.setObjectName("check_10")
        self.verticalLayout_10.addWidget(self.check_10)
        self.Button_10 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_10.setObjectName("Button_10")
        self.verticalLayout_10.addWidget(self.Button_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout_12.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.check_11 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_11.setObjectName("check_11")
        self.verticalLayout_11.addWidget(self.check_11)
        self.Button_11 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_11.setObjectName("Button_11")
        self.verticalLayout_11.addWidget(self.Button_11)
        self.horizontalLayout_3.addLayout(self.verticalLayout_11)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 619, 26))
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
        self.check_1.setText(_translate("MainWindow", "Dro01"))
        self.Button_1.setText(_translate("MainWindow", "Dro01"))
        self.check_2.setText(_translate("MainWindow", "Dro02"))
        self.Button_2.setText(_translate("MainWindow", "Dro02"))
        self.check_3.setText(_translate("MainWindow", "Dro03"))
        self.Button_3.setText(_translate("MainWindow", "Dro03"))
        self.check_4.setText(_translate("MainWindow", "Dro04"))
        self.Button_4.setText(_translate("MainWindow", "Dro04"))
        self.check_5.setText(_translate("MainWindow", "Dro05"))
        self.Button_5.setText(_translate("MainWindow", "Dro05"))
        self.check_6.setText(_translate("MainWindow", "Dro06"))
        self.Button_6.setText(_translate("MainWindow", "Dro06"))
        self.check_7.setText(_translate("MainWindow", "Dro07"))
        self.Button_7.setText(_translate("MainWindow", "Dro07"))
        self.check_8.setText(_translate("MainWindow", "Dro08"))
        self.Button_8.setText(_translate("MainWindow", "Dro08"))
        self.check_9.setText(_translate("MainWindow", "Dro09"))
        self.Button_9.setText(_translate("MainWindow", "Dro09"))
        self.check_10.setText(_translate("MainWindow", "Dro10"))
        self.Button_10.setText(_translate("MainWindow", "Dro10"))
        self.check_11.setText(_translate("MainWindow", "Dro_select"))
        self.Button_11.setText(_translate("MainWindow", "Dro_select"))
        
        
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)  
        
        
class mainprogram(MainWindow):
    def __init__(self):
        super().__init__()  
        self.Button_1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a = mainprogram()
    a.show()
    sys.exit(app.exec_()) 