from turtle import Turtle,Screen
FONT = ("Arial",18,"normal")
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        

    def refresh_score(self):
        self.write(f"Score: {self.score}",move=False,align=ALIGN,font=FONT)

    def increase_score(self):
        self.clear()
        self.score  +=  1
        self.refresh_score()

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",move=False,align=ALIGN,font=FONT)


    

        
        
        


        

scoreboard=Scoreboard()  
