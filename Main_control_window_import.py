# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:10:37 2019

@author: 18926
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from main_control_gui20 import Ui_MainWindow
class Main_control_window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main_control_window, self).__init__(parent)
        self.setupUi(self)  