# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:43:13 2018

@author: 18926
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,copy
from RFsocketcontral_import import MainWindow
from socket import *
class mainprogram(MainWindow):
    global RFcheck,host,port,s1,s2,s3,s4,s5,s6
    port = 5025
    RFcheck=[0,0,0,0,0,0]
    host=['','','','','','']
    def __init__(self):
        super().__init__()
        self.sendorder.clicked.connect(self.sendnetorder)
        self.RF_on.clicked.connect(self.RFon)
        self.RF_off.clicked.connect(self.RFoff)
        self.RF_1.append('192.168.1.113')
        self.RF_2.append('192.168.1.156')
        self.RF_3.append('192.168.1.157')
        self.RF_4.append('192.168.1.158')
        self.RF_5.append('192.168.1.159')
        self.RF_6.append('192.168.1.160')
        host[0]=self.RF_1.toPlainText()
        host[1]=self.RF_2.toPlainText()
        host[2]=self.RF_3.toPlainText()
        host[3]=self.RF_4.toPlainText()
        host[4]=self.RF_5.toPlainText()
        host[5]=self.RF_6.toPlainText()
       
    def RFon(self):
        RFcheck[0]=self.RFcheck_1.checkState()
        RFcheck[1]=self.RFcheck_2.checkState()
        RFcheck[2]=self.RFcheck_3.checkState()
        RFcheck[3]=self.RFcheck_4.checkState()
        RFcheck[4]=self.RFcheck_5.checkState()
        RFcheck[5]=self.RFcheck_6.checkState()
        for i in range(6):
            if RFcheck[i]==2:
#                name='s'+str(i+1)
                locals()['s'+str(i+1)]=socket(AF_INET, SOCK_STREAM)
                locals()['s'+str(i+1)].settimeout(1)           #响应时间
                try:
                    locals()['s'+str(i+1)].connect((host[i], port))             # 连接到服务器
                    locals()['s'+str(i+1)].send(b'ENBR1\n')
                    locals()['s'+str(i+1)].close()
                except:
                    self.text_state.append('RF'+str(i+1)+'net connect failed in '+str(host[i]))
    def RFoff(self):
        RFcheck[0]=self.RFcheck_1.checkState()
        RFcheck[1]=self.RFcheck_2.checkState()
        RFcheck[2]=self.RFcheck_3.checkState()
        RFcheck[3]=self.RFcheck_4.checkState()
        RFcheck[4]=self.RFcheck_5.checkState()
        RFcheck[5]=self.RFcheck_6.checkState()
        for i in range(6):
            if RFcheck[i]==2:
#                name='s'+str(i+1)
                locals()['s'+str(i+1)]=socket(AF_INET, SOCK_STREAM)
                locals()['s'+str(i+1)].settimeout(1)           #响应时间
                try:
                    locals()['s'+str(i+1)].connect((host[i], port))             # 连接到服务器
                    locals()['s'+str(i+1)].send(b'ENBR0\n')
                    locals()['s'+str(i+1)].close()
                except:
                    self.text_state.append('RF'+str(i+1)+'net connect failed in '+str(host[i]))
       
       
        
                
                
    def sendnetorder(self):
#        for i in range(6):
#            DCcheck[i]=locals()['RFcheck'+str(i+1)].checkState()
        RFcheck[0]=self.RFcheck_1.checkState()
        RFcheck[1]=self.RFcheck_2.checkState()
        RFcheck[2]=self.RFcheck_3.checkState()
        RFcheck[3]=self.RFcheck_4.checkState()
        RFcheck[4]=self.RFcheck_5.checkState()
        RFcheck[5]=self.RFcheck_6.checkState()
        order=self.text_order.toPlainText()
        for i in range(6):
            if RFcheck[i]==2:
#                name='s'+str(i+1)
                locals()['s'+str(i+1)]=socket(AF_INET, SOCK_STREAM)
#                locals()['s'+str(i+1)].settimeout(1)           #响应时间
                try:
                    locals()['s'+str(i+1)].connect((host[i], port))             # 连接到服务器
                    locals()['s'+str(i+1)].send(b'%d\n','ENBR0')
                    locals()['s'+str(i+1)].clise()
                except:
                    self.text_state.append('RF'+str(i+1)+'net connect failed in '+str(host[i]))
            
            
            
         
        
       
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a = mainprogram()
    a.show()
    sys.exit(app.exec_()) 