#!C:\Users\rolim\AppData\Local\Programs\Python\Python37-32\python.exe

import datetime
import mysql.connector
import cgi

def printHeader():
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<head><title>Insert data in MySQL Database</title></head>")
    print("<body>")

def printFooter():
    print("</body></html>")

printHeader()

print("<h2>Cadastro simples: </h2>")
print("<hr><p></p>")
print("<form method='post' action='Aula26.Projeto01.py' >")
print("<p>Nome: <input type='txt' name='txtName'/></p>")
print("<p>Email: <input type='txt' name='txtEmail'/></p>")
print("<p>Message: <input type='txt' name='txtMessage'/></p>")
print("<p><input type='submit' value='Submit'/></p>")

form = cgi.FieldStorage()

if len(form) > 0:
    cnx = mysql.connector.connect(host='localhost', database='guestbook', user='root', password='')
    cursor = cnx.cursor()
    add_guest = ("INSERT INTO guests (name,email,date,message) VALUES (%s, %s, %s, %s)")

    data_guest= (form["txtName"].value, form["txtEmail"].value, datetime.datetime.now(), form["txtMessage"].value)

    cursor.execute(add_guest, data_guest)

    cnx.commit()
    cursor.close()
    cnx.close()

    print("<h3>Sucesso, todos dados foram salvos!</h3>")
else:
    print("<h3>Algo deu errado!</h3>")
printFooter()
