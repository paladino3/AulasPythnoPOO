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
        return "%s is a %s" % (self.name, self.specie)

