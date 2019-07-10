
class Retanglo:

    resultadoArea = 0

    def __init__(self, ladoA = 1, ladoB = 1):#construtor e valor default
        self.calcArea(ladoA,ladoB)


    def calcArea(self, ladoA, ladoB):   #metodo calcula area
        self.resultadoArea = ladoB * ladoB



rt1 = Retanglo()#valor padrao = 1*1 =1

print("\nThe result area is "+str(rt1.resultadoArea))

rt2 = Retanglo(5,5) #5*5 =25
print("\nThe result area is "+str(rt2.resultadoArea))
