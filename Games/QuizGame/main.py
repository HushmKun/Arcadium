from .quiz_brain import QuizBrain
from os import system 

def game() -> None:
    on = True
    while on : 
        system("clear || cls ")
        quiz = QuizBrain()
        while quiz.still_has_questions() : 
            quiz.next_question()
            
        print("Congrats. You finished the quiz.")
        print(f"Your total score is {quiz.score}/{quiz.question_number}\n\n")

        if (input("Do you want to continue ?! (y/n) ").lower() == 'y') :
            continue
        else : 
            on = False    
