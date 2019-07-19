from tkinter import *
import random

def mousePressed(event):
    canvas = event.widget.canvas
    redraAll(canvas)

def keyPressed(event):
    canvas = event.widget.canvas
    canvas.data["ignoreNextTimerEvent"] = True
    if (event.char == "q"):
        gameOver(canvas)
    elif(event.char == "r"):
        init(canvas)
    if(canvas.data["isGameOver"] ==False):
        if(event.keysym == "Up"):
            moveSnake(canvas,-1,0)
        elif(event.keysym == "Down"):
            moveSnake(canvas,+1,0)
        elif (event.keysym == "Left"):
            moveSnake(canvas, 0, -1)
        elif (event.keysym == "Right"):
            moveSnake(canvas, 0,+1)
    redraAll(canvas)

def moveSnake(canvas, drow, dcol):
    canvas.data["snakeDrow"] = 0
    canvas.data["snakeDcol"] = -1
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    headRow = canvas.data["headRow"]
    headCol = canvas.data["headCol"]
    newHeadRow = headRow + drow
    newHeadCol = headCol + dcol
    if((newHeadRow<0)or (newHeadRow >=rows) or (newHeadCol < 0) or (newHeadCol >= cols)):
        gameOver(canvas)
    elif(snakeBoard[newHeadRow][newHeadCol]>0):
        gameOver(canvas)
    elif(snakeBoard[newHeadRow][newHeadCol]<0):
        snakeBoard[newHeadRow][newHeadCol] = 1 + snakeBoard[newHeadRow][newHeadCol]
        canvas.data["headRow"] = newHeadRow
        canvas.data["headCol"] =  newHeadCol
        placeFood(canvas)
    else:
        snakeBoard[newHeadRow][newHeadCol] = 1 + snakeBoard[HeadRow][HeadCol]
        canvas.data["headRow"] = newHeadRow
        canvas.data["headCol"] = newHeadCol
        removeTail(canvas)

def removeTail(canvas):
    snakeBoard = canvas.data["snakeBorad"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            if (snakeBoard[row][col]>0):
                snakeBoard[row][col]-=1


def gameOver(canvas):
    canvas.data["isGameOver"] = True
def timerFired(canvas):
    ignoreThisTimerEvent = canvas.data["ignoreNextTimerEvent"]
    canvas.data["ignoreNextTimerEvent"] = False
    if ((canvas.data["isGameOver"] == False) and (ignoreThisTimerEvent == False)):
        drow = canvas.data["snakeDrow"]
        dcol = canvas.data["snakeDcol"]
        moveSnake(canvas,drow,dcol)
        redraAll(canvas)
    delay = 150
    canvas.after(delay,timerFired,canvas)

def redraAll(canvas):
    canvas.delete(ALL)
    drawSnakBoard(canvas)
    if (canvas.data["isGameOver"] == True):
        cx = canvas.data["canvasWidth"]/2
        cy = canvas.data["canvasHeight"]/2
        canvas.creat_text(cx,cy,text="Game Over!!!", font=("Helvetica",32,"bold"))
        
def drawSnakBoard(canvas):
    snakeBoard=canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            drawSnakeCell(canvas,snakeBoard,row,col)

def drawSnakeCell(canvas, snakeBoard,row,col):
    margin = canvas.data["margin"]
    cellSize = canvas.data["cellSize"]
    left = margin + col * cellSize
    right = left + cellSize
    top = margin + row * cellSize
    bottom = top + cellSize
    canvas.create_rectangle(left,top,right,bottom, fill="white")
    if (snakeBoard[row][col]>0):
        canvas.create_oval(left,top,right,bottom, fill="blue")
    elif(snakeBoard[row][col]< 0):
        canvas.create_oval(left,top,right,bottom,fill="green")



def placeFood(canvas):
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    while True:
        row = random.randint(0, rows -1)
        cols = random.randint(0, cols -1)
        if (snakeBoard[row][col] == 0):
            break
        snakeBoard[row][col] = -1

def findSnakeHead(canvas):
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    headRow= 0
    headCol= 0
    for row in range(rows):
        for col in range(cols):
            if(snakeBoard[row][col] > snakeBoard[headRow][headCol]):
                headRow = row
                headCol = col
    canvas.data["headRow"] = headRow
    canvas.data["headCol"] = headCol

def loadSnakeBoard(canvas):
    rows = canvas.data["rows"]
    cols = canvas.data["rols"]
    snakeBoard= []
    for row in range(rows): snakeBoard += [[0] * cols]
    snakeBoard[int(rows/2)] [int(cols/2)] = 1
    canvas.data["snakeBoard"] = snakeBoard
    findSnakeHead(canvas)
    placeFood(canvas)
def printInstructions():
    print()
    print("Snake")
    print("Cobra")
    print("Use the arrow keys to  move the snake")
    print("Use as setas para controlar a cobra")
    print("Eat food to grow")
    print("Coma comida para crescer")
    print("Stay on the board and dont crash into yourself")
    print("Fique dentro da borda e nao bata em si mesmo!")
    print("Press 'r' to restart ")
    print("Precione 'r' para reniciar")
    print()

def init(canvas):
    printInstructions()
    loadSnakeBoard(canvas)
    canvas.data["isGameOver"] = False
    canvas.data["snakeDrow"] = 0
    canvas.data["snakeDool"] = -1
    canvas.data["ignoreNextTimeEvent"] = False
    redraAll(canvas)
    
def run(rows, cols):
    root = Tk()
    margin = 10
    cellSize = 30
    canvasWidth = 2*margin + cols*cellSize
    canvasHeight = 2*margin + cols*cellSize
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()
    root.resizable(width=0, height=0)
    root.canvas=canvas.canvas=canvas
    canvas.data={}
    canvas.data["margin"]=margin
    canvas.data["cellSize"]=cellSize
    canvas.data["canvasWidth"]=canvasWidth
    canvas.data["canvasHeight"]=canvasHeight
    canvas.data["rows"] = rows
    canvas.data["cols"] = cols
    init(canvas)
    root.bind("<Button-1>", mousePressed)
    root.bind("<key>", keyPressed)
    timerFired(canvas)
