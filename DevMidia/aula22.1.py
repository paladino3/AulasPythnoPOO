#!C:\Users\rolim\AppData\Local\Programs\Python\Python37-32\python.exe
#Formulários insertar
#CGi

import cgi #importante pare html

def printHeader():#escopo do cabeçalho
    print("Content-type: text/html")
    print()
    print("<html>")
    print("<head><title>Forms whit CGI Python - GET -</title></head>")
    print("<body>")

def printFooter():
    print("</body></html>")

printHeader()

print("<h2>Método post em video</h2>")

print("<form method='POST' action='aula22.1.py'><p><input type='radio' name='rblSex' value='Male'>Male<br><input type='radio' name='rblSex' value='Famale'>Famale<br><input type='submit' value='Submit'/></p></form>")

pairs = cgi.parse()

if "rblSex" in pairs:
    print("<p><h2>Your sex is: %s</h2></p>" % (cgi.escape( pairs ["rblSex"][0] )))

printFooter()