#!/usr/bin/env python

access_template = ['switchport mode access',                   
'switchport access vlan %d',                   
'switchport nonegotiate',                   
'spanning-tree portfast',                   
'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
'switchport mode trunk',
'switchport trunk allowed vlan %s']



a = raw_input ("Enter interface mode (access/trunk): ");
b = raw_input ("Enter interface type and number: ");

if a == 'access':
    c = raw_input ("Enter VLAN number: ");
else:
    c = raw_input ("Enter allowed VLANs: ");

if a == 'access':
    print ("Interface %s" % b)
    print '\n'.join(access_template) % int(c)
        
elif a == 'trunk':
    print ("Interface %s" % b)
    print '\n'.join(trunk_template) % c
