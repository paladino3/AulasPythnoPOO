#Herança


class Pessoa:#classe pai
    def __init__(self, first , last ):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname+ " " + self.lastname

class Funcionario(Pessoa):#classe filho

    def __init__(self,first, last, employeeid):
        Pessoa.__init__(self,first,last)#usamos o contrutor que já foi herdado da classe pai
        self.employeedid = employeeid

    def GetEmployee(self):
        return self.Name()+ ", " + self.employeedid

p = Pessoa("Wesley","Rolim")
f=Funcionario("Jose","Fagundes","1020")

print(p.Name())
print(f.GetEmployee())
