import os
import time

os.popen('activate artiq-kasli && d: && cd D:/artiq-kasli/artiq-master && artiq_master')
os.popen('activate artiq-kasli && d: && cd D:/artiq-kasli/artiq-master && artiq_dashboard')
time.sleep(1)
os.popen('activate artiq-kasli && d: && cd D:/artiq-kasli && python main_control.py')
#os.popen('activate artiq-kasli && d: && cd D:/artiq-kasli/artiq-master && python pulse_monitor_window.py')
        