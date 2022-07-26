from .data import *
from random import randint
from os import system

def clear():
    system("clear")


def game():
    rand = randint(0,len(data)-1)
    clear()
    print(logo)
    print("\t Instagram Followers Edition ")
    print(f"Compare A: {data[rand]['name']}, a {data[rand]['description']}, from {data[rand]['country']}. ")
    f1 = data[rand]['follower_count']
    print(vs)

    
    score = 0
    while True :
        rand2 = randint(0,len(data)-1)
        print(f"Compare B: {data[rand2]['name']}, a {data[rand2]['description']}, from {data[rand2]['country']}. ")
        f2 = data[rand2]['follower_count']
        while rand == rand2 :
            rand2 = randint(0,len(data)-1)
            
        #input choice
        choice = input("Choose 'A' or 'B' : ").upper()

        #compare
        if choice =='A' :
            if f1>f2:
                score += 1
                rand = rand
                f1 = f1
            else : 
                print("You Lose.")
                print(f"Your score = {score} , Press Any Key to exit.")
                input()
                break

        else :
            if f1<f2:
                score += 1
                f1 = f2
                rand = rand2
            else : 
                print("You Lose.")
                print(f"Your score = {score} , Press Any Key to exit.")
                break
        clear()
        print(logo)
        print(f"Correct! Your score = {score}")
        print(f"Compare A: {data[rand]['name']}, a {data[rand]['description']}, from {data[rand]['country']}.")
        print(vs)

    
if __name__ == '__main__':
    game()