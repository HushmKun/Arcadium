from os import system
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
		case 'Rock-Paper-Scissor':
			import Games.RPS.RPS 
		case 'High-Low':
			import Games.HighLow.HiLo 
		case 'Hangman':
			import Games.Hangman.Main 
		case 'Quiz Game':
			import Games.QuizGame.main 
		case "Exit":
			on = False 

print("ಥ_ಥ Sad to see you go. Bye.")
	

