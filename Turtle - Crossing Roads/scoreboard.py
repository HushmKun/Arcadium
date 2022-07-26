from turtle import Turtle 

FONT = ("Courier", 20, "normal")
FONT2 = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-240,220)
        self.pencolor("black")
        self.level = 1 

    def updatescore(self):
        self.clear()
        self.write(arg= f"Level : {self.level}", font= FONT)
    
    def game_over(self):
        self.goto(-60,0)
        self.write(arg= "Game Over", font= FONT2)
