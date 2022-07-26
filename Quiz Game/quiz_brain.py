class QuizBrain:

    def __init__ (self , qlist) :
        self.question_number = 0 
        self.score = 0 
        self.question_list = qlist

    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number }: {current.text} ? (True/False):  ")
        self.check_answer(ans , current.answer )

    def check_answer(self , answer , correct_answer) :
        if answer.lower() == correct_answer.lower() :
            self.score += 1
            print("Correct !")
        else :
            self.score = self.score
            print("Sorry, It's wrong.")
        print(f"Your current score is {self.score}/{self.question_number}")    
        print("\n")


     