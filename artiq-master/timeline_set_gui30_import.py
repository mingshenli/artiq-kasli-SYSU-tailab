# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 21:57:20 2019

@author: 18926
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from gui_window.timeline_set_gui30_window import Ui_MainWindow
from gui_window.timeline_vi import Ui_timeline_vi


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
class timeline_vi_window(QtWidgets.QMainWindow, Ui_timeline_vi):
    def __init__(self, parent=None):
        super(timeline_vi_window, self).__init__(parent)
        self.setupUi(self)
 