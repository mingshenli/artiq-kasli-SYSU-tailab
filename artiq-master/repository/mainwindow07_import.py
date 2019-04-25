# -*- coding: utf-8 -*-
"""
Created on Fri May 18 20:44:04 2018

@author: 18926
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from gui_test07_window import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
 