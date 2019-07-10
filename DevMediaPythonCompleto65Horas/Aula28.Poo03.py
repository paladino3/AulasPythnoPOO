#Destructor

class Point:


    def __init__(self, x=0 , y=0 ):#construtor
        self.x = x
        self.y = y


    def __del__(self):# Destrutor!!!
        class_name = self.__class__.__name__
        print(class_name + "Destruida")

p1=Point()
p2=Point()
p3=Point()#criando a classe

print(id(p1),id(p2),id(p3))#mostrando info

del p1,p2,p3

