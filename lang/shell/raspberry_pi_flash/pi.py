import time
import os
import subprocess

strP = "RASPBERRY PI"
length = ""


while(True):
    subprocess.call("./raspberry_pi.sh", shell=True)
    time.sleep(0.5)
    os.system('clear')
    time.sleep(0.5)
