from turtle import Turtle
from random import *
class Food (Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.7,0.7)
        self.speed(0)
        self.refresh()

    def refresh(self):
        randx= randint(-230,230)
        randy= randint(-230,230)
        self.goto( randx , randy )