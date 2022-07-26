import turtle as t
from snake import Snake
import time
from food import Food
from score import ScoreBoard


game_on = True

screen = t.Screen()
screen.setup(500,500)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
board = ScoreBoard()

screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")
screen.update()

while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    #detect food and add score
    if snake.head.distance(food) < 15 :
        food.refresh()
        board.score += 1
        board.clear()
        board.write(f"Score = {board.score}",
        align="center",font=("courier",15,"normal"))
        snake.add_seg()
    
    #End game when hit a wall
    if  snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240 :
        game_on = False
        board.clear()
        board.game_over()

    #Detect Tail
    for seg in snake.snake_body[1:] :
        if snake.head.distance(seg) < 15 :
            game_on = False
            board.clear()
            board.game_over()

screen.exitonclick()