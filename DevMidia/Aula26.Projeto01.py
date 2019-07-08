#!C:\Users\rolim\AppData\Local\Programs\Python\Python37-32\python.exe

import datetime
import mysql.connector
import cgi

def printHeader():
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<header><title>Insert data in MySQL Database</title></header>")
    print("<body>")

def printFooter():
    print("</body></html>")

printHeader()

print("<h2>Insert in guestbook(Livro)</h2>")
print("<form method='post' action='Aula26.Projeto01.py' >")
