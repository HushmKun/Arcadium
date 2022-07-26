import Games.RPS.RPS as RPS
import Games.HighLow.HiLo as HiLo
import Games.Hangman.Main as Hangman
import Games.QuizGame.main as Quiz

on = True
while on :
	
	RPS.system("clear || cls")
	print("""

\t █████╗ ██████╗  ██████╗ █████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗
\t██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██║   ██║████╗ ████║
\t███████║██████╔╝██║     ███████║██║  ██║██║██║   ██║██╔████╔██║
\t██╔══██║██╔══██╗██║     ██╔══██║██║  ██║██║██║   ██║██║╚██╔╝██║
\t██║  ██║██║  ██║╚██████╗██║  ██║██████╔╝██║╚██████╔╝██║ ╚═╝ ██║
\t╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝
                                                               
""")
	questions = [
	RPS.inq.List('Games',
					message="Games ",
					choices=['Rock-Paper-Scissor','High-Low','Hangman','Quiz Game','Exit'],
				),
	]

	answers = RPS.inq.prompt(questions)

	match answers['Games'] :
		case 'Rock-Paper-Scissor':
			RPS.rps()
		case 'High-Low':
			HiLo.game()
		case 'Hangman':
			Hangman.game()
		case 'Quiz Game':
			Quiz.game()
		case "Exit":
			on = False 

print("ಥ_ಥ Sad to see you go. Bye.")
	

