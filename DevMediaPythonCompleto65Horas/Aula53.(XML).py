import xml.etree.ElementTree as ET
from tkinter import *
import os.path

g_customer_count = 0

class App:

    def __init__(self, master):
        master.geometry("300x150")
        master.title("my XML Exemplo")
        frame = Frame(master)
        frame.pack()

        self.btRead = Button(frame, text="Read Elementes in XML File", command=self.readXML)
        self.btRead.pack(side=LEFT)

        self.lblCount = Label(frame)
        self.lblCount.pack(side=LEFT)

        frameName = Frame(root)
        frameName.pack(side=BOTTOM, pady=10)
        self.labelName = Label(frameName, text="Name: ")
        self.labelName.pack(side=LEFT)
        self.inputName = Entry(frameName)
        self.inputName.pack(side=LEFT, padx=5)


        frameID = Frame(root)
        frameID.pack(side=BOTTOM, pady=10)
        self.labelID = Label(frameID, text="ID: ")
        self.labelID.pack(side=LEFT)
        self.inputID = Entry(frameID)
        self.inputID.pack(side=LEFT, padx=5)


    def readXML(self):
        fileName = "customers.xml"

        if os.path.isfile(fileName):

            global g_customer_count

            tree = ET.parse(fileName)
            root = tree.getroot()
            self.inputID.delete(0,'end')
            self.inputName.delete(0,'end')

            self.inputID.insert(INSERT, str(root[g_customer_count][0].text))
            self.inputName.insert(INSERT, str(root[g_customer_count][1].text))

            count = 0

            for customer in root.iter('customer'):
                count +=1

            self.lblCount.config(text=str(g_customer_count + 1)+ "/ "+str(count))
            if g_customer_count < count - 1:
                g_customer_count = g_customer_count +1
        else:

            print("File nao existe!")

root = Tk()
app = App(root)
root.mainloop()