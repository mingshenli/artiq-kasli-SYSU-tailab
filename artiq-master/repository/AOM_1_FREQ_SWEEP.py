# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:09:22 2020

@author: HP
"""
from socket import *
import numpy as np
import logging
import time
from artiq.protocols.pc_rpc import (Client)
schedule, exps, datasets = [
    Client('::1', 3251, 'master_' + i) for i in 'schedule experiment_db dataset_db'.split()
    ]


##############################################################################扫频初始化
#fre=[]
#for i in np.arange(21,29,0.8):             #修改扫描频率范围和步长
#    fr="FREQ"+str(i)+"MHZ\n"
#    fre.append(fr.encode())
#host="192.168.1.109"
#port=5025
#s=socket(AF_INET,SOCK_STREAM)
#s.connect((host,port))
#s.send(b'AMPR -10\n')                     #控制幅度
#s.close()
#s=socket(AF_INET,SOCK_STREAM)
#s.connect((host,port))
#s.send(b'ENBR1\n')                         #0表示不输出，1表示输出信号
#s.close()
##############################################################################扫频初始化
########################################################################计数初始化
datasets.set("count_y",[])


scanlength=1
scan_point_length=5
for j in np.arange(0,scanlength,1):                #控制扫描次数和扫描时间
    for i in np.arange(0,scan_point_length,1):           #控制扫描点数和步长对应
        #############################################################################变频
#        s=socket(AF_INET,SOCK_STREAM)
#        s.connect((host,port))
#        s.send(fre[i])
#        s.close()
#        start=time.clock()
#        
#        #############################################################################变频
#        #################################################################################等待
#        t=1                                     #控制每个频率停留时间
#        while True:
#            end=time.clock ()
#            if  float(end-start)>=t:
#                break
        #################################################################################等待
        ##################################################################################count
        expid1 = dict(
        file = 'repository/count/input_count_32.py',
        class_name = 'inputtest',
        log_level=logging.DEBUG,
        arguments=None
        )
        
        rid = schedule.submit(
           pipeline_name='main', expid=expid1, priority=0, due_date=None, flush=False)
        ###################################################################################count
        time.sleep(1)############################################要留足够长的时间给count执行和写数据
        print('now scan at',i)
        
#################################################关闭网口        
#s=socket(AF_INET,SOCK_STREAM)
#s.connect((host,port))
#s.send(b'ENBR1\n')
#s.close()
#################################################关闭网口  
        
        
############################################读取数据
time.sleep(5)############################################要留足够长的时间给count执行和写数据
count=datasets.get("count_y")
print(count)  