import json
from tkinter import *


class App:
    def __init__(self, master):
        master.geometry("250x150")
        master.title("Meu JSON Exemplo")
        frame = Frame(master)
        frame.pack()

        self.btSave = Button(frame, text="Save JSON File",command=self.saveFile)
        self.btSave.pack(side=LEFT)

        self.btRead = Button(frame, text="Read JSON File",command=self.readFile)
        self.btRead.pack(side=LEFT)

        #ID
        frameID = Frame(root)
        frameID.pack(side=BOTTOM, pady=10)
        self.labelID = Label(frameID, text="ID:")
        self.labelID.pack(side=LEFT, padx=5)
        self.inputID = Entry(frameID)
        self.inputID.pack(side=LEFT, padx=5)

        #NAME
        frameName = Frame(root)
        frameName.pack(side=BOTTOM, pady=10)
        self.labelName = Label(frameName, text="Name:")
        self.labelName.pack(side=LEFT, padx=5)
        self.inputName = Entry(frameName)
        self.inputName.pack(side=LEFT, padx=5)

        #City
        frameCity = Frame(root)
        frameCity.pack(side=BOTTOM, pady=10)
        self.labelCity = Label(frameCity, text="City:")
        self.labelCity.pack(side=LEFT, padx=5)
        self.inputCity = Entry(frameCity)
        self.inputCity.pack(side=LEFT, padx=5)

    def readFile(self):
        with open("data.json", "r") as file:
            data = json.load(file)
            self.inputID.insert(INSERT, str(data["id"]))
            self.inputName.insert(INSERT, str(data["name"]))
            self.inputCity.insert(INSERT, str(data["city"]))

    def saveFile(self):
        data = {'id' : self.inputID.get(), 'name' : self.inputName.get(), 'city' : self.inputCity.get()}

        with open("data.json", "w") as file:
            json.dump(data, file)

root = Tk()
app = App(root)
root.mainloop()
