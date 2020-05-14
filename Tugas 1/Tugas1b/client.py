import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.130', 31003)
print(f"connecting to {server_address}")
sock.connect(server_address)
try:
    # Send data
    file_name = "untitled.png"
    content = file_name
    print ('sending data...')
    sock.sendall(content.encode())
    while 1:
        data = sock.recv(1024)
        print(f"recieved{data}")
        hasil = open("hasil " + file_name, 'a+b')
        if not data:
            hasil.close()
            break
        hasil.write(data)
    print(f"received{file_name}")
    # print ("done!")
finally:
    print("File telah diterima")
    sock.close()