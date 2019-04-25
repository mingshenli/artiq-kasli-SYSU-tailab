"""
利用 Clinet 工具连接 artiq_master 演示
请确保 artiq_master 已经在本机上运行，
并且在激活 artiq 的环境下用 python 执行该程序
"""

import logging
from artiq.protocols.pc_rpc import (Client)


#利用 Client 工具连接到 master
schedule, exps, datasets = [
    Client('::1', 3251, 'master_' + i) for i in 'schedule experiment_db dataset_db'.split()
    ]

# 看一下现在 master 管理的实验脚本
print('The explorer:')
for task in exps.list_directory('repository'):
    print(task)
print('--------------------')
print(' ')
    
# 假设其中有一个脚本叫做 led.py 
# 运行一下
print('Running led.py')
expid = dict(
    file = 'repository/hello.py',
    class_name = 'hello',
    log_level=logging.DEBUG,
#     如果有参数，就利用下面的方式传递参数
     arguments = dict(
         state = True,
         count =  5 )
    )
rid = schedule.submit(
    pipeline_name='main', expid=expid, priority=0, due_date=None, flush=False)
print('--------------------\n')
    
# 还可以观察现在都有什么任务在执行
print('current schedule:')
print(schedule.get_status())

# 获取实验数据
# 当然你得确保这个数据确实在 artiq_dashboard 的 dataset 上可以看到
#print(datasets.get('datas.test'))
