#!C:\Users\rolim\AppData\Local\Programs\Python\Python37-32\python.exe
#Arquivos CGI

import cgi

def printHeader():
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<head><title>Arquivos em CGI</title></head>")
    print("body")

def printFooter():
    print("</body></html>")

printHeader()

print("<h2>White file example with CGI, Escrevendo exemplos de arquivos!</h2>")

print("<form method='post' action='aula24.py' >")
print("<p>Name: <input type='text' name='txtName' /></p>")
print("<p>Company: <input type='text' name='txtCompany'/></p>")
print("<p>Favorite Color: <select name='selColor'><option value='Select'>Select</option><option value='Blue'>Blue</option><option value='Red'>Red</option><option value='Green'>Green</option><option value='Yellow'>Yellow</option></select></p>")
print("<p><input type='submit' value='Submit'/></p>")
print("</form>")

form = cgi.FieldStorage()#ele recupera as informacoes que foram passadas atrasves do metodo post

if len(form)>0 and form["selColor"].value != "Select":
    with open('dataSaved.txt','w') as fileOutput:
        fileOutput.write()

