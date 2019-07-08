#!C:\Users\rolim\AppData\Local\Programs\Python\Python37-32\python.exe
#Arquivos CGI

import cgi

def printHeader():
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<head><title>Arquivos em CGI</title></head>")
    print("<body>")

def printFooter():
    print("</body></html>")

printHeader()

print("<h2>Read file example with CGI, Lendo exemplos de arquivos!</h2>")

print("<form method='post' action='Aula24.Ex2.py' enctype='multipart/form-data' >")
print("<p>Arquivo: <input type='file' name='file'/></p>")
print("<p><input type='submit' value='Submit'/></p>")
print("</form>")

form = cgi.FieldStorage()#ele recupera as informacoes que foram passadas atrasves do metodo post

if "file" in form:

    fileitem = form["file"]

    if not fileitem.file:
        print("<h3>No file found!</h3>")
    else:
        text_file = open(fileitem.filename, "r")

        print("<hr><h3>Result:</h3>")

        for line in text_file:
            datas = line.split(';')
            print("<p>Name: " + datas[0] + "<br>")
            print("<p>Company: " + datas[1] + "<br>")
            print("<p>Color: " + datas[2] + "<br>")
else:

    print("<h3>No file selected</h3>")

printFooter()
