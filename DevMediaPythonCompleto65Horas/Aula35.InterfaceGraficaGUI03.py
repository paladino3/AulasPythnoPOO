from distutils import command
from tkinter import *
from tkinter import messagebox


class EntryDemo(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.pack(expand=YES,fill=BOTH)
        self.master.title("Calcular area de um retangulo")
        self.master.geometry("500x300")
        self.configure(background="#ff0000")

        self.frame1=Frame(self)
        self.frame1.pack(pady=5)

        self.label1 =Label(self.frame1, fb="blue", bg ="yellow", text="Size 1:")
        self.label1.pack(side=LEFT, padx=5)


        self.text1 = Entry (self.frame1, width=17 , name="number1")
        self.text1.insert(INSERT, "Entre com um valor do lado 1")
        self.text1.pack(side=LEFT,pack=5)

        self.frame2 = Frame(self)
        self.frame2.pack(pady=5)

        self.label2 = Label(self.frame2, fb="blue", bg="yellow", text="Size 2:")
        self.label2.pack(side=LEFT, padx=5)

        self.text2 = Entry(self.frame2, width=17, name="number2")
        self.text2.insert(INSERT, "Entre com um valor do lado 2")
        self.text2.pack(side=LEFT, pack=5)

        self.frame3 = Frame(self)
        self.frame3.pack(pady=5)

        self.button1 = Button(self.frame3, text="Quit", command=self.quit, fb="yellow")
        self.button1.pack(side=LEFT,padx=5)


    def quit(self):
        self.master.destroy()

    def calcularArea(self):
        area = int(self.text1.get())*int(self.text2.get())
        messagebox.showinfo("Resultado","A area do retangulo é: "+str(area))

def main():
    EntryDemo().mainloop()
if __name__ == "__main__":
    main()