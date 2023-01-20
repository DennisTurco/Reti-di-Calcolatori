#!/usr/bin/env python

# Dennis Turco
# date: 20/11/2022
# summary

from socket import *
import sys, time
import optparse

name = "Dennis"
surname = "Turco"

parser = optparse.OptionParser()
parser.add_option('-s', '--server',   dest="server",  default="", help="server name (default localhost)" )
parser.add_option('-p', '--port',     dest="port",    default=10102, type=int, help="server listening port" )
parser.add_option('-b', '--bufsize',  dest="bufsize", default=100,  type=int, help="delivery buffer size" )
options, remainder = parser.parse_args()
print ("OPTIONS  server:", options.server, " - port:", options.port, " - bufsize:", options.bufsize)

addr = (options.server, options.port)
s = socket(AF_INET, SOCK_DGRAM)

ta = time.time()

Len = s.sendto(f"hello from {name} {surname}, in python".encode('utf-8'), addr) 
#Len = s.sendto("hello".encode('utf-8'), addr) 

print ("sent ", Len, " Bytes \n")

tb = time.time()
print ("time :", tb-ta)

s.close()