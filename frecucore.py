#!/usr/bin/python3
'''Medicion de la frecuencia por segundo de la cpu, usarlo como SUDO'''
import os
from time import sleep
import sys
print("-----^C to exit-----")
print("Recuerda que se pueden ejecutar globalmente.....")
medida = 0
while True:
        try:
                with open("/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq") \
                     as f, open("/sys/devices/system/cpu/cpu1/cpufreq/cpuinfo_cur_freq") as g:
                        core0 = f.read()
                        core1 = g.read()
                with open("/sys/devices/system/cpu/cpu2/cpufreq/cpuinfo_cur_freq") as h, \
                     open("/sys/devices/system/cpu/cpu3/cpufreq/cpuinfo_cur_freq") as i:
                        core2 = h.read()
                        core3 = i.read()
                        medida += 1
                        print("########--Measure number {}--#################\n".format(medida))
                        print("      #CPU CORE1 FREQ %s      #CPU CORE2 FREQ %s      #CPU CORE3 FREQ %s      #CPU CORE4 FREQ %s" %(core0,core1,core2,core3))
                        sleep(1.0)
        except:
                if os.getuid() != 0:
                    print("This script requires sudo privileges, Quitting...")
                    sys.exit()
                else:
                    print("Quitting...")
                    sys.exit()
