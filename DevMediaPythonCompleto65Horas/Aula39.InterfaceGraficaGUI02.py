from tkinter import *

root = Tk()

button1=Button(root, text="Button 1")
button1.grid(row=1, column=1, padx=5, pady=5)

button2=Button(root, text="Button 2")
button2.grid(row=1, column=2, padx=5, pady=5)

button3=Button(root, text="Button 3")
button3.grid(row=2, column=1, padx=5, pady=5)

button4=Button(root, text="Button 4")
button4.grid(row=2, column=2, padx=5, pady=5)

button5=Button(root, text="Button 5")
button5.grid(row=3, column=1, padx=5, pady=5)

button6=Button(root, text="Button 6")
button6.grid(row=3, column=2, padx=5, pady=5)

button7=Button(root, text="Button 7")
button7.grid(row=4, column=1,columnspan=2, padx=5, pady=5)


root.mainloop()