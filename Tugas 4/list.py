import socket
import sys
from time import sleep
import base64

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 8888)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

pesan = (b"list")
sock.send(pesan)
print("\nRequest dikirim\n")
data = sock.recv(2048)
print("List file : \n"+data.decode())

sock.close()