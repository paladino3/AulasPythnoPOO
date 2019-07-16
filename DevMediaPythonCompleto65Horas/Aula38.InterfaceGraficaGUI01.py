"""
Mouse and keyboard event
"""
from tkinter import *
from tkinter import messagebox


class MouseLocation(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack(expand = YES, fill=BOTH)
        self.master.title("Mouse and Keyboard Events")
        self.master.geometry("500x500")

        self.mousePosition = StringVar()#varariaves em widgeth
        self.mousePosition.set("Mouse outside window")
        self.positionLabel = Label(self, textvariable=self.mousePosition)
        self.positionLabel.pack(side=BOTTOM)

        self.bind("<Button-1>", self.buttonLeftClick)
        self.bind("<Button-3>", self.buttonRightClick)
        self.bind("<ButtonRelease-1>", self.buttonLeftRelease)
        self.bind("<Enter>", self.enterWindow)
        self.bind("<Leave>", self.exitWindow)
        self.bind("<B1-Motion>", self.mouseDragged)


        #self.master.bind("<KeyPress>", self.keyPressed)
        #self.master.bind("<KeyRelease", self.keyReleased)

        self.master.bind("<Control-Shift-KeyPress-Tab>", self.comboPressed)
    def buttonLeftClick(self, event):
        self.mousePosition.set("LEFT BUTTON Pressed at [" + str(event.x) + ", " + str(event.y) + "]")

    def buttonRightClick(self, event):
        self.mousePosition.set("RIGHT BUTTON Pressed at [" + str(event.x) + ", " + str(event.y) + "]")

    def buttonLeftRelease(self, event):
        self.mousePosition.set("RIGHT BUTTON Release at [" + str(event.x) + ", " + str(event.y) + "]")

    def buttonRightRelease(self, event):
        self.mousePosition.set("LEFT BUTTON Release at [" + str(event.x) + ", " + str(event.y) + "]")

    def enterWindow(self, event):
        self.mousePosition.set("Mouse in  Window")

    def exitWindow(self, event):
        self.mousePosition.set("Mouse outside  Window")

    def mouseDragged(self, event):
        self.mousePosition.set("Dragged at [" + str(event.x) + ", " + str(event.y) + "]")

    def keyPressed(self, event):
        messagebox.showinfo("Key Pressed", "Any Key Pressed")

    def keyReleased(self, event):
        messagebox.showinfo("Key Released", "Any Key Released")

    def comboPressed(self, event):
        messagebox.showinfo("Keys Pressed", "CTRL + SHIFT + TAB")

def main():
    MouseLocation().mainloop()

if __name__ == "__main__":
    main()