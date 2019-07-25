#!C:\Users\rolim\AppData\Local\Programs\Python\Python37-32\python.exe
"""
Sistema de Gerenciamento de produtos! Projeto prático!
"""
from tkinter import *
import mysql.connector

def loadEntry():
    print()
def addEntry():

    print()
def updateEntry():
    print()
def deleteEntry():
    print()

def initWindow():
    global listProduct#definindo escopo global
    windowInit = Tk()
    windowInit.title("Products")

    frame1 = Frame(windowInit)
    frame1.pack()
    btnLoad = Button(frame1, text="  Load  ", command=loadEntry)
    btnAdd = Button(frame1, text="  Add  ", command=addEntry)
    btnUpdate = Button(frame1, text="Update", command=updateEntry)
    btnDelete = Button(frame1, text="  Delete  ", command=deleteEntry)

    btnLoad.pack(side=LEFT)
    btnAdd.pack(side=LEFT)
    btnUpdate.pack(side=LEFT)
    btnDelete.pack(side=LEFT)

    frame2 = Frame(windowInit)
    frame2.pack()
    scroll = Scrollbar(frame2, orient=VERTICAL)
    listProduct = Listbox(frame2, yscrollcommand=scroll.set, height=5)
    scroll.config(command=listProduct.yview)
    scroll.pack(side=RIGHT, fill=Y)
    listProduct.pack(side=LEFT, fill=BOTH, expand=1)
    return windowInit

def setList ():

    cnx = mysql.connector.connect(host='localhost', database='guestsbook', user='root', password='')
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM tbproducts')
    for(id, product, descripition, quantity, price) in cursor:
        listProduct.insert(END, product)
    cursor.close()
    cnx.close()

win = initWindow()
setList()
win.mainloop()