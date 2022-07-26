import Games.RPS.RPS as RPS
import Games.HighLow.HiLo as HiLo
on = True
while on :
	
	RPS.system("clear")
	questions = [
	RPS.inq.List('Games',
					message="Games ",
					choices=['Rock-Paper-Scissor','High-Low','Exit'],
				),
	]

	answers = RPS.inq.prompt(questions)

	match answers['Games'] :
		case 'Rock-Paper-Scissor':
			RPS.rps()
		case 'High-Low':
			HiLo.game()
		case "Exit":
			on = False 

print("Good Bye.")
	

