from queue import Queue
import threading
from urllib.request import urlopen

def get_url(q, url):
    q.put(urlopen(url).read())

theurls = ["http://yahoo.com", "http://google.com.br", "http://uol.com.br" ]

q = Queue()

for u in theurls:
    t=threading.Thread(target=get_url, args=(q,u))
    t.daemon=True
    t.start()
s = q.get()
print(s)