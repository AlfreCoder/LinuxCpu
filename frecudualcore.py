#!/usr/bin/python3
'''Measure of a dualcore cpu frecuency, requires SUDO privileges'''
import os
from time import sleep
import sys
print("-----^C to exit-----\n")
medida = 0
while True:
        try:
                with open("/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq") \
                     as f, open("/sys/devices/system/cpu/cpu1/cpufreq/cpuinfo_cur_freq") as g:
                        core0 = f.read()
                        core1 = g.read()
                        cores = [core0,core1]
                        medida += 1
                        print("<><><><><>--Measure number {}--<><><><><><>\n".format(medida))
                        for i in range(0,len(cores)):
                                print("> Core{} CPU frequency in Mhz: {}".format(i+ 1, cores[i]))
                        print("<><><><><><><><><><><><><><><><><><><><><>\n\n\n")
                        sleep(1.5)
                        
        except:
                if os.getuid() != 0:
                    print("This script requires sudo privileges, Quitting...")
                    sys.exit()
                else:
                    print("Quitting...")
                    sys.exit()
