from tkinter import *
root = Tk()

myListbox = Listbox(root)
myListbox.insert(1, "Red")
myListbox.insert(2, "Green")
myListbox.insert(3, "Blue")
myListbox.insert(4, "Yellow")
myListbox.insert(5, "White")
myListbox.insert(6, "Black")

myListbox.insert(1, "Purple")#oque vale e o incede para derterminar a posicoa na lista

myListbox.pack()

root.mainloop()