#Leonardo Lusoli 8/1/2015
#Roberto Alfieri

from threading import Thread
from socket import *
import sys
import optparse


def ascolto(s,addr):
        print ("connection from the client: ", addr, file = sys.stderr)
        data = s.recv(1500).decode()
        print ('received: ',data, file = sys.stderr)
        answer = data
        s.send(answer.encode())
        print ('sent: ' , answer, file = sys.stderr)


if __name__ == "__main__":
        parser = optparse.OptionParser()
        parser.add_option('-s', '--server',  dest="server",  default="0.0.0.0", help="server name" )
        parser.add_option('-p', '--port',    dest="port",    type=int,  default=10102, help="server listening port" )
        options, remainder = parser.parse_args()
        print("OPTIONS  server:", options.server, " - port:", options.port)

        addr = (options.server,options.port)
        sock = socket(AF_INET,SOCK_STREAM)
        # Bind the socket to the port
        # server_address = (nomeserver, port)

        print('starting up on port: ',addr, file = sys.stderr)
        sock.bind(addr)
        
        # Listen for incoming connections
        sock.listen(1)
        print('waiting for a connection ', file = sys.stderr)
        sock.listen(1)
        
        # Wait for a connection
        while(1):
                s2, c_addr = sock.accept()
                #set the thread for the receive request
                ric = Thread(target = ascolto, args = (s2,c_addr))
                ric.start()
        sock.close()