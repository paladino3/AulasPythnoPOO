#!C:\Users\rolim\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi

def printHeader():
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<head><title>Form with CGI Python - GET</title></head>")
    print("<body>")

def printFooter():
    print("</body></html>")

printHeader()
print("<p><h2>Formulário Basico!</h2></p>")

print("<form method='post' action='aula23.py'>")
print("<p>First Name: <input type='text' name='txtName' /></p>")
print("<p>Last Name: <input type='text' name='txtLastName' /></p>")
print("<p><input type='radio' name='rblSex' value='Male'>Male<br><input type='radio' name='rblSex' value='Female'>Female</p>")
print("<p>Company: <input type='text' name='txtCompany' /></p>")
print("<p>Favorite Color: <select name='selColor'><option value='Select'>Select</option><option value='Blue'>Blue</option><option value='Red'>Red</option><option value='Green'>Green</option><option value='Yellow'>Yellow</option></select></p>")
print("<p><input type='submit' value='Submit' /></p>")
print("</form>")

form = cgi.FieldStorage()

if len(form) > 0 and form["selColor"].value != "Select" :

    print("<hr><h3>Result:</h3>")

    if "txtName" in form:
        print("<p>Name: %s</p>" % cgi.escape(form["txtName"].value))

    if "txtLastName" in form:
        print("<p>Last Name: %s</p>" % cgi.escape(form["txtLastName"].value))

    if "rblSex" in form:
        print("<p>Sex: %s</p>" % cgi.escape(form["rblSex"].value))

    if "txtCompany" in form:
        print("<p>Company: %s</p>" % cgi.escape(form["txtCompany"].value))

    if "selColor" in form:
        print("<p>Favorite Color: %s</p>" % cgi.escape(form["selColor"].value))


printFooter()



