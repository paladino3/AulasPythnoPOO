from tkinter import *
from tkinter.scrolledtext import *
from tkinter.filedialog import *

class App:
    def __init__(self, master):

        master.geometry("300x300")
        master.title("Meu Leitura e Escrita de Arquivos exemplos")
        frame = Frame(master)
        frame.pack()

        bottomframe = Frame(root)
        bottomframe.pack(side=BOTTOM, expand=YES, fill=BOTH)

        self.btRead = Button(frame, text="Read File", command=self.readFile)
        self.btRead.pack(side=LEFT)

        self.btSave = Button(frame, text="Save File", command=self.saveFile)
        self.btSave.pack(side=LEFT)

        self.showText= ScrolledText(bottomframe)
        self.showText.pack(side=LEFT, padx=5, expand=YES, fill=BOTH)


    def readFile(self):
        myFile = askopenfile(parent=root, mode="rb", title="Select file")
        if myFile != None:
            data = myFile.read()
            self.showText.insert("1.0", data)
            myFile.close()

        """with open("myFile.txt","r") as myFile:
            for line in myFile:
                self.showText.insert(END, line)
"""
    def saveFile(self):
        myfile = asksaveasfile(mode="w")
        if myfile != None:
            data = self.showText.get("1.0", END+"-1c")
            myfile.write(data)
            myfile.close()
"""        
        myfile = open("myFile.txt", "w")
        data = self.showText.get("1.0", END+"-1c")
        myfile.write(data)
        myfile.close()
"""
root =  Tk()
app = App(root)
root.mainloop()