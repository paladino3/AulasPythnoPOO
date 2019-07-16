from tkinter import *

root = Tk()

topframe = Frame(root)
topframe.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM, expand=YES, fill=BOTH)

button1 = Button(topframe, text="Button 1")
button1.pack(side=LEFT)

button2 = Button(topframe, text="Button 2")
button2.pack(side=LEFT)

button3 = Button(topframe, text="Button 3")
button3.pack(side=LEFT)

button4 = Button(bottomframe, text="Button 4")
button4.pack(side=BOTTOM, expand=YES, fill=X)

root.mainloop()