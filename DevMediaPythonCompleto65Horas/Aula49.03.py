import re


inputEmail = input(str("Digite seu email: "))

myDomain = re.search("@[\w.]+", inputEmail)

if myDomain:
    print("Seu email dominio é: ",myDomain.group())
else:
    print("Email  whitout domain")