import socket
import sys
import base64

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 8888)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    filename="uploadfile.txt"
    temp = open(filename,"rb")
    file = temp.read()
    temp.close()
    file = file.decode()
    pesan = "add_file "+filename+" "+file
    # print(file)
    print ("Menambahkan File")
    sock.send(pesan.encode())

    data = sock.recv(2048).decode()
    print(data)
finally:
    print("Closing Connection")
    sock.close()