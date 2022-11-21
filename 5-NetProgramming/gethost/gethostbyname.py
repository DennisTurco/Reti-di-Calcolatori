# Author: Dennis Turco
# compile: python gethostbyname.py nost_name
# example: python gethostbyname.py www.google.com

import socket  # socket library
import sys  # sys library for get parameters from command line


# check parameters list
if len(sys.argv) < 2:
    name = "www.python.org"
else:
    [name] = sys.argv[1:]


# get the host
try:
    host = socket.gethostbyname(name) 
    print(f"Name: {name} --> Host: {host}")
except (socket.gaierror):
    print("cannot resolve host name: " + name)