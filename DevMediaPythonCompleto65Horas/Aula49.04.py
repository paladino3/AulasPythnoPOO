import re

def validateEmail(email):

    if len(email)>7:
        if re.match("/^[a-z0-9.]+@[a-z0-9]+\.[a-z]+\.([a-z]+)?$/i;",email):
            return 1
        return 0

inputEmail= input("Entre com seu email: ")

if validateEmail(inputEmail):
    print("Validate")
else:
    print("Not validate")
