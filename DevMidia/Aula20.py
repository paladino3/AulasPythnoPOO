#!C:\Users\rolim\AppData\Local\Programs\Python\Python37-32\python.exe

""""
print('Content-Type:text/html')
print()
print('<html>')
print('<head><title>Hello World from Python!!!</title></head>')
print('<body>')
print('<h2>Hello World from Python!!</h2>')
print('</body></html>')
"""
from datetime import time

print('Content-Type:text/html')
print()
print('<html>')
print('<head><title>Current Date and Time</title></head>')
print('<body>')
print('<br>')
print('<h3><center>'+ time.ctime(time.time())+'</center></h3>')
print('</body></html>')