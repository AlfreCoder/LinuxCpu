#!/usr/bin/python3
'''Measure of cpu Frecuency per second.Requires Sudo privileges'''
import os
from time import sleep
import sys
print("---------^C to exit---------")
while True:
        try:
                with open("/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq") \
                     as f:
                        print("Current cpu freq in Mhz--> {}".format(f.read()))
                        sleep(1.0)
        except:
                if os.getuid() != 0:
                    print("This script requires sudo privileges, Quitting...")
                    sys.exit()
                else:
                    print("Quitting...")
                    sys.exit()
