# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:28:07 2019

@author: 18926
"""


from artiq.protocols.pc_rpc import (Client)
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import math as m

schedule, exps, datasets = [
    Client('::1', 3251, 'master_' + i) for i in 'schedule experiment_db dataset_db'.split()
    ]
x=[]
y=[]
try:
    a=datasets.get('count_y')
except:
    datasets.set('count_x',x)
    datasets.set('count_y',y)
app = QtGui.QApplication([])
win = pg.GraphicsWindow(title="monitor")
win.resize(1000,600)
win.setWindowTitle('monitor')
pg.setConfigOptions(antialias=True)


p6 = win.addPlot(title="number")
p6.enableAutoRange('xy', True)
curve = p6.plot()
#data = np.random.normal(size=(10,1000))
y=[]
x=[]
#for i in range(100):
#    data.append(m.sin(i))
#    x.append(i)
#data=np.array(data)
#x=np.array(x)
ptr = 0
def update():
    global curve, data, ptr,x
    y.append(m.sin(ptr))
    x.append(ptr)
    
    
    
#    if len(ax)!=len(ay):
#        print('***************************error*******************************************')
#        print(m.sin(len(ax)))
    ax=np.array(datasets.get('count_x'))
    ay=np.array(datasets.get('count_y'))
    while len(ax)!=len(ay):
        ax=np.array(datasets.get('count_x'))
        ay=np.array(datasets.get('count_y'))
    curve.setData(ax,ay)
   
#    if ptr == 0:
#        p6.enableAutoRange('xy', True)  ## stop auto-scaling after the first data set is plotted
    ptr += 1
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(100)

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()