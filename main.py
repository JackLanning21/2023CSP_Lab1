# Import Turtle
import turtle as trtl

# Declare Turtles.
# ONLY USE THE lines TURTLE!!!!
box = trtl.Turtle()
lines = trtl.Turtle()
wn = trtl.Screen()
Startx = -490
Starty = -300
Endx = 490
Endy = -300
lines.speed(400)

# Setup Screen
def setupScreen():
    global wn
    wn.setup(1000, 700)

# Create the box on the screen
def setupBox():
    box.speed(0)
    box.penup()
    box.goto(-490, -300)
    box.pendown()
    box.forward(980)
    box.left(90)
    box.forward(630)
    box.left(90)
    box.forward(980)
    box.left(90)
    box.forward(630)
    box.hideturtle()


# Code for 80 point version goes here
def v80():
    global Startx
    global Starty
    global Endx
    global Endy
    lines.penup()
    lines.goto(Startx,Starty)
    lines.pendown()
    for x in range(50):
        lines.penup()
        lines.goto(Endx, Endy)
        lines.pendown()
        lines.goto(Startx, Starty)
        Startx += 19.6
        Endy += 12.6

# Code for the 90 point version goes here
def v90():
    # Calling the 80 point function - don't copy-paste from earlier method!!
    v80()
    global Startx
    global Starty
    global Endx
    global Endy
    lines.penup()
    lines.goto(-Startx, Starty)
    lines.pendown()
    Endy -= 638
    for x in range(50):
        lines.penup()
        lines.goto(Startx, Starty)
        lines.pendown()
        lines.goto(-Endx, Endy)
        Startx -= 19.6
        Endy += 12.6

# Code for the 100 point version here
def v100():
    # Calling the 90 point function - don't copy-paste from earlier method!!
    v90()
    global Startx
    global Starty
    global Endx
    global Endy
    lines.penup()
    lines.goto(Startx, -Starty)
    lines.pendown()
    Endy -= 630
    Starty += 630
    for x in range(50):
        lines.penup()
        lines.goto(Startx, Starty)
        lines.pendown()
        lines.goto(Endx, -Endy)
        Startx += 19.6
        Endy += 12.6
    lines.penup()
    lines.goto(-Startx, Starty)
    lines.pendown()
    Endy -= 630
    for x in range(50):
        lines.penup()
        lines.goto(Startx, Starty)
        lines.pendown()
        lines.goto(-Endx, -Endy)
        Startx -= 19.6
        Endy += 12.6

# Code for the 110 point version here

Startx2 = -245
Starty2 = -142.5
Endx2 = 245
Endy2 = -142.5
def v110():
    # Calling the 100 point function - don't copy-paste from earlier method!!
    v100()
    global Startx2
    global Starty2
    global Endx2
    global Endy2
    lines.penup()
    lines.goto(Startx2, Starty2)
    lines.pendown()
    for x in range(50):
        lines.penup()
        lines.goto(Endx2, Endy2)
        lines.pendown()
        lines.goto(Startx2, Starty2)
        Startx2 += 9.8
        Endy2 += 6.15
    lines.goto(Startx2, Starty2)
    lines.penup()
    lines.goto(-Startx2, Starty2)
    lines.pendown()
    Endy2 -= 307.5
    for x in range(50):
        lines.penup()
        lines.goto(Startx2, Starty2)
        lines.pendown()
        lines.goto(-Endx2, Endy2)
        Startx2 -= 9.8
        Endy2 += 6.15
    lines.penup()
    lines.goto(Startx2, -Starty2)
    lines.pendown()
    Endy2 -= 329
    Starty2 += 307.5
    for x in range(50):
        lines.penup()
        lines.goto(Startx2, Starty2)
        lines.pendown()
        lines.goto(Endx2, -Endy2)
        Startx2 += 9.8
        Endy2 += 6.15
    lines.penup()
    lines.goto(-Startx2, Starty2)
    lines.pendown()
    Endy2 -= 307.5
    for x in range(50):
        lines.penup()
        lines.goto(Startx2, Starty2)
        lines.pendown()
        lines.goto(-Endx2, -Endy2)
        Startx2 -= 9.8
        Endy2 += 6.15

setupScreen()
setupBox()
v110()





wn.mainloop()
