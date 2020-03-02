import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('192.168.1.123', 31000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(32)
        print(f"received {data}")
        hasil = open("hasil" +".jpg", 'a+b')
        if not data:
            hasil.close()
            break
        break
        hasil.write(data)
    print("File Berhasil di terima")
    # Clean up the connection
    connection.close()