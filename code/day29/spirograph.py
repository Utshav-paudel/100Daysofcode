from turtle import Turtle,Screen
import turtle as t
import random

tur=Turtle()
t.colormode(255)
tur.speed("fastest")

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color_=(r,g,b)
    return color_
gap=int(input())
for i in range(int(360/gap)):
    tur.color(random_color())
    tur.circle(100)
    tur.setheading(tur.heading()+gap)
    tur.circle(100)

# spirograph()
screen=Screen()
screen.exitonclick()
