print('Test Dictionararies Methods')

myMonthsDictionary = {1:'Janeiro',2:'Fevereiro',3:'Março',4:'Abril',
                      5:'Maio',6:'Junho',7:'Julho',8:'Agosto',9:'Setembro',10:'Outubro',11:'Novembro',12:'Dezembro'}

print('Os itens do meus meses são: ',myMonthsDictionary.items())
print('As chaves do meus metodos dict_keys: ',myMonthsDictionary.keys())
print('\nThe myMonthsDictionary values are: ',myMonthsDictionary.values())
print('\nThe quantity of items are: ',len(myMonthsDictionary))

myIpunt = int(input('Type birthday month'))

if (myIpunt in myMonthsDictionary):
    print('Your birthday is ',myMonthsDictionary[myIpunt])
else:
    print('Month not exists')

newCopiedDictionary = myMonthsDictionary.copy()
newCopiedDictionary[3]='nothing'
print('Copied dictionary: \n',newCopiedDictionary)
print('Source dictionary: \n',myMonthsDictionary)

