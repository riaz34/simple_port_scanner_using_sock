#!//usr/bin/python

import socket

target=input("enter the ipaddress: ")
port_rg=input("enter the port range: ")

low=int(port_rg.split('-')[0])
high=int(port_rg.split('-')[1])
print('########################################################################')
print('target ip:',target,'scanning start from:',low,' scanning end at: ',high)
print('########################################################################')
print('/n/n')
for port in range(low, high+1):
  s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  status=s.connect_ex((target,port))
  if (status==0):
    print('port:',port,'*open*')
  else:
    print('port:',port'closed :)')
