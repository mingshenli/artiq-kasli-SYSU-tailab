#from artiq.experiment import *
from gui.timeline_set_gui import mainprogram as time_gui
from artiq.experiment import *
import logging
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,copy
import os
import time
class start_gui(EnvExperiment):
    """start_gui"""
    def build(self):
        pass
    def run(self):
#        app = QtWidgets.QApplication(sys.argv)
#        a =time_gui()
#        a.show()
#        sys.exit(app.exec_())
        os.system('activate artiq-kasli && d: &&  cd D:/artiq-kasli/artiq-master && python timeline_set_gui.py' )
        
        
        
