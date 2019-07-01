import carro

uno_vermelho = carro.Carro('vermelho',4,'Flex',1.0,0,False,0)
uno_vermelho.ligar()
help(uno_vermelho.abastecer(1))

print('A quantidade de combustivel do carro é: {}'.format(uno_vermelho.qtd_combustivel))


uno_preto =carro.Carro('preto',2,'Flex',1.0,0,False,0)
uno_preto.desligar()
print('A quantidade de combustivel do carro é: {}'.format(uno_preto.qtd_combustivel))
uno_preto.acelerar(20)
uno_preto.ligar()
uno_preto.acelerar()