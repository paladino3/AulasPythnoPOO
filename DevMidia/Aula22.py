#!C:\Users\rolim\AppData\Local\Programs\Python\Python37-32\python.exe
#Formulários insertar
#CGi

import cgi #importante pare html

def printHeader():
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<head><title>Forms with CGI Python - GET</title></head>")
    print("<body>")

def printFooter():
    print("</body></html>")

printHeader()

print("<h2>Form with GET Method</h2>")

print("<form method='GET' action'aula22.py'><p>Company:<input type='text' name='txtCompany'/><br><input type='submit' value='Submit'/></p></form>")

pairs = cgi.parse()

if "txtCompany" in pairs:
    print("<p>Your company is: %s</p>" % (cgi.escape( pairs ["txtCompany"][0] )))

printFooter()
