from tkinter import *

root = Tk()

def onselect(event):
    myW = event.widget
    index = int(myW.curselection()[0])

    value = myW.get(index)
    print('You selected item %d: "%s"' %(index, value))

myScrollbar = Scrollbar(root)
myScrollbar.pack(side=RIGHT, fill=Y)

myList = Listbox(root, yscrollcommand=myScrollbar.set)

for item in range(100):
    myList.insert(END, "item " + str(item))
myList.pack(side=LEFT, fill=BOTH)
myList.bind("<<ListboxSelect>>",onselect)
myScrollbar.config(command=myList.yview)
mainloop()