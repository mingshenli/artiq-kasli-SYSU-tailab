# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:52:24 2019

@author: 18926
"""

from hardwarelib import hardwarelist, dc_16chan 
class scan(object):
    def __init__(self):
        self.hardware=hardwarelist()
        self.HardwareList=self.hardware.hardware
        
        self.DC_16chan=dc_16chan()
#        self.DC16chan.DC1(5)
    def run(self,roundtime=1,pa_lib=None):
        pam_number=len(pa_lib)
        for cycle in range(roundtime):
            for pa in range(pam_number):
                    getattr(getattr(self,pa_lib[pa][0]),pa_lib[pa][1])(pa_lib[pa][2]+(cycle)*pa_lib[pa][3])
        
        


if __name__=='__main__':
    A=scan()
    A.run(5,[['DC_16chan','DC1',0,0.1],['DC_16chan','DC16',3,0.2]])
