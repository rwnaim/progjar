import socket
import time
import sys
import asyncore
import logging

jml_req = 0
port = 8000

class BackendList:
	def __init__(self):
		self.servers=[]
		self.servers.append(('127.0.0.1',9000))
		self.current=0
	def getserver(self):
		s = self.servers[self.current]
		self.current=self.current+1
		if (self.current>=len(self.servers)):
			self.current=0
		return s

	def addserver(self):
		global port
		port += 1
		self.servers.append(('127.0.0.1', port))

class Backend(asyncore.dispatcher_with_send):
	def __init__(self,targetaddress):
		asyncore.dispatcher_with_send.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connect(targetaddress)
		self.connection = self

	def handle_read(self):
		try:
			self.client_socket.send(self.recv(8192))
		except:
			pass
	def handle_close(self):
		try:
			self.close()
			self.client_socket.close()
		except:
			pass


class ProcessTheClient(asyncore.dispatcher):
	def handle_read(self):
		data = self.recv(8192)
		if data:
			self.backend.client_socket = self
			self.backend.send(data)
	def handle_close(self):
		self.close()

class Server(asyncore.dispatcher):
	def __init__(self,port_num):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.bind(('',port_num))
		self.listen(5)
		self.bservers = BackendList()
		logging.warning("load balancer berjalan di port {}" . format(port_num))

	def handle_accept(self):
		pair = self.accept()
		global jml_req
		if pair is not None:
			sock, addr = pair
			logging.warning("Terkoneksi dari {}" . format(repr(addr)))
			jml_req+=1
			if (len(self.bservers.servers) < 5):
				if (jml_req > 300):
					jml_req = 0
					self.bservers.addserver()
			#menentukan ke server mana request akan diteruskan
			bs = self.bservers.getserver()
			logging.warning("Koneksi dari {} diteruskan ke {}" . format(addr, bs))
			backend = Backend(bs)

			#mendapatkan handler dan socket dari client
			handler = ProcessTheClient(sock)
			handler.backend = backend


def main():
	port_num=44444
	try:
		port_num=int(sys.argv[1])
	except:
		pass
	svr = Server(port_num)
	asyncore.loop()

if __name__=="__main__":
	main()
