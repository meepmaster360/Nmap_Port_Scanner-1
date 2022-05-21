import os
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

os.system("clear")

re = Fore.RED
bl = Fore.BLUE
wh = Fore.WHITE
ma = Fore.MAGENTA
cy = Fore.CYAN

print(re + "| Made By WebRoa |" + bl + " | Nmap Port Scanner |" + ma + " | NPS |")
print(wh + """
     _   _ _____   _____ 
    | \ | |  __ \ / ____|
    |  \| | |__) | (___  
    | . ` |  ___/ \___ \ 
    | |\  | |     ____) |
    |_| \_|_|    |_____/ 
                      
                      
""")

print(cy)
print("I Will Need IP Address To Scan For Open Ports")
ip = input("Enter IP Address: ")
port = input("Port You Want To Scan For: ")
print("Starting Port Scanning")
time.sleep(1)
os.system("nmap " + ip + " -p " + port)
time.sleep(1000000)