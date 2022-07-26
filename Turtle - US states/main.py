import turtle as t
import pandas

screen = t.Screen()
screen.setup(1.0,1.0,0,0)
image ="states.gif"
screen.addshape(image)
tt = t.Turtle(shape=image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list() 
guessed_list = []

while len(guessed_list) < 50 : 

    answer_text = screen.textinput(title=f"{len(guessed_list)}/50 States correct.",prompt="What's another state name ?!").title()
    if answer_text == 'Exit':
        break
    elif answer_text in all_states :
        guessed_list.append(answer_text)
        tur = t.Turtle()
        tur.hideturtle()
        tur.penup()
        state_name = data[data["state"] == answer_text]
        tur.goto(int(state_name.x) , int(state_name.y) )
        tur.write(answer_text)
    

states_not_guessed = [n for n in all_states if n not in guessed_list]


saved = pandas.DataFrame(states_not_guessed)
saved.to_csv('states_to_learn.csv')
screen.exitonclick()