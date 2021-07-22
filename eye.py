#!//usr/bin/python

import socket

ip = raw_input("Enter the ip address:")

port = input("Enter the port:")

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

if sock.connect_ex((ip,port)):
       print("#####################################################")
       print "Port",port,"is closed :("
       print("#####################################################")
else:
         print("#####################################################") 
         print "Port",port,"is OPEN :)"
         print("#####################################################")
