# classe privada
class PrivateClassTest:


    def __init__(self):

        self.publicData = "plubic"

        self.__privateData = "private" #no python nao exite atributo privado, porem temos (__mengle) emula um atributo privado.

#ele muda o nome do atributo para: _PrivateClassTest__privateData, desta forma ele simula um private.

myclass = PrivateClassTest()

print(myclass.publicData)
#print(myclass.__privateData) erro pois o atributo teoricamente esta privato..
print(myclass._PrivateClassTest__privateData)


myclass._PrivateClassTest__privateData = "Changed"#acessando este método da forma correta, já que o python nao possui atributo privato
print(myclass._PrivateClassTest__privateData)



