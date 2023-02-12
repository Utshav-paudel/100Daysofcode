#creating triangle,square,pentagon,hexagon,heptagon,ocatgon,nonagon,and decagon with random colour

from turtle import Turtle,Screen          #importing of libraries
import random

tur=Turtle()
def draw_shape(num_sides):                #creating function that draw shape as we pass
    angle=360/num_sides                   #number of sides
    for i in range(num_sides):
        tur.forward(100)
        tur.left(angle)
        
for i in range(3,11):                    #loop that fulfill all our shapes upto decagon
    tur.color(random.choice(["red","green","blue","yellow","orange"]))
    draw_shape(i)


Screen().exitonclick()