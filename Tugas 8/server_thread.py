from socket import *
import socket
import threading
import time
import sys
import logging

from http import HttpServer

httpserver = HttpServer()


class ProcessTheClient(threading.Thread):
	def __init__(self, connection, address):
		self.connection = connection
		self.address = address
		threading.Thread.__init__(self)

	def run(self):
		rcv=""
		while True:
			try:
				data = self.connection.recv(1024)
				if data:
					d = data.decode()
					rcv=rcv+d
					# print(rcv)
					# if rcv[-2:]=='\r\n':
					#end of command, proses string
					logging.warning("data dari client: {}" . format(rcv))
					result = httpserver.proses(rcv)
					result = result + "\r\n\r\n"
					logging.warning("balas ke  client: {}" . format(result))
					self.connection.sendall(result.encode())
					rcv=""
					self.connection.close()
				else:
					break
			except OSError as e:
				pass
		self.connection.close()



class Server(threading.Thread):
	def __init__(self):
		self.the_clients = []
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		threading.Thread.__init__(self)

	def run(self):
		self.my_socket.bind(('0.0.0.0', 10002))
		self.my_socket.listen(1)
		while True:
			self.connection, self.client_address = self.my_socket.accept()
			logging.warning("connection from {}".format(self.client_address))
			clt = ProcessTheClient(self.connection, self.client_address)
			clt.start()
			self.the_clients.append(clt)

def main():
	svr = Server()
	svr.start()

if __name__=="__main__":
	main()