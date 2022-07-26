import turtle as t

DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    """'create()' a snake , 'move()' a snake distance of 20 """
    def __init__(self) -> None:
        self.head = t.Turtle(shape="square")
        snake2 = t.Turtle(shape="square")
        snake3 = t.Turtle(shape="square")
        self.snake_body = [self.head,snake2,snake3]
        x = 0
        for _ in self.snake_body :
            _.color("white")
            _.penup()
            _.goto(x,0)
            x -= 20

    def add_seg(self):
        snake = t.Turtle(shape="square")
        snake.color("black")
        snake.penup()
        snake.speed(0)
        pos = self.snake_body[-1].pos()
        snake.goto(pos)
        snake.color("white")
        self.snake_body.append(snake)        
       
    def move(self):
        for num in range(len(self.snake_body)-1,0,-1) :
            new_pos = self.snake_body[num -1].pos()
            self.snake_body[num].goto(new_pos)
        self.head.forward(DIST)
    
    def up(self):
        if self.head.heading() != DOWN :
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP :
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT :
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT :
            self.head.seth(RIGHT)

