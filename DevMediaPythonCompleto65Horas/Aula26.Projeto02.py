#!C:\Users\rolim\AppData\Local\Programs\Python\Python37-32\python.exe

import datetime
import mysql.connector
import cgi

def printHeader():
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<head><title>Read Data From MySQL Database</title></head>")
    print("<body>")

def printFooter():
    print("</body></html>")

printHeader()

print("<h2>Nomes inseridos no Banco de Dados: </h2>")
print("<hr><p></p>")#linha horizontal
cnx = mysql.connector.connect(host='localhost', database='guestsbook', user='root', password='')
cursor = cnx.cursor()

cursor.execute('SELECT * FROM guests')

row = cursor.fetchone()#pega as informações em uma unica linha
print("<table>")

while row is not None:
    print("<tr>")#linha
    print("<td>" + str(row[0]) + "</td>")#coluna
    print("<td>" + str(row[1]) + "</td>")
    print("<td>" + str(row[2]) + "</td>")
    print("<td>" + str(row[3]) + "</td>")
    print("<td>" + str(row[4]) + "</td>")

    row = cursor.fetchone()

    print("</tr>")#fecha linha

print("</table>")

cursor.close()
cnx.close()

printFooter()
