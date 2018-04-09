'''CPU TEMPERATURE PER SECOND'''
from time import sleep
import sys
print("----------^C to exit----------")
while True:
        try:
                with open("/sys/class/thermal/thermal_zone0/temp") as f:
                    print("Cpu Temperature {}'C".format(int(f.read())/1000))
                    sleep(1.0)
        except:
                print("Quitting..")
                sys.exit()

