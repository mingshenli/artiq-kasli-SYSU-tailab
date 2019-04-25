from artiq.experiment import *


class Normal(EnvExperiment):
    """ input_count_example
    """
    def build(self):
        self.setattr_device("core")
        self.setattr_device('scheduler')
        self.setattr_device("ttl1")
        self.setattr_argument("duration", # PMT 采集时间 
            NumberValue(default=0.2, unit='ms', ndecimals=3, step=0.1)) 
        
    @kernel
    def run(self):
        self.core.reset()
#        self.ttl0.input
        while not self.scheduler.check_pause():
            try:
                delay(1*ns) #单次计数完全不需要
                
                self.ttl1.gate_rising(500*ns)
                count = float(self.ttl1.count())
                delay(1*us)
#                self.set_dataset('datas.count_now', count, broadcast=True)
                print("****************************",count,"*********************************")
            except RTIOUnderflow:
                self.core.break_realtime()
                print("**********************flow********************************")