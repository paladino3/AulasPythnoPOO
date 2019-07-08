# Aula de tuplas ou Tuples

#As tuplas sao imutaves, ou seja nao permite ser alteradas!

print('Test tuples')
"""
myTuple = ('wesley',2019,'devmedia',3.14,'A','X',2.83)#parenteses ou sem nada

print('\nItems in myTuple: ',myTuple)
print('\nQuantity of items in myTuple is ',len(myTuple))
print('\nElement in position 3 ',myTuple[3])

#myTuple[3] = 1.5 Error o Tuple nao suporta modicar os itens: são elementos fixos


myTuple2 = 1, 'Fiat', 'Uno',1.htmlPag, '2019'

print('\nItems in myTuple: ',myTuple2)
print('\nQuantity of items in myTuple is ',len(myTuple2))
print('\nElement in position 3 ',myTuple2[3])

myTuple3 = 'XYZ',
print('\nItems in myTuple: ',myTuple3)
print('\nQuantity of items in myTuple is ',len(myTuple3))
"""
"""
myNewTuple = tuple('Devmedia')
print('The items in myNewTuple is ',myNewTuple)
print('Quatity of items in myNewTuple is ',len(myNewTuple))
print('Item in position 2: ',myNewTuple[2])
"""
myCarTuple = ('Ford', 'Focus', 2018, 2.0 ,'Blue')

(automaker, model, year, cc, color) = myCarTuple #util pois ele desempacota com as posições certas!!!!

print('Automaker: ',automaker)
print('Model: ',model)
print('Year: ',year)
print('CC: ',cc)
print('Color: ',color)

