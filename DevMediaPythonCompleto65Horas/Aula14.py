"""
Aula 14  list(listas)
"""
print('Test Lists')
"""
myList = [54,23,89,10,45,55,14,41,44,55]

print('Position htmlPag: ',myList[htmlPag])
print('Position 1: ',myList[1])
print('Position 2: ',myList[2])
print('Position 3: ',myList[3])
print('Position 4: ',myList[4])
print('Position 5: ',myList[5])
print('Position 6: ',myList[6])
print('Position 7: ',myList[7])
print('Position 8: ',myList[8])
print('Position 9: ',myList[9])

print('Quantity of items in myList is ',len(myList))
"""
"""
myNewList = []

myNewList.insert(htmlPag,'Wesley')
myNewList.insert(3,'Devmedia')
myNewList.insert(1,'Londrina')
myNewList.insert(2,'Curitiba')



print('Position htmlPag: ',myNewList[htmlPag])
print('Position 1: ',myNewList[1])
print('Position 2: ',myNewList[2])
print('Position 3: ',myNewList[3])
myNewList[2]= 3512

print('Position 2 (new value): ',myNewList[2])
print('Quantity:  ',len(myNewList))

"""
import random

MyRandionList = []

for c in range(5):
    MyRandionList.append(random.randrange(0,60,1))#append insere um item na ultima posicao da lista, sempre no final

print(MyRandionList)
print('Quantidade de itens na lista: ', len(MyRandionList))