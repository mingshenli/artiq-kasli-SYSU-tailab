# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 17:46:45 2018

@author: 18926
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:28:49 2018

@author: 18926
"""

import sys
import select

from artiq.experiment import *


def chunker(seq, size):
    res = []
    for el in seq:
        res.append(el)
#        print("      this is what def chunker do to the chunker(self.urukuls,4)",res)
        if len(res) == size:
            yield res
            res = []
    if res:
        yield res


def is_enter_pressed() -> TBool:
    if select.select([sys.stdin,], [], [], 0.0)[0]:
        sys.stdin.read(1)
        return True
    else:
        return False


class KasliTester(EnvExperiment):
    def build(self):
        # hack to detect artiq_run
        if self.get_device("scheduler").__class__.__name__ != "DummyScheduler":
            raise NotImplementedError(
                "must be run with artiq_run to support keyboard interaction")

        self.setattr_device("core")
        self.urukul_cplds = dict()
        self.urukuls = dict()
    
        ddb = self.get_device_db()
#      
        for name, desc in ddb.items():
            if isinstance(desc, dict) and desc["type"] == "local":
                module, cls = desc["module"], desc["class"]
    
                if (module, cls) == ("artiq.coredevice.urukul", "CPLD"):
                    self.urukul_cplds[name] = self.get_device(name)
                    print("this is self.urulul_cplds[name]",self.get_device(name))
                elif (module, cls) == ("artiq.coredevice.ad9910", "AD9910"):
                    self.urukuls[name] = self.get_device(name)
                elif (module, cls) == ("artiq.coredevice.ad9912", "AD9912"):
                    self.urukuls[name] = self.get_device(name)
                
        ddb = self.get_device_db()
        for name, desc in ddb.items():
            if isinstance(desc, dict) and desc["type"] == "local":
                module, cls = desc["module"], desc["class"]
                if ((module, cls) == ("artiq.coredevice.ad9910", "AD9910")
                    or (module, cls) == ("artiq.coredevice.ad9912", "AD9912")):
                    sw_device = desc["arguments"]["sw_device"]
#                    del self.ttl_outs[sw_device]
                elif (module, cls) == ("artiq.coredevice.urukul", "CPLD"):
                    io_update_device = desc["arguments"]["io_update_device"]
#                    del self.ttl_outs[io_update_device]
#                elif (module, cls) == ("artiq.coredevice.sampler", "Sampler"):
#                    cnv_device = desc["arguments"]["cnv_device"]
#                    del self.ttl_outs[cnv_device]
#                elif (module, cls) == ("artiq.coredevice.zotino", "Zotino"):
#                    ldac_device = desc["arguments"]["ldac_device"]
#                    clr_device = desc["arguments"]["clr_device"]
#                    del self.ttl_outs[ldac_device]
#                    del self.ttl_outs[clr_device]

        # Sort everything by RTIO channel number
       
        self.urukuls = sorted(self.urukuls.items(), key=lambda x: x[1].sw.channel)
        

    @kernel
    def init_urukul(self, cpld):
        self.core.break_realtime()
        cpld.init()
        

    @kernel
    def setup_urukul(self, channel, frequency):
        self.core.break_realtime()
        channel.init()
        channel.set(frequency*MHz)
        channel.sw.on()
        channel.set_att(6.)

 
    # We assume that RTIO channels for switches are grouped by card.
    def test_urukuls(self):
        print("*** Testing Urukul DDSes.")

        print("Initializing CPLDs...")
        for name, cpld in sorted(self.urukul_cplds.items(), key=lambda x: x[0]):
            print(name + "...")
            self.init_urukul(cpld)
        print("...done")
#        print("       this is self.urukul_cplds",self.urukul_cplds)
        
        print("Frequencies:")
        for card_n, channels in enumerate(chunker(self.urukuls, 4)):
            for channel_n, (channel_name, channel_dev) in enumerate(channels):
#                frequency = 10*(card_n + 1) + channel_n
                frequency=1
                print("{}\t{}MHz".format(channel_name, frequency))
                print(card_n,channel_n)
                self.setup_urukul(channel_dev, frequency)
        print("Press ENTER when done.")
        input()

        print("Testing RF switch control. Press ENTER when done.")
        

    def run(self):
        print("****** Kasli system tester ******")
        print("")
        self.core.reset()
        self.test_urukuls()

        
        
