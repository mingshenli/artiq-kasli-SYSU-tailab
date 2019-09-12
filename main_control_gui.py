# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\18926\Desktop\qtsesigner\main_control_gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(768, 540)
        MainWindow.setMinimumSize(QtCore.QSize(0, 30))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 50))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 2, 1, 1, QtCore.Qt.AlignBottom)
        self.TLset = QtWidgets.QPushButton(self.centralwidget)
        self.TLset.setMinimumSize(QtCore.QSize(0, 100))
        self.TLset.setObjectName("TLset")
        self.gridLayout.addWidget(self.TLset, 0, 0, 1, 1)
        self.Roundtime = QtWidgets.QSpinBox(self.centralwidget)
        self.Roundtime.setMinimumSize(QtCore.QSize(0, 100))
        self.Roundtime.setMaximum(100000)
        self.Roundtime.setProperty("value", 1)
        self.Roundtime.setObjectName("Roundtime")
        self.gridLayout.addWidget(self.Roundtime, 6, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.DCset = QtWidgets.QPushButton(self.centralwidget)
        self.DCset.setMinimumSize(QtCore.QSize(0, 100))
        self.DCset.setObjectName("DCset")
        self.gridLayout.addWidget(self.DCset, 0, 2, 1, 1)
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setMinimumSize(QtCore.QSize(0, 200))
        self.Run.setObjectName("Run")
        self.gridLayout.addWidget(self.Run, 5, 0, 2, 2, QtCore.Qt.AlignBottom)
        self.Monitor = QtWidgets.QPushButton(self.centralwidget)
        self.Monitor.setMinimumSize(QtCore.QSize(0, 100))
        self.Monitor.setObjectName("Monitor")
        self.gridLayout.addWidget(self.Monitor, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 26))
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
        self.label.setText(_translate("MainWindow", "round time"))
        self.TLset.setText(_translate("MainWindow", "activate timelineSet"))
        self.pushButton.setText(_translate("MainWindow", "start count"))
        self.DCset.setText(_translate("MainWindow", "activate DCset"))
        self.Run.setText(_translate("MainWindow", "run timeline"))
        self.Monitor.setText(_translate("MainWindow", "activate pulse_monitor "))
        self.pushButton_2.setText(_translate("MainWindow", "stop count"))

