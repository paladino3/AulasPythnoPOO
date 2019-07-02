import carro, moto

uno_vermelho = carro.Carro('Vermelho',4,'flex',1.0)
uno_preto=carro.Carro('Preto',2,'Gás',1.4)


print(uno_preto.is_ligado)

uno_vermelho.ligar()

moto1= moto.Moto('Azul','flex',600,2)

print('{} Cilindradas'.format(moto1.potencia))
print(moto1.is_ligado)
print(moto1.qtd_passageiros)
