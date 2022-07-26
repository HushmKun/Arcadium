import requests 
from html import unescape

question_data =[  
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "hard",
      "question": "Japan was part of the Allied Powers during World War I.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The Republic of Malta is the smallest microstate worldwide.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Entertainment: Video Games",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Donkey Kong was originally set to be a Popeye arcade game.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Entertainment: Television",
      "type": "boolean",
      "difficulty": "medium",
      "question": "The television show Doctor Who first aired in 1963.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Entertainment: Japanese Anime & Manga",
      "type": "boolean",
      "difficulty": "medium",
      "question": "The anime Attack on Titan was directed by Tetsurō Araki, the same person who directed the anime Highschool of the Dead.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Science: Computers",
      "type": "boolean",
      "difficulty": "easy",
      "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Entertainment: Music",
      "type": "boolean",
      "difficulty": "medium",
      "question": "&quot;The Division Bell&quot; is the final album of the progressive rock band Pink Floyd.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "hard",
      "question": "Switzerland has four national languages, English being one of them.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Entertainment: Video Games",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Mortal Kombat was almost based on Jean-Claude Van Damme movie.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Entertainment: Television",
      "type": "boolean",
      "difficulty": "easy",
      "question": "&quot;The Simpsons&quot; family is named after creator Matt Groening&#039;s real family.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    }
  ]
class Question : 
    
    def __init__ (self , q_text , q_answer)  -> None: 
        self.text = q_text
        self.answer = q_answer
        
class QuizBrain:

    def __init__ (self)  -> None:
        self.question_number = 0 
        self.score = 0 
        try : 
            parameters = {
                "amount": 10,
                "type": "boolean"
            }
            response = requests.get(url="https://opentdb.com/api.php", params=parameters)
            question_data = response.json()["results"]
            self.question_list = [Question(unescape(question['question']),question['correct_answer']) for question in question_data ]
        except :
            self.question_list = [Question(question['question'],question['correct_answer']) for question in question_data ]

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)


    def next_question(self) -> None:
        current = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number }: {current.text} ? (True/False):  ")
        self.check_answer(ans , current.answer )

    def check_answer(self , answer , correct_answer)  -> None:
        if answer.lower().strip() == correct_answer.lower() :
            self.score += 1
            print("Correct !" , end="")
        else :
            self.score = self.score
            print("Sorry, It's wrong.", end="")
        print(f"Your current score is {self.score}/{self.question_number}\n")    
        


     