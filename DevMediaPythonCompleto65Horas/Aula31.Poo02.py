#polimorfismo

class Animal:

    def __init__(self,nome):
        self.nome = nome

class Gato(Animal):
    def talk(self):
        return "Miauuu"

class Cachorro(Animal):
    def talk(self):
        return "Au au Au au"

Animal = [Gato("Snow"),Cachorro("Lacraia"),Cachorro("Mell")]

for animais in Animal:
    print(animais.__class__.__name__+" "+animais.nome + ": " + animais.talk() )

