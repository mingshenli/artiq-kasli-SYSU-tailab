# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\program\qtsesigner\timeline_vi.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_timeline_vi(object):
    def setupUi(self, timeline_vi):
        timeline_vi.setObjectName("timeline_vi")
        timeline_vi.resize(1342, 833)
        self.centralwidget = QtWidgets.QWidget(timeline_vi)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 0, 93, 28))
        self.pushButton.setObjectName("pushButton")
        timeline_vi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(timeline_vi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1342, 26))
        self.menubar.setObjectName("menubar")
        timeline_vi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(timeline_vi)
        self.statusbar.setObjectName("statusbar")
        timeline_vi.setStatusBar(self.statusbar)

        self.retranslateUi(timeline_vi)
        QtCore.QMetaObject.connectSlotsByName(timeline_vi)

    def retranslateUi(self, timeline_vi):
        _translate = QtCore.QCoreApplication.translate
        timeline_vi.setWindowTitle(_translate("timeline_vi", "MainWindow"))
        self.pushButton.setText(_translate("timeline_vi", "PushButton"))

