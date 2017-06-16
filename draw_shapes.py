from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(600, 600)
goto(0,0)

### Write your code below:

sides = int(input("Enter the number of sides: "))
color = input("Enter the color of your shape: ")
print("Your shape will be", color, "and have", sides, "sides.")

def drawShapeRight():
    for i in range(sides):
        fillcolor(color)
        pencolor(color)
        begin_fill()
        pensize(10)
        pendown()
        forward(100)
        right(360/sides)
        penup()
        end_fill()
def drawShapeBackwardRight():
    for i in range(sides):
        fillcolor(color)
        pencolor(color)
        begin_fill()
        pensize(10)
        pendown()
        back(100)
        right(360/sides)
        penup()
        end_fill()

def drawShapeLeft():
    for i in range(sides):
        fillcolor(color)
        pencolor(color)
        begin_fill()
        pensize(10)
        pendown()
        forward(100)
        left(360/sides)
        penup()
        end_fill()

def drawShapeBackwardLeft():
    for i in range(sides):
        fillcolor(color)
        pencolor(color)
        begin_fill()
        pensize(10)
        pendown()
        back(100)
        left(360/sides)
        penup()
        end_fill()

def tessTri():
    for i in range(4):
        drawShapeRight()
        drawShapeBackwardRight()
        drawShapeLeft()
        drawShapeBackwardLeft()
        forward(200)

def tessHex():
    for i in range(4):
        drawShapeRight()
        drawShapeBackwardRight()
        forward(200)

speed(0)
drawShapeRight()
print("Here is your shape!")

yes = input("Do you want to draw a tessellation? ")
if yes == "yes":
    tessellation = input("Do you want your tessellation to be made with triangles or hexagons? ")
    if tessellation == "triangles":
        clear()
        sides = 3
        speed(0)
        pensize(1)
        goto(-300, -200)
        tessTri()
        goto(-350, -100)
        tessTri()
        goto(-300, 0)
        tessTri()
        goto(-350, 100)
        tessTri()
        goto(-300, 200)
        tessTri()
        print("Here is your tessellation of triangles!")
    if tessellation == "hexagons":
        clear()
        sides = 6
        speed(0)
        pensize(1)
        goto(-300, -200)
        tessHex()
        goto(-300, 150)
        tessHex()
        print("Here is your tessellation of hexagons!")



# Close window on click.
exitonclick()
