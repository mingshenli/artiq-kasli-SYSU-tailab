"""
利用 Clinet 工具连接 artiq_master 演示
请确保 artiq_master 已经在本机上运行，
并且在激活 artiq 的环境下用 python 执行该程序
"""

import logging
from artiq.protocols.pc_rpc import (Client)
schedule, exps, datasets = [
    Client('::1', 3251, 'master_' + i) for i in 'schedule experiment_db dataset_db'.split()
    ]
from artiq.experiment import *

class inputtest(EnvExperiment):
    '''client01'''
    def build(self):
        pass
    
    def run(self):
        expid = dict(
            file = 'repository/count/input_count_2.1.py',
            class_name = 'inputtest',
            log_level=logging.DEBUG,
            arguments=None
        )
    
        r1=schedule.submit(
            pipeline_name='monitor', expid=expid, priority=0, due_date=None, flush=False)
           
         
            



