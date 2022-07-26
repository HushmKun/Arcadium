import turtle as t 
from random import *

is_race_on = False

t.colormode(255)
screen = t.Screen()
screen.setup(500,400)
user_input = screen.textinput("Bets","Which one will you bet on ?")

tim = t.Turtle(shape="turtle")
tom = t.Turtle(shape="turtle")
tem = t.Turtle(shape="turtle")
tam = t.Turtle(shape="turtle")
tum = t.Turtle(shape="turtle")

T_list = [tim,tom,tem,tam,tum]
C_list = ["red","blue","green","black","yellow"]

cor = -100
if user_input:
    is_race_on = True

for ____ in T_list:
    ____.penup()
    cchoice = choice(C_list)
    ____.color(cchoice)
    C_list.remove(cchoice)
    ____.goto(x= -230 , y= cor)
    cor += 50

while is_race_on :
    for T in T_list:
        if T.xcor() > 230:
            is_race_on = False
            winning_color = T.pencolor()
            if winning_color == user_input:
                print(f"You win! The {winning_color} turtle wins.")
            else :
                print(f"You lose! The {winning_color} turtle wins.")


screen.exitonclick()