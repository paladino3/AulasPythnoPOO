class Veiculo():

    def __init__(self,cor,tipo_combustivel,potencia, qtd_combustivel=0, is_ligado=False, velcidade=0):
        self.cor = cor
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
            print('O veiculo já está ligado. ')
        else:
            self.is_ligado = True
            print('veiculo ligado')

    def desligar(self):
        if self.is_ligado == False:
            print('O veiculo está desligado.')
        else:
            self.is_ligado = False
            print('O veiculo foi desligado.')

    def acelerar(self,velocidade=10):
        if self.is_ligado ==  True:
            self.velocidade +=velocidade
            print('Veiculo acelerando em {} Km/h'.format(velocidade))
        else:
            print('O veiculo precisa estar ligado para ser acelerado!')