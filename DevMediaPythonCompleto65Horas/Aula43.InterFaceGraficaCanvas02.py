from tkinter import *


class PaintBox(Frame):


    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Paint with Python")
        self.master.geometry("500x500")

        self.message = Label(self, text="Drag the mouse to draw")
        self.message.pack(side=BOTTOM)

        self.myCanvas = Canvas(self)
        self.myCanvas.pack(expand=YES, fill=BOTH)

        self.myCanvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x1,y1 = (event.x -2 ), (event.y -2 )
        x2,y2 = (event.x +2 ), (event.y +2 )
        self.myCanvas.create_oval(x1,y1,x2,y2,fill="Blue", outline="red")

def main():
    PaintBox().mainloop()

if __name__ == "__main__":
    main()

