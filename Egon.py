import random
import turtle
l = []
screen = turtle.Screen()
screen.setup(600, 600)
Egon = turtle.Turtle()
Egon.shape("turtle")
A = turtle.Turtle()
B = turtle.Turtle()
C = turtle.Turtle()
def drawtri():
    A.penup()
    B.penup()
    C.penup()
    A.goto(-210,-260)
    B.goto(150,-150)
    C.goto(0,150)
def drawrect():
    Egon.penup()
    Egon.goto(-300,-300)
    Egon.pendown()
    Egon.goto(300,-300)
    Egon.goto(300,300)
    Egon.goto(-300,300)
    Egon.goto(-300,-300)

drawtri()
drawrect()
Egon.penup()
Egonlocx = random.randint(-300,300)
Egonlocy = random.randint(-300,300)
Egon.goto(Egonlocx,Egonlocy)

l.append(A)
l.append(B)
l.append(C)

t = 0
while t < 5000:
    screen.tracer(0)
    die = random.randint(1, 6)
    if die == 1 or die == 2:
        print(Egon.distance(A))
        halfway = (1 / 2) * Egon.distance(A)
        Egon.setheading(Egon.towards(A))
        Egon.forward(halfway)
        Egon.dot()
    elif die == 3 or die == 4:
        print(Egon.distance(B))
        halfway = (1 / 2) * Egon.distance(B)
        Egon.setheading(Egon.towards(B))
        Egon.forward(halfway)
        Egon.dot()
    elif die == 5 or die == 6:
        print(Egon.distance(C))
        halfway = (1 / 2) * Egon.distance(C)
        Egon.setheading(Egon.towards(C))
        Egon.forward(halfway)
        Egon.dot()
        t += 1
screen.tracer(1)
screen.exitonclick()
'''
for i in range (len(l)):
    Egon.pendown()
    n = random.randint(0, len(l)-1)
    print (Egon.distance(l[n]))
    halfway = (1/2) * Egon.distance(l[n])
    Egon.setheading(Egon.towards(l[n]))
    Egon.forward(halfway)
'''