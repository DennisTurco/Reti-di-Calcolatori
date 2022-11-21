# Author: Dennis Turco
# compile: python gethostbyname.py nost_name
# example: python gethostbyname.py www.google.com

import socket  # socket library
import sys  # sys library for get parameters from command line


# check parameters list
if len(sys.argv) < 2:
    host = "142.250.184.36"
else:
    [host] = sys.argv[1:]


# get the host
try:
    name = socket.gethostbyaddr(host) 
    print(f"Host: {host} --> Name: {name}")
except (socket.gaierror):
    print("cannot resolve host name: " + host)