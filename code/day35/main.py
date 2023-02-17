from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

tur=Turtle()
screen=Screen()
#setting up the screen
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("snake game")
screen.tracer(0)    # for smooth animation while moving

# snake body
snake = Snake()
# food
food = Food()
# scoreboard
scoreboard = Scoreboard()

# key movement
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# snake movement
gameon = True
while gameon:
    time.sleep(0.1)   # creating delay for smooth animation
    screen.update()
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.referesh() 
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        gameon = False
        scoreboard.gameover()

    # detect collision with snake
    for segmen in snake.segment:
        if segmen == snake.head:
            pass
        elif snake.head.distance(segmen) <10:
            gameon = False
            scoreboard.gameover()



        
screen.exitonclick()