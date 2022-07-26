from random import randint
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=500, height=500)
screen.tracer(0)

# Player
player = Player()

# cars
car = CarManager()

# Score
score = Scoreboard()
score.updatescore()

# Key-binding
screen.listen()
screen.onkey(player.up , "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car.create_car()
    car.move()

    for cars in car.cars:
        if player.distance(cars) < 20:
            game_is_on = False
            score.game_over()

    if player.levelup() :
        score.level += 1 
        score.updatescore()
        player.restart()
        car.speedup()


screen.exitonclick()