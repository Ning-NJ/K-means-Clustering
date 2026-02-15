from turtle import Turtle, Screen
from Kmeans import kMean, randomCoords
import random

colors = ["blue", "red", "orange", "steel blue", "purple", "black", "hot pink", "saddle brown", "silver", "dark slate gray"]
GlobalCoords = []
GlobalCen = []

def unGroupClicked(x, y):
    global GlobalCoords
    if len(GlobalCoords) == 0:
        message = "Please Group coordinates first"
        clearMessage()
        showMessage(message, -350, -100, 10, True, tTempWrite)
        return 0
    draw.clear()
    global GlobalCen
    GlobalCen.clear()
    for coord in GlobalCoords:
        draw.goto(coord.getX(), coord.getY())
        draw.dot(5)
    scr.update()

def drawGroupClicked(x, y):
    if len(GlobalCoords) == 0:
        clearMessage()
        message = "Please draw some coordinates first"
        showMessage(message, -350, -100, 10, True, tTempWrite)
        return 0
    cenNum = scr.numinput("Group Number","How many groups do you want?", minval=1, maxval=min(10, len(GlobalCoords)))
    if cenNum == None:
        return 0
    result = kMean(GlobalCoords, -200, 500, -350, 350, cenNum)
    groups = result[0]
    global GlobalCen
    GlobalCen = result[1]
    draw.clear()
    usedColors = []
    for coords in groups:
        color = chooseColor(colors, usedColors)
        usedColors.append(color)
        for coord in coords:
            draw.goto(coord.getX(), coord.getY())
            draw.dot(5, color)

    scr.update()

def chooseColor(colors, usedcolors):
    colorCopy = []
    colorCopy.extend(colors)
    for i in usedcolors:
        colorCopy.remove(i)
    return random.choice(colorCopy)

def clearClicked(x, y):
    draw.clear()
    global GlobalCoords, GlobalCen
    GlobalCoords.clear()
    GlobalCen.clear()
    scr.update()

def drawCoordClicked(x, y):
    draw.clear()
    global GlobalCoords, GlobalCen
    GlobalCoords.clear()
    GlobalCen.clear()
    cordNum = scr.numinput("Coordinate Number","How many coordinates do you want?", minval=1, maxval=1000)
    if cordNum == None:
        return 0
    GlobalCoords = randomCoords(cordNum, -195, 495, -345, 345)
    for coord in GlobalCoords:
        draw.goto(coord.getX(), coord.getY())
        draw.dot(5)
    scr.update()

def DrawCenClicked(x, y):
    global GlobalCen
    if len(GlobalCen) == 0:
        clearMessage()
        message = "Please group coordinates first"
        showMessage(message, -350, -100, 10, True, tTempWrite)
        return 0
    for cen in GlobalCen:
        draw.goto(cen.getX(), cen.getY())
        draw.dot(15)
    scr.update()

def drawRectangle(forwards):
    t.pendown()
    t.fillcolor("khaki")
    t.begin_fill()
    for i in forwards:
        t.forward(i)
        t.right(90)
    t.end_fill()
    t.penup()

def showMessage(message, x, y, size, erase, turtle):
    turtle.goto(x, y)
    turtle.write(message, align= "center", font = ("Arial", size, "bold"))
    scr.update()
    if erase == True:
        scr.ontimer(clearMessage, 5000)

def clearMessage():
    tTempWrite.clear()
    scr.update

def drawUI():
    t.goto(-500, 350)
    forwards = [300, 700, 300, 700]
    drawRectangle(forwards)
    buttonCoords = []

    for i in range (len(buttons)):
        x = -410
        yChange = i
        if (i+1)%2 == 0:
            x = -300
            yChange = i-1
        newBCoord = [x, 280-40*yChange]
        buttonCoords.append(newBCoord)
        buttons[i].goto(newBCoord)

    for i in buttons:
        i.shape('square')
        i.color('dark gray')
        i.turtlesize(stretch_wid=2, stretch_len=4, outline=2)

    t.setheading(90)
    t.goto(150, -350)
    t.pendown()
    t.forward(750)
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.setheading(0)
    t.forward(750)
    scr.update()

    buttonNames = ["Draw Coordinates", "Group", "Draw Centroids","Degroup", "Clear"]

    for i in range (len(buttonNames)):
        showMessage(f"{buttonNames[i]}", buttonCoords[i][0], buttonCoords[i][1]+25, 7, False, tWrite)
    scr.update()

scr = Screen()
scr.setup(1000, 700)
scr.tracer(0, 0)
scr.title("K-Mean Clustering")
drawCordButton = Turtle()
drawGroupButton = Turtle()
clearButton = Turtle()
unGroup = Turtle()
drawCen = Turtle()
buttons = [drawCordButton, drawGroupButton, drawCen, unGroup, clearButton]
t = Turtle()
draw = Turtle()
tWrite = Turtle()
tTempWrite = Turtle()
turtles = [t, draw, tWrite, tTempWrite]
for turtle in turtles:
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
for i in buttons:
    i.speed(0)
    i.penup()

drawUI()

unGroup.onclick(unGroupClicked)
clearButton.onclick(clearClicked)
drawCordButton.onclick(drawCoordClicked)
drawGroupButton.onclick(drawGroupClicked)
drawCen.onclick(DrawCenClicked)

scr.mainloop()