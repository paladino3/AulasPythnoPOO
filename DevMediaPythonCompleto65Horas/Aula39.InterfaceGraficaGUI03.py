from tkinter import *


root = Tk()

myButton = Button(root, text="My Button")
myButton.pack()

myButton.place(bordermode=OUTSIDE, height=30, width=100, x=30, y=40)

root.mainloop()