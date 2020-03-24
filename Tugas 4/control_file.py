import shelve
import uuid
import socket
import os
import base64

class Control:
    def __init__(self):
        if not os.path.exists("new_folder"):
            os.makedirs("new_folder")
    def add(self,name=None,file=None):
        # file = file.encode()
        data_file = file
        f = open("new_folder/"+name,"wb")
        f.write(data_file)
        return True

    def get(self,name=None):
        temp = []
        f = open("new_folder/" +name, "rb")
        hasil = f.read()
        f.close()
        hasil = str(hasil, "utf-8")
        return hasil

    def list(self):
        list_file = os.listdir("new_folder")
        return list_file

if __name__=='__main__':
    p = control()
    print(p.list())