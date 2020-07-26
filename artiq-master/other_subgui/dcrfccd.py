# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:02:02 2020

@author: HP
"""

from dcrfccd_gui_import import MainWindow
import logging
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtCore import pyqtSignal
import time as t
import os
import sys,copy,re,math
import numpy as np
#import pyqtgraph as pg
import time

class mainprogram(MainWindow):
    
    
    def __init__(self):
        super().__init__()
        self.Dc_ctrl.clicked.connect(self.dc_ctrl)
        self.Rf_ctrl.clicked.connect(self.rf_ctrl)
        self.Ccd_ctrl.clicked.connect(self.ccd_ctrl)
    
    
    def DC_ctrl(self):
        print('dc')
    
    
    def RF_ctrl(self):
        print('rf')
    
    def CCD_ctrl(self):
        print('ccd')
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a = mainprogram()
    a.show()
#    b=timeline_vi()
#    b.show()
   
    sys.exit(app.exec_())
    
    
