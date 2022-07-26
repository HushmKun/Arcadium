from .RPSextras import *
from os import system
from random import randint
import inquirer as inq


def rps() -> None:
    repeat = True
    system('clear || cls')
    while repeat :
        questions = [
    inq.List('choice',
                    message="Choose ",
                    choices=[('Rock',0 ),('Paper',1),('Scissors',2)],
                ),
    ]
        player = inq.prompt(questions)['choice']

        match player: 
            case 0:
                print(ROCK)
            case 1:
                print(PAPER)
            case 2:
                print(SCISSORS)
    

        print("Computer Chose :")
        pc = randint(0,2)
        match pc : 
            case 0:
                print(ROCK)
            case 1:
                print(PAPER)
            case 2:
                print(SCISSORS)

        
        if (player+1) % 3 == pc :
            print("Computer Wins.")
        elif player == pc : 
            print("A Draw.")
        else:
            print("Player Wins.") 

        x = input("Do you want to continue ? (y,n) ").lower()
        if x == 'n' : 
            repeat = False
        else : 
            system('clear || cls ') 

if __name__ == '__main__':
    rps()