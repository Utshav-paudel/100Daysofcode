# we will write code in such a way that turtle move in randome direction with random colour
from turtle import Turtle,Screen
import turtle as t
import random
tur=Turtle()
#creating a function for random color
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color


tur.pensize(15)
tur.shape("turtle")
#loop that generate randomwalk

for i in range(100):
    tur.forward(30)
    tur.setheading(random.choice([0,90,180,270]))
    tur.pencolor(random_color())
screen=Screen()
screen.exitonclick()
