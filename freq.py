#!/usr/bin/python3
'''Measure the Frequency of dual-cores and quad-cores processors'''
import os, sys
from time import sleep
from pathlib import Path
print("****************^C to exit****************\n")
medida = 0
#paths to cpu cores
path0 = Path('/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq')
path1 = Path('/sys/devices/system/cpu/cpu1/cpufreq/cpuinfo_cur_freq')
path2 = Path('/sys/devices/system/cpu/cpu2/cpufreq/cpuinfo_cur_freq')
path3 = Path('/sys/devices/system/cpu/cpu3/cpufreq/cpuinfo_cur_freq')
if path2.exists() == False:
    print("Checking frequency in a DualCore Processor...\n")
elif path2.exists():
    print("Checking frequency in a QuadCore Processor...\n")

while True:
    if path2.exists() == False:
        try:
            with open(path0) as f, open(path1) as g:
                        core0 = int(f.read())
                        core1 = int(g.read())
                        cores = [core0,core1]
                        medida += 1
                        print("<><><><><>--Measure number {}--<><><><><><>\n".format(medida))
                        for i in range(0,len(cores)):
                                # // 1000 if your cpu is in a non decimal range of frequency
                                print("> Core{} CPU frequency in Mhz: {}".format(i+ 1, cores[i] / 1000))
                        print("<><><><><><><><><><><><><><><><><><><><><>\n\n\n")
                        sleep(1.5)
                        
        except:
                if os.getuid() != 0:
                    print("This script requires sudo privileges, Quitting...")
                    sys.exit()
                else:
                    print("Quitting...")
                    sys.exit()
    elif path2.exists():
        try:
            with open(path0) as f, open(path1) as g:
                    core0 = int(f.read())
                    core1 = int(g.read())
            with open(path2) as h, open(path3) as i:
                    core2 = int(h.read())
                    core3 = int(i.read())
                    cores = [core0, core1, core2, core3]
                    medida += 1
                    print("<><><><><>--Measure number {}--<><><><><><>\n".format(medida))
                    for i in range(0,len(cores)):
                            print("> Core{} CPU frequency in Mhz: {}".format(i+ 1, cores[i] / 1000))
                    print("<><><><><><><><><><><><><><><><><><><><><>\n\n\n")
                    sleep(1.5)
                        
        except:
            if os.getuid() != 0:
                print("This script requires sudo privileges, Quitting...")
                sys.exit()
            else:
                print("Quitting...")
                sys.exit()
