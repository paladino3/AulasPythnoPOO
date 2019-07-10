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

print("<h2>Query Strings</h2>")

query = os.environ["QUERY_STRING"]

if len(query) == 0:
    print("<p>Please add some query string.</p>")
else:
    print("<p style='font-style:italic'>The query string is " +cgi.escape(query))
    pairs = cgi.parse_qs(query)

    for key, valeu in pairs.items():
        print("<p>You set query string '%s' to value %s</p>" % (key, value))

printFooter()