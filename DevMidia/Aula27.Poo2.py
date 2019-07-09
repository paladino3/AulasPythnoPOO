

class Employee:

    employeeCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employeeCount += 1


    def showEmployee(self):
        print("\nName:{}".format(self.name)+ "\nSalary: R${}".format(self.salary))


    def showCount(self):
        print("\nQunatity of Employees is: %d"% Employee.employeeCount)



func1 = Employee("Wesley rolim ",2450)
func2 = Employee("Rebeca sail",1850)
func3 = Employee("Talisson cardoso",1530)
func4 = Employee("Nayara silva",2800)

func1.showEmployee()
func2.showEmployee()
func3.showEmployee()
func4.showEmployee()

func1.showCount()

print("\n\nEmployee.__name__:",Employee.__name__)
print("\n\nEmployee.__module__:",Employee.__module__)
print("\n\nEmployee.__bases__:",Employee.__bases__)
print("\n\nEmployee.__dict__:",Employee.__dict__)
print("\n\nEmployee.__doc__:",Employee.__doc__)






