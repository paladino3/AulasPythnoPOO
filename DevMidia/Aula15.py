
#Iremos ver nesta aula Lista, Ordenações e buscas IMPORTATEEEE!!!


print('Sorting and Searching Lists')
print('Ordenações e buscas em Listas')
"""
myList = [34, 5,44 ,25, 47 ,86, 0, 5,447 ,77 ,78 ,55 ,61 ,78 ,58 ,55 ,44 ,66 ]

print('\nItems in original order: ')

for item in myList:
    print('',item)

myList.sort()
print('\nItems after sorting:')

for item in myList:
    print('',item)

myList.reverse()
print('\nItems after reverse sorting: ')

for item in myList:
    print('',item)

print('\nSize of list: ',len(myList))# len(tamanho da minha lista)
print('\nCount items in list: ',myList.count(5))#.count(quantas vezes aparece o numero 5)
"""

myListOfStrings = ['Wesley','Devmedia', 'Python','List','Search','Hello','Word','Progamming','Londrina']

searchString = input('Type search string: ').title()


if searchString in myListOfStrings:
    print('Found at index: ',myListOfStrings.index(searchString))#metodo index retorna a posição
else:
    print('Not found!')