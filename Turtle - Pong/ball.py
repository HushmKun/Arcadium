from turtle import Turtle


class ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.xmove = 10
        self.ymove = 10

    def move(self):
        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto((newx,newy))

    def resetme(self): 
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
    def rebound(self):
        self.ymove *= -1

    def bounce(self):
        self.xmove *= -1