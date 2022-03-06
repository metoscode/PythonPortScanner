#!/usr/bin/Python3

import socket
from IPy import IP

def scan(target):
    convertedIP = checkIP(target)
    print('\n' + '[Scanning Target]' + str(target))
    for port in range(1,100):
        portScanner(convertedIP, port)


def checkIP(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)


def getBanner(sock):
    return sock.recv(1024)


def portScanner(ipaddress, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect((ipaddress, port))
        try:
            banner = getBanner(s)
            print("Open Port " + str(port) + " : " + str(banner.decode().strip('\n')))
        except:
             print("Open Port " + str(port))
    except:
        pass

hosts = input("Enter the target(s) you want to scan(separate multiple targets with ,): ")
if ',' in hosts:
    for ip_add in hosts.split(','):
        scan(ip_add.strip(' '))
else:
    scan(hosts)