#aulas de programação orientada a objetos

class Pet:

    def __init__(self,name,specie):#construtor
        self.name = name
        self.specie = specie

    def getName(self):
        return self.name

    def getSpecie(self):
        return self.specie

    def __str__(self):#atributo especial de exibicao padrao da classe
        return "{} is a {}".format(self.name, self.specie)


myPet1 = Pet("lacraia","dog")
myPet2 = Pet("snow","cat")
myPet3 = Pet("rex","fish")


print(myPet1)
print(myPet2)
print(myPet3)

print("myPet1 name attribute: "+str(myPet1.getName()))
print("myPet3 specie attribute: "+str(myPet3.getSpecie()))
print("myPet2 name attribute: "+str(myPet2.getName()))
print("myPet2 specie attribute: "+str(myPet2.getSpecie()))