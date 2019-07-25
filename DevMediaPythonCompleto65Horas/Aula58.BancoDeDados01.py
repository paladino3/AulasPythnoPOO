#!C:\Users\rolim\AppData\Local\Programs\Python\Python37-32\python.exe
"""
Sistema de Gerenciamento de produtos! Projeto prático!
"""
from tkinter import *
import mysql.connector

def whichSelected():
    if len(listProduct.curselection())>0:
        return int(listProduct.curselection()[0]) +1
    else:
        return -1

def loadEntry():
    id= whichSelected()
    if id > 0:
        windowLoad = Toplevel()
        windowLoad.title("Loaded Product")
        frame1 = Frame(windowLoad)
        frame1.pack()

        cnx = mysql.connector.connect(host='localhost', database='guestsbook', user='root', password='')
        cursor = cnx.cursor()
        cursor.execute('SELECT * FROM tbproducts WHERE id=' + str(id))
        row = cursor.fetchone()#pegar as info desta selecao no banco de  dados

        Label(frame1, text="ID").grid(row=0, column=0, sticky=W)
        idVar=StringVar()
        idVar.set(str(row[0]))
        entryId = Entry(frame1, textvariable=idVar, state=DISABLED)
        entryId.grid(row=0, column=1, sticky=W)

        Label(frame1, text="Product").grid(row=1, column=0, sticky=W)
        productVar = StringVar()
        productVar.set(str(row[1]))
        entryProduct = Entry(frame1, textvariable=productVar, state=DISABLED)
        entryProduct.grid(row=0, column=1, sticky=W)

        Label(frame1, text="Descripition").grid(row=1, column=0, sticky=W)
        descripitionVar = StringVar()
        descripitionVar.set(str(row[2]))
        entryDescripition = Entry(frame1, textvariable=descripitionVar, state=DISABLED)
        entryDescripition.grid(row=2, column=1, sticky=W)

        Label(frame1, text="Quantity").grid(row=3, column=0, sticky=W)
        quantityVar = StringVar()
        quantityVar.set(str(row[3]))
        entryQuantity = Entry(frame1, textvariable=quantityVar, state=DISABLED)
        entryQuantity.grid(row=3, column=1, sticky=W)

        Label(frame1, text="Price").grid(row=4, column=0, sticky=W)
        priceVar = StringVar()
        priceVar.set(str(row[4]))
        entryPrice = Entry(frame1, textvariable=priceVar, state=DISABLED)
        entryPrice.grid(row=4, column=1, sticky=W)
    else:
        print("Please select a product")


def addEntry():

    windowAdd = Toplevel()
    windowAdd.title("Add Product")
    frame1 = Frame(windowAdd)
    frame1.pack()

    Label(frame1, text="Product").grid(row=0, column=0, sticky=W)
    entryProduct = Entry(frame1)
    entryProduct.grid(row=0, column=1,sticky=W)

    Label(frame1, text="Descripition").grid(row=1, column=0, sticky=W)
    entryDescripition = Entry(frame1)
    entryDescripition.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Quantity").grid(row=2, column=0, sticky=W)
    entryQuantity = Entry(frame1)
    entryQuantity.grid(row=2, column=1, sticky=W)

    Label(frame1, text="Price").grid(row=3, column=0, sticky=W)
    entryPrice = Entry(frame1)
    entryPrice.grid(row=3, column=1, sticky=W)

    def saveAdd():

        newProduct = entryProduct.get()
        newDescripition = entryDescripition.get()
        newQuantity = entryQuantity.get()
        newPrice = entryPrice.get()

        cnx = mysql.connector.connect(host='localhost', database='guestsbook', user='root', password='')
        cursor = cnx.cursor()
        add_product = ("INSERT INTO tbproducts (product, descripition, quantity, price) VALUES (%s,%s,%s,%s)")
        data_product = (newProduct, newDescripition, newQuantity, newPrice)

        cursor.execute(add_product,data_product)
        cnx.commit()

        cursor.close()
        cnx.close()
        print("ADD OK")
        setList()#aqui atualiza a lista de produtos

    btnSaveAdd = Button(frame1, text="Salvar", command=saveAdd)
    btnSaveAdd.grid(row=4, column=1, sticky=W)


def updateEntry():
    id = whichSelected()

    if id > 0:
        windowUpdate = Toplevel()
        windowUpdate.title("Update Product")
        frame1 = Frame(windowUpdate)
        frame1.pack()

        cnx = mysql.connector.connect(host='localhost', database='guestsbook', user='root', password='')
        cursor = cnx.cursor()
        cursor.execute('SELECT * FROM tbproducts WHERE id=' + str(id))
        row = cursor.fetchone()  # pegar as info desta selecao no banco de  dados

        Label(frame1, text="ID").grid(row=0, column=0, sticky=W)
        idVar = StringVar()
        idVar.set(str(row[0]))
        entryId = Entry(frame1, textvariable=idVar, state=DISABLED)
        entryId.grid(row=0, column=1, sticky=W)

        Label(frame1, text="Product").grid(row=1, column=0, sticky=W)
        productVar = StringVar()
        productVar.set(str(row[1]))
        entryProduct = Entry(frame1, textvariable=productVar)
        entryProduct.grid(row=0, column=1, sticky=W)

        Label(frame1, text="Descripition").grid(row=1, column=0, sticky=W)
        descripitionVar = StringVar()
        descripitionVar.set(str(row[2]))
        entryDescripition = Entry(frame1, textvariable=descripitionVar)
        entryDescripition.grid(row=2, column=1, sticky=W)

        Label(frame1, text="Quantity").grid(row=3, column=0, sticky=W)
        quantityVar = StringVar()
        quantityVar.set(str(row[3]))
        entryQuantity = Entry(frame1, textvariable=quantityVar)
        entryQuantity.grid(row=3, column=1, sticky=W)

        Label(frame1, text="Price").grid(row=4, column=0, sticky=W)
        priceVar = StringVar()
        priceVar.set(str(row[4]))
        entryPrice = Entry(frame1, textvariable=priceVar)
        entryPrice.grid(row=4, column=1, sticky=W)

        def saveUpdate():
            updateId = int (entryId.get())
            updateProduct = entryProduct.get()
            updateDescripition = entryDescripition.get()
            updateQuantity = entryQuantity.get()
            updatePrice = entryPrice.get()

            cnx = mysql.connector.connect(host='localhost', database='guestsbook', user='root', password='')
            cursor = cnx.cursor()
            update_product = ("UPDATE tbproducts SET product=%s, descripition=%s , quantity=%s, price=%s WHERE id=%s")
            data_product= (updateProduct, updateDescripition, updateQuantity, updatePrice, updateId)

            cursor.execute(update_product, data_product)
            cnx.commit()

            cursor.close()
            cnx.close()
            print("UPDATE OK")
            setList()  # aqui atualiza a lista de produtos

        btnSaveUpdate = Button(frame1, text="Update", command=saveUpdate)
        btnSaveUpdate.grid(row=5, column=1, sticky=W)

    else:
        print("Please select a product")


def deleteEntry():
    id = whichSelected()

    if id > 0:
        cnx = mysql.connector.connect(host='localhost', database='guestsbook', user='root', password='')
        cursor = cnx.cursor()
        delete_product=("DELETE FROM tbproducts WHERE id=" + str(id))
        cursor.execute(delete_product)
        cnx.commit()

        cursor.close()
        cnx.close()
        print("Produto Deletado! com sucesso")
        setList()
    else:
        print("Please select a product")

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