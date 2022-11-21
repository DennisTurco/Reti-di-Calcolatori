#Leonardo Lusoli 8/1/2015
#Roberto Alfieri

from threading import Thread
from socket import *
import sys
import optparse

def ascolto(s,addr):
        print ("connection from the client  ", addr, file = sys.stderr)
        # Receive the data in small chunks and retransmit it
        while True:
                data = s.recv(1500).decode()
                print ("message received ", data, file = sys.stderr)
                if data:
                      answer=data
                      s.send(answer.encode())
                      print ("message sent  ", data, file = sys.stderr)
                else:
                      print ("closed connection from ", addr , file = sys.stderr)
                      break

if __name__ == "__main__":

        parser = optparse.OptionParser()
        parser.add_option('-s', '--server',  dest="server",  default="0.0.0.0", help="server name" )
        parser.add_option('-p', '--port',    dest="port",    type=int,  default=10102, help="server listening port" )
        options, remainder = parser.parse_args()
        print ("OPTIONS  server:", options.server, " - port:", options.port)

        addr = (options.server,options.port)
        sock = socket(AF_INET,SOCK_STREAM)
        # Bind the socket to the port
        print ('server bind on port ',addr, file = sys.stderr)
        sock.bind(addr)
        print ('waiting for a connection ', file = sys.stderr)
        sock.listen(1)
        while(1):
                connection, client_address = sock.accept()
                #set the thread for the receive request
                ric = Thread(target = ascolto, args = (connection, client_address))
                ric.start()
        sock.close()