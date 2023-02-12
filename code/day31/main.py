from turtle import Turtle,Screen #importing all required modules
tur=Turtle()
screen=Screen()                 # creating screen
#defining function for all key
def up():
    tur.setheading(90)
    tur.forward(10)
def down():
    tur.setheading(270)
    tur.forward(10)
def right():
    tur.setheading(0)
    tur.forward(10)
def left():
    tur.setheading(180)
    tur.forward(10)
def erase():
    tur.clear()
    tur.home()
    tur.penup()
    tur.pendown()
def circle():
    tur.circle(100)
#instructions
screen.title("Click up,down,left,right for up,down,left and right and c for circle and e for erase")
#assining functions to key
screen.onkey(fun=up,key="Up")
screen.onkey(fun=down,key="Down")
screen.onkey(fun=left,key="Left")
screen.onkey(fun=right,key="Right")
screen.onkey(fun=erase,key="e")
screen.onkey(fun=circle,key="c")
# assigning function while pressing
screen.onkeypress(fun=up,key="Up")
screen.onkeypress(fun=down,key="Down")
screen.onkeypress(fun=left,key="Left")
screen.onkeypress(fun=right,key="Right")
screen.onkeypress(fun=erase,key="e")
screen.listen()

screen.exitonclick()