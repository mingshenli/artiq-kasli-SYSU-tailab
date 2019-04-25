# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 21:57:20 2019

@author: 18926
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from timeline_set_gui_window import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
 