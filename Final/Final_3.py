import ipaddress
import sys
import re
import ipcalc
import socket
import itertools
import re
import numpy


shakes = open("ShowIpRoute.txt", "r")
output = open("output3.txt","w")

for line in shakes:
    if re.search("via", line):
        output.write(line)
shakes.close()
output.close()

shakes = open("output3.txt", "r")
split = []
i = 1
for line in shakes:
    split = re.split(' ', line)
#    print split[0]
    i = i + 1

    if split [0] == 'D':
        print "Protocol: EIGRP"
        print "Prefix: %s " % split[1]
        print "AD/Metric: %s " % split[3]
        print "Next-Hop: %s " % split[5]
        print "Last update: %s " % split[7]
        print "Outbound interface: %s" % split [8]


    elif split [0] == 'O':
        print "Protocol: OSPF"
        print "Prefix: %s " % split[2]
        print "AD/Metric: %s " % split[4]
        print "Next-Hop: %s " % split[6]
        print "Last update: %s " % split[8]
        print "Outbound interface: %s" % split [9]

    elif split [0] == 'E':
        print "Protocol: EGP "
        print "Prefix: %s " % split[1]
        print "AD/Metric: %s " % split[3]
        print "Next-Hop: %s " % split[5]
        print "Last update: %s " % split[7]
        print "Outbound interface: %s" % split [8]

    
shakes.close()


