# Patrick Reed
import turtle
wn = turtle.Screen()
wn.mode('logo')

# Microelements
def halfcircle(t, direction, increments):
    if direction == 'right':
        for i in range(180):
            jess.right(1)
            jess.forward(increments)
    elif direction == 'left':
        for i in range(180):
            jess.left(1)
            jess.forward(increments)

# Macroelements
def setup(t):
    jess.penup()
    jess.backward(100)
    jess.left(90)
    jess.forward(200)
    jess.right(90)
    jess.pendown()

def deck(t):
    jess.color('black')
    jess.right(115)
    jess.forward(200)
    for i in range(6):
        jess.left(5)
        jess.forward(30)
    jess.left(90)
    for i in range(5):
        jess.left(12)
        jess.forward(30)
    jess.forward(185)
    jess.left(65)
    jess.forward(125)
    jess.right(130)

def hull(t):
    jess.color('black')
    jess.seth(180)
    jess.forward(21)
    jess.left(65)
    jess.forward(200)
    for i in range(6):
        jess.left(7)
        jess.forward(30)

def gotomast(t):
    jess.penup()
    jess.left(135)
    jess.forward(165)
    jess.seth(0)
    jess.pendown()

def mast(t, height):
    jess.color('gray')
    jess.forward(height)
    halfcircle(jess, 'right', .15)
    jess.forward(height + 6)
    jess.right(110)
    jess.forward(18)

def gotomainsail(t):
    jess.penup()
    jess.seth(0)
    jess.forward(315)
    jess.pendown()

def mainsail(t):
    jess.color('blue')
    jess.left(145)
    jess.forward(220)
    jess.left(100)
    jess.forward(140)

def gotoboom(t):
    jess.penup()
    jess.left(180)
    jess.pendown()

def boom(t):
    jess.color('gray')
    jess.forward(145)
    halfcircle(jess, 'left', .075)
    jess.forward(149)

def gotocrossbar(t):
    jess.penup()
    jess.seth(0)
    jess.forward(175)
    jess.pendown()

def crossbar(t):
    jess.color('gray')
    jess.left(100)
    jess.forward(45)
    halfcircle(jess, 'left', .1)
    jess.forward(95)
    halfcircle(jess, 'left', .1)
    jess.forward(50)

def gotoheadsail(t):
    jess.penup()
    jess.seth(0)
    jess.forward(50)
    jess.right(90)
    jess.forward(16)
    jess.pendown()

def headsail(t):
    jess.color('blue')
    jess.right(71)
    jess.forward(387)
    jess.right(120)
    for i in range(6):
        jess.right(2)
        jess.forward(25)
    jess.seth(26)
    for i in range(7):
        jess.left(6)
        jess.forward(49)

def gotoportlines(t):
    jess.penup()
    jess.seth(0)
    jess.forward(17)
    jess.pendown()

def portlines(t):
    jess.color('violet')
    jess.right(150)
    jess.forward(90)
    jess.seth(180)
    jess.forward(220)

def gotostarboardline(t):
    jess.penup()
    jess.right(150)
    jess.forward(100)
    jess.seth(0)
    jess.forward(210)
    jess.pendown()

def starboardline(t):
    jess.color('violet')
    jess.left(150)
    jess.forward(110)
    jess.seth(180)
    jess.forward(280)

def gotoheadline(t):
    jess.penup()
    jess.seth(0)
    jess.right(63)
    jess.forward(56)
    jess.seth(0)
    jess.pendown()

def headline(t):
    jess.color('black')
    jess.left(90)
    jess.forward(90)

def gotoboomline(t):
    jess.penup()
    jess.seth(0)
    jess.left(15)
    jess.forward(160)
    jess.pendown()

def boomline(t):
    jess.seth(200)
    jess.forward(100)
    
# Full project
def boat(t):
    setup(jess)
    deck(jess)
    hull(jess)
    gotomast(jess)
    mast(jess, 315)
    gotomainsail(jess)
    mainsail(jess)
    gotoboom(jess)
    boom(jess)
    gotocrossbar(jess)
    crossbar(jess)
    gotoheadsail(jess)
    headsail(jess)
    gotoportlines(jess)
    portlines(jess)
    gotostarboardline(jess)
    starboardline(jess)
    gotoheadline(jess)
    headline(jess)
    gotoboomline(jess)
    boomline(jess)
    
# Initializes Turtle
jess = turtle.Turtle()
boat(jess)
# Exits program
wn.exitonclick()