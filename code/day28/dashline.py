from  turtle import Turtle,Screen
tur=Turtle()
#creating dash line
for i in range(15):
    tur.forward(10)
    tur.penup()
    tur.forward(10)
    tur.pendown()
Screen().exitonclick()