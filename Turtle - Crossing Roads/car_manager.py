from turtle import Turtle
import random as rand

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
        def __init__(self) -> None:
            super().__init__()
            self.cars = []
            self.speed = STARTING_MOVE_DISTANCE
            self.x = 6

        def create_car(self):
            chance = rand.randint(1,self.x)
            if chance == 1 :
                new_car = Turtle()
                new_car.penup()
                new_car.shape('square')
                new_car.color(rand.choice(COLORS))
                new_car.shapesize(stretch_wid=1,stretch_len=2)
                new_car.goto(320,rand.randint(-200,200))
                self.cars.append(new_car)

        def move(self):
            for car in self.cars : 
                car.bk(self.speed)

        def speedup(self):
            self.speed += MOVE_INCREMENT 
            if self.x > 2:
                self.x -= 1 

        
