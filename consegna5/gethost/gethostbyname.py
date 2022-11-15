# Author: Dennis Turco
# compile: nano python gethostbyname.py nost_name
# example: nano python gethostbyname.py www.google.com

# Note: nano command is nedded for read/write into file "/etc/hosts"

import socket  # socket library
import sys  # sys library for get parameters from command line

# -------------------------------------------- functions --------------------------------------------

def add_host_by_name(name, data, counter):
    # get the host
    try:
        host = socket.gethostbyname(name) 
    except (socket.gaierror):
        print("cannot resolve host name: " + name)
        return

    # add string in "counter" line
    with open(filename, "w") as file:
        data[counter] = host + "    " + name + "\n\n"
        file.writelines(data)
    
    print(f"host address: {host} added in file {filename}")

    return host

def find_host_by_name(host):
    # get file lines
    with open(filename, "r+") as file:
        data = file.readlines()
    
    counter = 0
    for line in data:
        if len(line.split()) > 0: # this if is required for avoid error "index out of range" on "line.split()[0]"
            if name == line.split()[1]: # host founded
                print(f"name address: {name} founded in file {filename}")
                return line.split()[1]  

        if len(line) == 1: # read of ipv4 host terminated
            host = add_host_by_name(name, data, counter) # host doesn't found, i have to add it
            return host

        counter = counter + 1


# -------------------------------------------- "global" --------------------------------------------

filename = "/etc/hosts"

# check parameters list
if len(sys.argv) < 2:
    name = "www.python.org"
else:
    [name] = sys.argv[1:]


# find the host address
host = find_host_by_name(name)


# print
print(f"Name: {name} --> Host: {host}")