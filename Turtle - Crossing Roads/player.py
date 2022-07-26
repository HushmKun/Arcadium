from turtle import Turtle 

STARTING_POSITION = (0, -230)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 230


class Player(Turtle):
    
    def __init__ (self) -> None :
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        self.fd(MOVE_DISTANCE)

    def levelup(self):
        if self.ycor() > FINISH_LINE_Y :
            return True
        else :
            return False

    def restart(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()
