# import colorgram
# colors = colorgram.extract('hirstpainting.jpg',30)
# newcolor=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colorextracted=(r,g,b)
#     newcolor.append(colorextracted)
# This are the rgb we extracted
color_list=[(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]
import turtle as t
from turtle import Screen
import random
t.colormode(255)
tur=t.Turtle()
t.penup()
t.speed("fastest")
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
def draw():
    for i in range(10):
        t.dot(20,random.choice(color_list))
        t.forward(50)
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)
for i in range(10):
    draw()
screen=Screen()
screen.exitonclick()
