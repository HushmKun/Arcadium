import random 
import ART
import words
import pickle 

print(ART.logo)

word_list = words.word_list
display = [] #Empty
lives = 6 
index = 0
#random choice 
chosen_word = random.choice(word_list)


    
#create list filled with "-" based on letters count
for i in range(len(chosen_word)):
    display.append("-")

#print(lives)
print(ART.art[lives])
print(display)

#("-" in display) or
while  (lives > 0) and ("-" in display) :
    #input the guess
    guess = input("Guess a letter : ").lower()


    #check the guess
    
    if guess in chosen_word :    
        #letter = chosen_word[position]
        for position in range (len(chosen_word)) :
            if guess == chosen_word[position] :
                display[position] = guess
    else : 
        lives -= 1
    
        
    #print(f"Lives = {lives}")
    print(ART.art[lives])
    print(display)

if (lives > 0 ) :
    print("You Win.")
    print("Game Over.")
else : 
     print("You Lose.")
     print("Game Over.")

input()
