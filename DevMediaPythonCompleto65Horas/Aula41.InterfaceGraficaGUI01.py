from tkinter import *

class MyAppUI(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("My APP Com menu Bar")
        self.master.geometry("400x150")

        self.menubar = Menu(self)#para criar menu bar usamos o "menu"
        self.filemenu = Menu(self)#subitens no menu
        self.editmenu = Menu(self)
        self.colormenu = Menu(self)
        self.sizemenu = Menu(self)

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Quit", command=self.quit)

        self.menubar.add_cascade(labe="Edit", menu=self.editmenu)

        self.editmenu.add_cascade(label="Color", menu=self.colormenu)
        self.colormenu.add_command(label="Red", command=self.colorRed)
        self.colormenu.add_command(label="Green", command=self.colorGreen)
        self.colormenu.add_command(label="Blue", command=self.colorBlue)


        self.editmenu.add_cascade(label="Size", menu=self.sizemenu)
        self.sizemenu.add_command(label="10", command=self.size10)
        self.sizemenu.add_command(label="20", command=self.size20)
        self.sizemenu.add_command(label="30", command=self.size30)

        self.sizemenu.add_command()
        self.master.config(menu=self.menubar)

        self.frame1 = Frame(self)

        self.label1 = Label(self.frame1, fg="Black", text="DevMedia",font="Arial 35")
        self.label1.pack(side=LEFT, pady=20)

    def colorRed(self):
        self.label1.configure(fg="red")

    def colorGreen(self):
        self.label1.configure(fg="green")

    def colorBlue(self):
        self.label1.configure(fg="blue")


    def size10(self):
        self.label1.configure(font="Arial 10")

    def size20(self):
        self.label1.configure(font="Arial 20")

    def size30(self):
        self.label1.configure(font="Arial 30")

    def quit(self):
        self.master.destroy()

root = Tk()

app = MyAppUI()
app.pack()

root.mainloop()
