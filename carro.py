class Carro():

    def __init__(self,cor,qtd_portas,tipo_combustivel,potencia, qtd_combustivel, is_ligado, velcidade):
        self.cor = cor
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = qtd_combustivel
        self.is_ligado = is_ligado
        self.velocidade = velcidade


    def abastecer(self, qtd_combustivel):
        """explicando o metodo"""
        self.qtd_combustivel += qtd_combustivel


    def ligar(self):
        if self.is_ligado:
            print('O carro já está ligado. ')
        else:
            self.is_ligado = True
            print('Carro ligado')

    def desligar(self):
        if self.is_ligado == False:
            print('O carro está desligado.')
        else:
            self.is_ligado = False
            print('O carro foi desligado.')

    def acelerar(self,velocidade=10):
        if self.is_ligado ==  True:
            self.velocidade +=velocidade
            print('Carro acelerando em {} Km/h'.format(velocidade))
        else:
            print('O carro precisa estar ligado para ser acelerado!')