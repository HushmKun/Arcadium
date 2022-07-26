import turtle as t 
X = 0
Y = 228
class ScoreBoard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0 
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.goto(X,Y)
        self.write(f"Score = {self.score}",
        align="center",font=("courier",15,"normal"))


    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",
        align="center",font=("courier",35,"normal"))
        self.goto(0,-40)
        self.write(f"Your Score is {self.score}",
        align="center",font=("courier",20,"normal"))
    