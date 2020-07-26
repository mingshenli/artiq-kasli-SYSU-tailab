# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 19:54:49 2020

@author: 18926
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from demons_gui import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
 