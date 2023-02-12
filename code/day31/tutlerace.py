import random
from turtle import Turtle,Screen
screen=Screen()
screen.setup(width=500,height=400)   #setting screen size
race_on=False
#creating user input for bet
user_bet=screen.textinput(title="Make your bet",prompt="whicht turtle will win the race? Enter a color:")
print(user_bet)
#creating list for turtle colors
color=["red","green","yellow","blue","orange","purple"]
# changing y axis make turtle in diff positon in start
y_position=[-100,-60,-20,20,60,100]
new_tur=[]
#putting turtle to start
for i in range(6):
    tur=Turtle()
    tur.shape("turtle")
    tur.color(color[i])
    tur.penup()
    tur.goto(x=-230,y=y_position[i])
    new_tur.append(tur)

if user_bet:
    race_on=True
while race_on:
    for turtle in new_tur:
        if turtle.xcor()>230:
                race_on=False
                winning_tur=turtle.pencolor()
                if winning_tur==user_bet:
                    print(f"You've won {winning_tur} is the winner")
                else:
                    print(f"You've lost {winning_tur} is the winner")
        turtle.forward(random.randint(0,10))
screen.exitonclick()