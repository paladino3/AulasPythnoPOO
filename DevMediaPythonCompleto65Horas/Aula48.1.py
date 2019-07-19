"""
split e join

"""
myString1 = "A, C, E, F, E, D, S, T"

print("String is: ",myString1.strip())
print("String with split: ",myString1.split())
print("Split string by commas: ",myString1.split(","))
print("Split string by commas, max 2: ",myString1.split(",",2))
print()


myList1=["A", "B", "C", "D", "E", "F", "G", "H"]
myString2= "-"
print("Lista é: ",myList1)
print('Joining with %s: %s' % (myString2,myString2.join(myList1)))
print('Joining with ".-.": ', "*-*".join(myList1))