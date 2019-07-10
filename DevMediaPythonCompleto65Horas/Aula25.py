#!C:\Users\rolim\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi
import os
import sys

import cgitb; cgitb.enable()

def printHeader():
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<header><title>Upload File with CGI Python</title></head>")
    print("<body>")

def printFooter():
    print("</body></html>")


printHeader()

print("<h2>Upload File Example with CGI Python</h2>")

form = cgi.FieldStorage()

fileitem = form["filename"]

if fileitem.filename:

    fn = os.path.basename(fileitem.filename)

    open("./upload/" + fn, 'wb').write(fileitem.file.read())

    print("<p>The file " + fn + " was uploaded!</p>")

    print("<p>The file size is " + str(os.path.getsize("./upload/" + fn)) + " bytes</p>")

    print("<p>Link to file: <a href='" + "./upload/" + fn + "' target='_blank'>" + fn + "</a></p>")

else:
    print("<p>No file was uploaded!</p>")

printFooter()
