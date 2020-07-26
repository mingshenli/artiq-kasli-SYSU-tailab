# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:00:43 2020

@author: HP
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from dcrfccd_gui import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)