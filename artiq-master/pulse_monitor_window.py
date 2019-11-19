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
point_t=1#默认x轴步距
windowsize=100#设置最大显示点数
#######################################################
#必须先试探dataset中是否有设置参数，没有的话再行设置
try:
    a=datasets.get('count_y')
    point_t=datasets.get('count_t')
except:
    datasets.set('count_x',x)
    datasets.set('count_y',y)
    datasets.set('count_t',point_t)
#######################################################
#######################################################
#初始化显示窗口
app = QtGui.QApplication([])
win = pg.GraphicsWindow(title="monitor")
win.resize(1000,600)
win.setWindowTitle('monitor')
pg.setConfigOptions(antialias=True)
######################################################

######################################################
#初始化画图对象
p6 = win.addPlot(title="number")
p6.enableAutoRange('xy', True)
curve = p6.plot()
######################################################
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
    y.append(m.sin(ptr))#虚拟信号用作测试
    x.append(ptr)#虚拟信号用作测试
    
#########################################################    
# 用于解决读取y数据和读取x数据时差导致的数据长度不一致（可能有新的数据写入）   
#此功能暂时没有用，直接将x轴步距传入即可
#    if len(ax)!=len(ay):
#        print('***************************error*******************************************')
#        print(m.sin(len(ax)))
#    ax=np.array(datasets.get('count_x'))
#########################################################
    ay=np.array(datasets.get('count_y'))#读取所有计数数据
    length=len(ay)#获得计数长度
    t_fulllength=np.arange(0,length*point_t,point_t)
#########################################################    
# 用于解决读取y数据和读取x数据时差导致的数据长度不一致（可能有新的数据写入）   
#此功能暂时没有用，直接将x轴步距传入即可
#    print(len(t_fulllength),len(ay))
#    while len(ax)!=len(ay):
#        ax=np.array(datasets.get('count_x'))
#        ay=np.array(datasets.get('count_y'))
#    curve.setData(ax,ay)
######################################################3
    upday=ay[max(1,len(ay)-windowsize):len(ay)-1]
    updat=t_fulllength[max(1,len(ay)-windowsize):len(ay)-1]
    curve.setData(updat,upday)
   
#    if ptr == 0:
#        p6.enableAutoRange('xy', True)  ## stop auto-scaling after the first data set is plotted
    ptr += 1
timer = QtCore.QTimer()
timer.timeout.connect(update)#更新数据函数
timer.start(100)#计时器

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()