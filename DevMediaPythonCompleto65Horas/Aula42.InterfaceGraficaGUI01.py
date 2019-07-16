from tkinter import *

root = Tk()

def showSelection():
    selection="Value = "+str(var.get())
    myLabel.config(text=selection)

var = DoubleVar()

myScale = Scale(root, length=300, variable=var, from_=0 , to=1000, resolution=10, tickinterval=100)
myScale.pack(anchor=CENTER)


myButton = Button(root,text="Show selected value in scale", command=showSelection)
myButton.pack(anchor=CENTER, padx=20, pady=20)

myLabel =Label(root)
myLabel.pack()

root.mainloop()