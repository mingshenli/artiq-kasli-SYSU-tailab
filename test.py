# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:52:01 2019

@author: 18926
"""

from hardwarelib import hardwarelist, dc_16chan,SG382

class A(object):
    def __init__(self):
        self.DC_16chan=dc_16chan()
    def run(self):
        re=getattr(self.DC_16chan,'te')(1)
#        re=self.DC_16chan.te()
        print(re)
        
        
a=A()
a.run()