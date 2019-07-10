class Veiculo:


    def __init__(self,tipo):
        self.veiculoTipo = tipo

    def __str__(self):
        return  self.veiculoTipo


class Carro(Veiculo):# carro herdando a classe veiculo


    def __init__(self, montadora, modelo, combustivel):
        super(Carro, self).__init__("Carro")
        self.montadora = montadora
        self.modelo = modelo
        self.combustivel = combustivel

    def __str__(self):
        return super(Carro, self).__str__() + ", "+ self.montadora + ", "+ self.modelo + ", "+ self.combustivel

class Caminhao(Veiculo):#classe caminhao herdando de veiculo

    def __init__(self,montadora,modelo):
        super(Caminhao, self).__init__("Caminhão")
        self.montadora = montadora
        self.modelo = modelo
        self.combustivel = "Diesel"

    def __str__(self):
         return super(Caminhao, self).__str__() + ", "+ self.montadora + ", "+ self.modelo + ", "+ self.combustivel


meuCarro = Carro("Fiat","uno","Flex")
meuCaminhao = Caminhao("Volvo","d1002")


print(meuCarro)
print(meuCaminhao)
