#!/usr/bin/env python

import ipaddress
import sys
import re
import ipcalc
import socket
import itertools
import re
import numpy

def common(p):
    global q
    q = list(set.intersection(*map(set, p)))
    q.sort()
    print 'List_1=%s' %q
   
def unique1(p):
    j = 0
    global gj
    gj = set()
    for i in p:
        gj = (gj.symmetric_difference(i))       
    r = set(q)
    z = list(gj.symmetric_difference(r))
    z.sort()
    print 'List_2=%s' % z

def unique2(p):
     global q
     q = list(set.symmetric_difference(*map(set, p)))
     q.sort()
     print 'List_2=%s' %q

shakes = open("command.txt", "r")
output = open("output.txt","w")

shakes.seek(0)

for line in shakes:
    if re.match("switchport trunk allowed vlan", line):
        output.write(line)
shakes.close()
output.close()

with open('output.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('switchport trunk allowed vlan ','')

# Write the file out again
with open('output1.txt', 'w') as file:
  file.write(filedata)
file.close()

shakes = open('output1.txt', 'r')
l = []
shakes.seek(0)
for line in shakes:
    l.append(line.split(','))
#print l
shakes.close()


with open('output1.txt') as f:
    x=[]
    for line in f:
        int_list = [int(i) for i in line.split(',')]
        x.append(int_list)
    #print x
    

common(x)
unique1(x)
#unique2(x)

        

