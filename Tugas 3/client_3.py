import logging
import requests
import os
import threading

def download_gambar(url=None, i=None):
    if (url is None):
        logging.warning('error')
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi} thread {i}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


if __name__=='__main__':
    thread1 = []
    file = ('https://www.ttrweekly.com/site/wp-content/uploads/2018/10/Indonesia.jpg','https://www.its.ac.id/news/wp-content/uploads/sites/2/2019/06/WhatsApp-Image-2019-06-20-at-13.44.47.jpeg','https://www.its.ac.id/news/wp-content/uploads/sites/2/2018/06/WhatsApp-Image-2018-06-22-at-15.34.59.jpeg')
    for i in range(len(file)):
        logging.warning(f"Thread{i}")
        t = threading.Thread(target=download_gambar, args=(file[i], i,))
        thread1.append(t)

    for thread2 in thread1:
        logging.warning(f"{thread2} started")
        thread2.start()