from artiq.experiment import *


class TerminateAll(EnvExperiment):
    def build(self):
        self.setattr_device("scheduler")
        self.setattr_argument("graceful_termination", BooleanValue(True))

    def run(self):
        if self.graceful_termination:
            terminate = self.scheduler.request_termination#只会响应内部写好的判断（if self.check_pulse()
        else:
            terminate = self.scheduler.delete#粗暴停止

        for rid in self.scheduler.get_status().keys():#知道有哪些任务正在运行
            if rid != self.scheduler.rid:
                terminate(rid)
