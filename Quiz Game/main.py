from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data : 
    qtext = question['question']
    qanswer = question['correct_answer']
    Q = Question(qtext,qanswer)
    question_bank.append(Q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions() : 
    quiz.next_question()
    
print("Congrats. You finished the quiz.")
print(f"Your total score is {quiz.score}/{quiz.question_number}")
    
