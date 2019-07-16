from tkinter import *

root=Tk()

def showValue():
    selection = "Value in spinbox is " +str(mySpinbox.get())
    myLabel.config(text=selection, font="Arial 30", fg="Black")

mySpinbox = Spinbox(root,values=('Green','Red','Black','Blue','White','Yellow','Purple'), command=showValue)
mySpinbox.pack()


myLabel = Label(root)
myLabel.pack(padx=50, pady=20)


root.mainloop()
