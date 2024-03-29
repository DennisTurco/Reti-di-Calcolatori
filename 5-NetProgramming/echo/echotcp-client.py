#!/usr/bin/env python

# Dennis Turco
# Data: 20/11/2022
# Summary:

from socket import *
import sys, time
import optparse

name = "Dennis"
surname = "Turco"

parser = optparse.OptionParser()
parser.add_option('-s', '--server',  dest="server",  default="localhost", help="server name" )
parser.add_option('-p', '--port',    dest="port",    type=int,  default=10102, help="server listening port" )
parser.add_option('-m', '--message', dest="message", default=f"hello from {surname}, in python".encode('utf-8'), help="message to send")
options, remainder = parser.parse_args()
print ("OPTIONS  server:", options.server, " - port:", options.port, " - message:", options.message)

addr = (options.server,options.port)
s = socket(AF_INET,SOCK_STREAM)

s.connect(addr)
print("Connected to server: ", addr)
messaggio = "hello"
print("Send message: ", messaggio)
s.send(messaggio.encode())
risposta = s.recv(1500).decode()
#print (type(risposta))
print("Server response: ", risposta)
s.close()