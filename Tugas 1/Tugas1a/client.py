import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.130', 31000)
print(f"connecting to {server_address}")
sock.connect(server_address)


try:
    # Send data
    file_name = "city2.jpg"
    file = open(file_name, 'rb')
    content = file.read()
    print ('sending data...')
    sock.sendall(content)
    # print ("done!")
finally:
    print("closing")
    sock.close()