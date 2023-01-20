#!/usr/bin/env python

# Dennis Turco
# Data: 20/11/2022
# Summary :

from socket import *
import sys, time
import optparse

name = "Dennis"
surname = "Turco"

parser = optparse.OptionParser()
parser.add_option('-s', '--server',  dest="server",  default="localhost", help="server name" )
parser.add_option('-p', '--port',    dest="port",    type=int,  default=10102, help="server listening port" )
parser.add_option('-m', '--message', dest="message", default=f"hello from {name} {surname}, in python", help="message to send")
options, remainder = parser.parse_args()
print ("OPTIONS  server:", options.server, " - port:", options.port, " - message:", options.message)

addr = (options.server,options.port)
s = socket(AF_INET,SOCK_STREAM)

s.connect(addr)

print ("Connected to server: ", addr) 
messaggio = input('message (q to quit) > ')
while messaggio.upper() != 'Q' and len(messaggio) > 0:
	s.send(messaggio.encode())
	risposta = s.recv(1500).decode()
	print ("Server response: ", risposta)
	messaggio = input('message (q to quit) > ')
s.close()