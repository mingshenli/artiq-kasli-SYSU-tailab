# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\program\qtsesigner\main_control_gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 811)
        MainWindow.setMinimumSize(QtCore.QSize(0, 30))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 50))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TLset = QtWidgets.QPushButton(self.centralwidget)
        self.TLset.setMinimumSize(QtCore.QSize(0, 50))
        self.TLset.setMaximumSize(QtCore.QSize(16777215, 70))
        self.TLset.setObjectName("TLset")
        self.verticalLayout_2.addWidget(self.TLset)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Monitor = QtWidgets.QPushButton(self.centralwidget)
        self.Monitor.setMinimumSize(QtCore.QSize(0, 100))
        self.Monitor.setMaximumSize(QtCore.QSize(16777215, 120))
        self.Monitor.setObjectName("Monitor")
        self.horizontalLayout.addWidget(self.Monitor)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.save_count = QtWidgets.QPushButton(self.centralwidget)
        self.save_count.setObjectName("save_count")
        self.verticalLayout.addWidget(self.save_count)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.DCset = QtWidgets.QPushButton(self.centralwidget)
        self.DCset.setMinimumSize(QtCore.QSize(0, 50))
        self.DCset.setMaximumSize(QtCore.QSize(16777215, 70))
        self.DCset.setObjectName("DCset")
        self.verticalLayout_2.addWidget(self.DCset)
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setMinimumSize(QtCore.QSize(0, 50))
        self.Run.setMaximumSize(QtCore.QSize(16777215, 70))
        self.Run.setObjectName("Run")
        self.verticalLayout_2.addWidget(self.Run)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setMinimumSize(QtCore.QSize(400, 200))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_5.addWidget(self.textEdit)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.log = QtWidgets.QTextEdit(self.centralwidget)
        self.log.setMaximumSize(QtCore.QSize(16777215, 100))
        self.log.setObjectName("log")
        self.verticalLayout_10.addWidget(self.log)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.Roundtime = QtWidgets.QSpinBox(self.centralwidget)
        self.Roundtime.setMinimumSize(QtCore.QSize(100, 100))
        self.Roundtime.setMaximumSize(QtCore.QSize(150, 50))
        self.Roundtime.setMaximum(100000)
        self.Roundtime.setProperty("value", 1)
        self.Roundtime.setObjectName("Roundtime")
        self.verticalLayout_3.addWidget(self.Roundtime)
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setMinimumSize(QtCore.QSize(0, 50))
        self.add.setObjectName("add")
        self.verticalLayout_3.addWidget(self.add)
        self.clean = QtWidgets.QPushButton(self.centralwidget)
        self.clean.setObjectName("clean")
        self.verticalLayout_3.addWidget(self.clean)
        self.update_manu = QtWidgets.QPushButton(self.centralwidget)
        self.update_manu.setObjectName("update_manu")
        self.verticalLayout_3.addWidget(self.update_manu)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.hardware_name = QtWidgets.QComboBox(self.centralwidget)
        self.hardware_name.setMinimumSize(QtCore.QSize(200, 40))
        self.hardware_name.setObjectName("hardware_name")
        self.verticalLayout_4.addWidget(self.hardware_name)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.parameter = QtWidgets.QComboBox(self.centralwidget)
        self.parameter.setMinimumSize(QtCore.QSize(200, 40))
        self.parameter.setObjectName("parameter")
        self.verticalLayout_5.addWidget(self.parameter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.start_value = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.start_value.setMinimumSize(QtCore.QSize(0, 40))
        self.start_value.setMaximum(9999.0)
        self.start_value.setSingleStep(0.1)
        self.start_value.setObjectName("start_value")
        self.verticalLayout_6.addWidget(self.start_value)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.len = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.len.setMinimumSize(QtCore.QSize(0, 40))
        self.len.setMaximum(9999.0)
        self.len.setSingleStep(0.1)
        self.len.setObjectName("len")
        self.verticalLayout_7.addWidget(self.len)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.scan_mode = QtWidgets.QComboBox(self.centralwidget)
        self.scan_mode.setMinimumSize(QtCore.QSize(0, 40))
        self.scan_mode.setObjectName("scan_mode")
        self.scan_mode.addItem("")
        self.scan_mode.addItem("")
        self.verticalLayout_8.addWidget(self.scan_mode)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.run_mode = QtWidgets.QComboBox(self.centralwidget)
        self.run_mode.setObjectName("run_mode")
        self.run_mode.addItem("")
        self.run_mode.addItem("")
        self.run_mode.addItem("")
        self.horizontalLayout_7.addWidget(self.run_mode)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7, 0, QtCore.Qt.AlignRight)
        self.time_length = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.time_length.setMinimumSize(QtCore.QSize(20, 50))
        self.time_length.setMaximum(9999.0)
        self.time_length.setSingleStep(0.1)
        self.time_length.setObjectName("time_length")
        self.horizontalLayout_6.addWidget(self.time_length)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout_10, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 26))
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
        self.pushButton.setText(_translate("MainWindow", "start count"))
        self.pushButton_2.setText(_translate("MainWindow", "clear data"))
        self.save_count.setText(_translate("MainWindow", "save"))
        self.DCset.setText(_translate("MainWindow", "activate DCset"))
        self.Run.setText(_translate("MainWindow", "run timeline"))
        self.label.setText(_translate("MainWindow", "round time"))
        self.add.setText(_translate("MainWindow", "add"))
        self.clean.setText(_translate("MainWindow", "clean hardware set"))
        self.update_manu.setText(_translate("MainWindow", "update_manually"))
        self.label_2.setText(_translate("MainWindow", "hardware name"))
        self.label_3.setText(_translate("MainWindow", "parameter"))
        self.label_4.setText(_translate("MainWindow", "start value"))
        self.label_5.setText(_translate("MainWindow", "len"))
        self.label_6.setText(_translate("MainWindow", "scan_mode"))
        self.scan_mode.setItemText(0, _translate("MainWindow", "linear"))
        self.scan_mode.setItemText(1, _translate("MainWindow", "random"))
        self.run_mode.setItemText(0, _translate("MainWindow", "no artiq hardware scan manual go"))
        self.run_mode.setItemText(1, _translate("MainWindow", "no artiq hardware scan set time go"))
        self.run_mode.setItemText(2, _translate("MainWindow", "artiq with hardware set"))
        self.label_7.setText(_translate("MainWindow", "scan time length"))

