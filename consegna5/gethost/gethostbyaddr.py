# Author: Dennis Turco
# compile: sudo python gethostbyaddr.py ip_address
# example: sudo python gethostbyaddr.py 142.250.184.36

# Note: sudo command is nedded for read/write into file "/etc/hosts"

import socket  # socket library
import sys  # sys library for get parameters from command line

# -------------------------------------------- functions --------------------------------------------

def add_host_by_addr (host, data, counter):
    # get the host
    try:
        name = socket.gethostbyaddr(host) 
    except (socket.gaierror):
        print("cannot resolve host address: " + host)
        return

    # add string in "counter" line
    with open(filename, "w") as file:
        data[counter] = host + "    " + name[0] + "\n\n"
        file.writelines(data)
    
    print(f"host name: {name} added in file {filename}")

    return name

def find_host_by_addr(host):
    # get file lines
    with open(filename, "r+") as file:
        data = file.readlines()
    
    counter = 0
    for line in data:
        if len(line.split()) > 0: # this if is required for avoid error "index out of range" on "line.split()[0]"
            if host == line.split()[0]: # host founded
                print(f"host name: {line.split()[1]} founded in file {filename}")
                return line.split()[1]  

        if len(line) == 1: # read of ipv4 host terminated
            name = add_host_by_addr(host, data, counter) # host doesn't found, i have to add it
            return name

        counter = counter + 1

# -------------------------------------------- "global" --------------------------------------------
filename = "/etc/hosts"

# check parameters list
if len(sys.argv) < 2:
    host = "142.250.184.36"
else:
    [host] = sys.argv[1:]

# find the host
name = find_host_by_addr(host)

# print
print(f"Host: {host} --> Name: {name}")
