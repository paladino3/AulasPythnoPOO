
class Length:

    __metric = {"mm": 0.001, "cm" : 0.001, "m" : 1, "km" : 1000}

    def __init__(self,value,unit="m"):
        self.value = value
        self.unit = unit


    def convertToMeters(self):
        return self.value * Length.__metric[self.unit]

    def __add__(self, other):#overload operador de adicao
        l = self.convertToMeters() + other.convertToMeters()
        return  Length(l/Length.__metric[self.unit],self.unit)


    def __repr__(self):#toString
        return "Length("+ str(self.value)+", " + self.unit + ")"


z = Length(3,"km") + Length(200)

print(repr(z))

