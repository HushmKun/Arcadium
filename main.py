import Games.RPS.RPS as RPS
import Games.HighLow.HiLo as HiLo
import Games.Hangman.Main as Hangman

on = True
while on :
	
	RPS.system("clear")
	questions = [
	RPS.inq.List('Games',
					message="Games ",
					choices=['Rock-Paper-Scissor','High-Low','Hangman','Exit'],
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
		case "Exit":
			on = False 

print("Good Bye.")
	

