
import socket
import sys
import base64
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 8888)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    filename = "file_download.txt"
    pesan = "download " + filename
    print("Request File ke Server")
    sock.send(pesan.encode())

    data = sock.recv(4096)
    temp = open(filename, "wb")
    temp.write(data)
    temp.close()

    print("File telah diterima")
finally:
    print("Closing Connection")
    sock.close()