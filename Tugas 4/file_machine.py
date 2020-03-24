
from control_file import Control
import json
import logging

'''
------ PROTOCOL FORMAT ------
string terbagi menjadi 2 bagian yang dipisahkan oleh spasi
Format : command *spasi* parameter *spasi* parameter

------ FITUR ------
a. Upload File
   Untuk upload file ke dalam folder "new_folder"
   Request : add_file
   Parameter : namafile *spasi* isi dari file
   Response : berhasil -> "File Added"
              gagal -> "ERROR"
b. List File
   Untuk melihat list file di dalam folder 'new_folder'
   Request : list
   Parameter: -
   Response: list file yang ada dalam folder 'new_folder'
c. Download File
   Untuk download file berdasarkan nama file dari folder 'new_folder'
   Request : download
   Parameter : namafile yang ingin diambil
   Response: file ter download pada folder tempat script berada
d. Jika command tidak dikenali akan merespon dengan ERRCMD
'''
p = Control()

class Machine:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='add_file'):
                print("add_file")
                filename = cstring[1].strip()
                file = cstring[2].strip()
                # print(file)
                print("Menambahkan",filename)
                # print()
                p.add(filename,file.encode())
                return "File telah ditambahkan"

            elif (command=='list'):
                logging.info("list")
                data = {}
                data['files'] = []
                hasil = p.list()
                for filename in hasil:
                    data['files'].append({"filename":filename})
                return json.dumps(data, indent=4)

            elif (command=='download'):
                print("download")
                filename = cstring[1].strip()
                print("Retrieving", filename)
                hasil = p.get(filename)
                return hasil


            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    machine = Machine()