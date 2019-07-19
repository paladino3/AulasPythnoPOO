"""
Tratamentos e execeções
"""

number1= input("Entre com um número: ")
number2= input("Entre com um denominador: ")

try:
    number1=int(number1)
    number2=int(number2)
    result=int(number1/number2)
except ValueError:
    print("Erro, Apenas números são aceitos")
except ZeroDivisionError:
    print("Erro, Não existe divisão por Zero")
else:
    print("O resultado de {} / {} é: {}".format(number1,number2,result))
    print("Nehum erro ;)")
finally:
    print("GoodBye")
