from lxml import etree
from tkinter import *
import os.path

class App:

    def __init__(self, master):
        master.geometry("300x150")
        master.title("Minha validação XML Exemplo")
        frame = Frame(master)
        frame.pack()


        self.btValidate = Button(frame, text="Validate XML File", command= self.validateXML)
        self.btValidate.pack(side=LEFT)
        frameLabel = Label(root)
        frameLabel.pack(side=BOTTOM, pady=10, expand=TRUE, fill=BOTH)

        self.lblValidade = Label(frameLabel)
        self.lblValidade.pack(side=LEFT, expand=TRUE, fill=BOTH)


    def validateXML(self):
        try:
            XLMfileName = "validate_custumers.xml"

            XSDfileName = "validate_custumers.xsd"

            if os.path.isfile(XLMfileName) and os.path.isfile(XSDfileName):

                xmlschema_doc = etree.parse(XSDfileName)
                xmlschema = etree.XMLSchema(xmlschema_doc)

                xml_file = etree.parse(XLMfileName)

                if xmlschema.validate(xml_file):
                    self.lblValidade.config(text="XML is Validate")
                else:
                    self.lblValidade.config(text="XML Not is Validate!")
            else:
                print("File not exist")

        except etree.XMLSyntaxError:
            self.lblValidade.config(text="XML ERROR")
        except etree.DocumentInvalid:
            self.lblValidade.config(text="XmL Not is Validate")



root = Tk()

app =App(root)
root.mainloop()