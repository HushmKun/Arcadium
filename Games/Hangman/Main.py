from random import choice 
from .ART import *
from os import system

on = True
while on :

    system("cls || clear")
    print(logo)
    
    display = [] 
    lives = 6 
    chosen_word = choice(word_list)
        
    for i in range(len(chosen_word)):
        display.append("-")

    print(art[lives])
    print(display)

    while  (lives > 0) and ("-" in display) :
        guess = input("Guess a letter : ").lower()
    
        if guess in chosen_word :    
            for position in range (len(chosen_word)) :
                if guess == chosen_word[position] :
                    display[position] = guess
        else : 
            lives -= 1
        

        print(art[lives])
        print(display)

    if (lives > 0 ) :
        print("You Win.")
    else : 
        print(f"You Lose, Word was '{chosen_word}'")

    if (input("Do you want to continue ?! (y/n) ").lower() == 'y') :
        continue
    else : 
        on = False    
