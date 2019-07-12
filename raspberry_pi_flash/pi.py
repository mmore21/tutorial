import time
import os
import subprocess

strP = "RASPBERRY PI"
length = ""


while(True):
    subprocess.call("./raspi-motd.sh", shell=True)
    time.sleep(0.5)
    os.system('clear')
    time.sleep(0.5)
