import random 

computer_choice = random.randint(1, 50)

while True:
	player_choice = int(input("Guess the number from 1 - 50 \n>"))
	if player_choice > computer_choice:
		print("Too high ")
	elif player_choice < computer_choice:
		print("Too low ")
	elif player_choice == computer_choice:
		print("Congratulations!!!\n You've guessed the number")
		break
	else:
			print("Invalid choice ")
