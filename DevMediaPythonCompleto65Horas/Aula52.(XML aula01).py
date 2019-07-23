import xml.etree.ElementTree as ET
from tkinter import *
import os.path

class App:

    def __init__(self,master):
        master.geometry("300x150")
        master.title("Meu XML Exemplo.")
        frame = Frame(master)
        frame.pack()


        self.btSave = Button(frame, text="Save into XML file", command="saveXML")
        self.btSave.pack(side=LEFT)

        frameName = Frame(root)
        frameName.pack(side=BOTTOM, pady=10)
        self.labelName = Label(frameName, text="Name: ")
        self.labelName.pack(side=LEFT, padx=5)
        self.inputName = Entry(frameName)
        self.inputName.pack(side=LEFT, padx=5)

        frameID = Frame(root)
        frameID.pack(side=BOTTOM, pady=10)
        self.labelID = Label(frameName, text="ID: ")
        self.labelID.pack(side=LEFT, padx=5)
        self.inputID = Entry(frameName)
        self.inputID.pack(side=LEFT, padx=5)


def saveXML(self):
    fileName = "customers.xml"
    if os.path.isfile(fileName):
        tree = ET.parse(fileName)
        root = tree.getroot()
        doc = ET.SubElement(root, "customer")

        ET.SubElement(doc, "id", name="id_attribute").text = str(self.inputID.get())

        ET.SubElement(doc, "name").text = str(self.inputID.get())

        saveTree = ET.ElementTree(root)
        saveTree.write(fileName)
    else:

        root = ET.Element("root")
        doc = ET.SubElement(root, "customer")
        ET.SubElement(doc, "id", name="id_attribute").text = str(self.inputID.get())
        ET.SubElement(doc, "name").text = str(self.inputID.get())

        saveTree = ET.ElementTree(root)
        saveTree.write(fileName)

root = Tk()
app= App(root)
root.mainloop()

