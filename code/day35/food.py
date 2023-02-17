from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.referesh()

        
    def referesh(self):
        rand_x=random.choice(range(-270,270))
        rand_y=random.choice(range(-270,270))

        self.goto(rand_x,rand_y)
