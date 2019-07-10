"""
Nesta aula iremos ver os atributos especiais:
getter, setter e dell, que são os métodos que acessam os atributos, e ver os overload de operadores
"""

class Car:

    #construtor
    def __init__(self,automaker,model ):
        self.automaker = automaker
        self.model = model


    #Atributo especial getter
    def __getattr__(self, item):
        return "Not exist"

    #Atributo especial setter
    def __setattr__(self, name, value):
        if name == "automaker":
            if value == "GM":
                self.__dict__["automaker"] ="Chevrolet" #dicionary
            else:
                self.__dict__["automaker"] = value
        else:
             self.__dict__[name] = value


    def __delattr__(self, name):
        print("Attribute was deleted")

myCar = Car("Ford","Focus")

print(myCar.automaker)
print(myCar.model)
print(myCar.year)

meuCarro = Car("GM", "Camaro")
print(meuCarro)#objeto carro na memoria
print(meuCarro.model)
print(meuCarro.automaker)
