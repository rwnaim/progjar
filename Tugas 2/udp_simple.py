import socket

TARGET_IP = "192.168.1.130"
TARGET_PORT = 5006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes('INFORMATIKA'.encode()),(TARGET_IP,TARGET_PORT))