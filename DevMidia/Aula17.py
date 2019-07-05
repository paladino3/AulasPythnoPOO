#sequencia multidimencionais 2 dimenções

print('Test Multidimensional Sequences')
"""
myTableList = [[1, 2, 3,] , [4, 5, 6,] , [7, 8, 9,]]

print('Value in table list')
for colunas in myTableList:#percorre linhas
    for item in colunas:# percorre seus itens
        print(item,end=' ')
    print()
"""
"""
myTableTuple = ((1,2,3) , (4,5, ) , (6,7,8))

for row in myTableTuple:
    for item in row:
        print(item, end=' ')
    print()"""

def printList(inputList):
    print('Value in List: ')
    for row in inputList:
        for item in row:
            print(item,end=' ')
        print()

def average(gradesOfStudant):
    total= 0.0
    for grade in gradesOfStudant:
        total += grade
    return total/len(gradesOfStudant)

listOfGrades = [ [6.4, 7.5 ,8.5 ,7.7] , [9.8 , 5.8 , 9.0 , 7.9] , [0.0 , 3.5 , 6.8 ,5.9]]

printList(listOfGrades)
for i in range(len(listOfGrades)):
    print('Avarage / Students ', i, 'is ',average(listOfGrades))