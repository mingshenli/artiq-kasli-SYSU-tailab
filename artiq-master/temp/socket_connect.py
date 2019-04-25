# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 10:54:13 2018

@author: 18926
"""
#!/usr/bin/env python
# coding=utf8

from socket import *

host = '192.168.1.113'
port = 5025
bufsiz = 1024

s = socket(AF_INET, SOCK_STREAM)    # 开启套接字
try:
    s.connect((host, port))             # 连接到服务器
except:
    print('fail')
s.send(b"ENBR0\n")
#while True:
#    data = raw_input('> ')      # 等待输入
#    if not data:
#        break
#    tcpCliSock.send(data)       # 发送信息
#    response = tcpCliSock.recv(bufsiz)       # 接受返回信息
#    if not response:
#        break
#    print (response)

