import turtle as t 
import Paddles as P
import ball as b
import time

def updateboard(obj):
    obj.clear()
    obj.write(f"{l_paddle.score}     {r_paddle.score}", font=("arial",20,"normal"))

screen = t.Screen()
screen.screensize(900,500)
screen.setup(width=1.0,height=1.0,startx=None , starty=None)
screen.bgcolor('black')
screen.tracer(0)

# Right paddle obj.
r_paddle = P.Paddles( 470 , 0)

# Left paddle obj.
l_paddle = P.Paddles(-490 , 0)

# scoreboard
sb= t.Turtle(visible=False)
sb.goto(-20,255)
sb.pencolor('white')
updateboard(sb)

# ball 
ball = b.ball()

# Moving them 
screen.listen()
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"s")


is_game_on = True

while is_game_on :
    updateboard(sb)
    time.sleep(0.03)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.rebound()
    
    if ball.xcor() > 500 :
        l_paddle.score += 1
        ball.resetme()
        continue

    if ball.xcor() < -510 :
        r_paddle.score += 1
        ball.resetme()
        continue
    
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 460) or (ball.distance(l_paddle) < 50 and ball.xcor() < -470) :
        ball.bounce()
        

screen.exitonclick()