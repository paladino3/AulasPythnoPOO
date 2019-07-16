from tkinter import *

master = Tk()

myCanvas = Canvas(master, width=400, height=400)
myCanvas.pack()

myCanvas.create_line(0,0,400,400)
myCanvas.create_line(0,400,400,0, fill="Red", dash=(4,4))

myCanvas.create_rectangle(100,100,300,300,fill="Blue")
myCanvas.create_oval(100,100,300,300, fill="Green")

mainloop()