from turtle import Turtle

class Paddles (Turtle):

    def __init__(self, x,y ) -> None:
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.turtlesize(stretch_wid= 1,stretch_len= 5)
        self.goto(x,y)
        self.setheading(90)
        self.score = 0 

    def up(self):
        self.fd(40)
    
    def down(self):
        self.bk(40)

    