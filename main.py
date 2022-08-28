from os import system
import sys
from inquirer import prompt , List as Listy


on = True
while on :
	
	system("clear || cls")
	print("""
\t █████╗ ██████╗  ██████╗ █████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗
\t██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██║   ██║████╗ ████║
\t███████║██████╔╝██║     ███████║██║  ██║██║██║   ██║██╔████╔██║
\t██╔══██║██╔══██╗██║     ██╔══██║██║  ██║██║██║   ██║██║╚██╔╝██║
\t██║  ██║██║  ██║╚██████╗██║  ██║██████╔╝██║╚██████╔╝██║ ╚═╝ ██║
\t╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝
                                                               
""")
	questions = [
	Listy('Games',
					message="Games ",
					choices=['Snake','Rock-Paper-Scissor','High-Low','Hangman','Quiz Game','Exit'],
				),
	]

	answers = prompt(questions)

	match answers['Games'] :
		case 'Snake':
			import Games.Snake.main
			del sys.modules['Games.Snake.main']
			del Games.Snake.main
		case 'Rock-Paper-Scissor':
			import Games.RPS.RPS
			del sys.modules['Games.RPS.RPS']
			del Games.RPS.RPS 
		case 'High-Low':
			import Games.HighLow.HiLo 
			del sys.modules['Games.HighLow.HiLo']
			del Games.HighLow.HiLo
		case 'Hangman':
			import Games.Hangman.Main 
			del sys.modules['Games.Hangman.Main']
			del Games.Hangman.Main
		case 'Quiz Game':
			import Games.QuizGame.main
			del sys.modules['Games.QuizGame.main']
			del Games.QuizGame.main 
		case "Exit":
			on = False 
	
print("ಥ_ಥ Sad to see you go. Bye.")
	

