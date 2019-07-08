#!C:\Users\rolim\AppData\Local\Programs\Python\Python37-32\python.exe

import os
import cgi

def printHeader():
    print ("Content-Type:text/html")
    print ()
    print ("<html>")
    print ("<head><title>Information about system</title></head>")
    print ("<body>")


def printFooter():
    print("</body></html>")

printHeader()

rowNumber = 0
backgroundColor = "white"

print("<table style='border:0'>")

for item in os.environ.keys():

    rowNumber += 1

    if rowNumber % 2 == 0:
        backgroundColor = "white"
    else:
        backgroundColor = "lightblue"

    print("<tr style='background-color:%s'><td>%s</td>s%</td></tr>" % (backgroundColor, cgi.escape(item), cgi.escape(os.environ[item])))

print("</table>")

printFooter()
