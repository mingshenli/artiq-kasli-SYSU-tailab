from artiq.experiment import*
class code(EnvExperiment):
    def build(self):
        self.setattr_device('core')
        self.setattr_device('ttl16')
        self.setattr_device('ttl17')
        self.setattr_device('ttl18')
        self.setattr_device('ttl19')
        self.setattr_device('ttl20')
        self.setattr_device('ttl21')
    @kernel
    def run(self):
        self.ttl16.on()
        delay(100.0*us)
        self.ttl16.off()
        delay(200.0*us)
        self.ttl16.on()
        delay(50.0*us)
        self.ttl17.on()
        delay(50.0*us)
        self.ttl16.off()
        delay(50.0*us)
        self.ttl17.off()
        delay(1000000.0*us)
