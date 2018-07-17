#!/usr/bin/env python

import ipaddress
import sys
import re
import ipcalc
import socket

def enter_ip():
    global ip
    ip = raw_input ("Enter Ip address:");
    check_ip(ip)

def enter_mask():
    global mask
    global p
    mask = raw_input("Enter subnet mask in decimal format:");
    p = int(mask)
    check_mask(p) 

def check_ip(ip):
	parts=ip.split(".")
	if len(parts)<4 or len(parts)>4:
		return False
	else:
		while len(parts)== 4:
			a=int(parts[0])
			b=int(parts[1])
			c=int(parts[2])
			d=int(parts[3])
			if a<= 0 or a>=255:
				return False
			elif b>=255 or b<0:	
				return False
			elif c>=255 or c<0:
				return False
			elif d>=255 or d<0:
				return False
			else:
				return True
			    
def check_mask(p):
    if (p < 1 or p > 32):
        return False
        enter_mask()
    else:
        return True
  
        
def output(ip):
    teams_list = ip.split(".")
    row_format = "{:>9}" * (len(teams_list) + 1)
    print row_format.format("", *teams_list)
    b = []
    for x in ip.split("."):
        b.append('{0:08b}'.format(int(x)))
    print row_format.format("", *b)

enter_ip()
if check_ip(ip) == False:
    print "Invalid IP Address"
    enter_ip()
enter_mask()
if check_mask(p) == False:
    print "Invalid Mask"
    enter_mask()   
output(ip)

res = ip + '/' + mask;
subnet = ipcalc.Network(res)
print "network address is: %s/%s" % (str(subnet.network()), mask)
print "broadcast address is: %s/%s" % (str(subnet.broadcast()), mask)
