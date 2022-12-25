import socket, ssl

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# require a certificate from the server
ssl_sock = ssl.wrap_socket(s)
#                           ca_certs="./CAcert.pem",
#                           cert_reqs=ssl.CERT_NONE)
#                           cert_reqs=ssl.CERT_REQUIRED)


ssl_sock.connect(('192.168.0.4', 443))

print repr(ssl_sock.getpeername())
print ssl_sock.cipher()

# Set a simple HTTP request -- use httplib in actual code.
ssl_sock.write("""GET / HTTP/1.0\r
Host: www.verisign.com\r\n\r\n""")

data = True; 
while data:
  data = ssl_sock.read()
  print data;

# note that closing the SSLSocket will also close the underlying socket
ssl_sock.close()
