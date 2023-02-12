from turtle import Turtle,Screen #importing everything from turtle module
turt = Turtle()



turt.shape("turtle")  #passing shape to Turtle() function as argument
turt.color("red")

#creating square using turtle
for i in range(4):
    turt.forward(100)
    turt.right(90)
screen=Screen()
screen.exitonclick()
