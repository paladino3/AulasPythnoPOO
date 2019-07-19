"""
Aula de Expressoes Relugares
Assunto amplo, um curso inteiro para dominar expressoes regulares, vendo o básico
"""
import re
#importar re regular expression

myText = "Bats are rats with wings"

searchObj = re.findall(r'[b|r]ats', myText, re.M|re.I)


if searchObj:
    print("Found: ",searchObj)
else:
    print("Not found")