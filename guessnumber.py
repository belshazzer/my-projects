print ("Welcome to Number Guessing Game!")

import random

computer_guess = random.randint(1, 100)
attempts = 6

while attempts > 0:
  try:
    user_guess = int(input(f"Guess the number between 1- 100. You have {attempts} attempts "))
  except ValueError:
    print ("Invalid input enter a number")
    continue

  if user_guess > computer_guess:
    attempts -= 1
    print (f"Too high \nYou have {attempts} attempts left ")
  elif user_guess < computer_guess:
    attempts -= 1 
    print (f"Too low \nYou have {attempts} attempts left ")
  elif user_guess == computer_guess:
    print (f"Congratulations!! You've guessed the number")
    break 
  else:
    print ("Invalid number enter a valid number")
    
if attempts == 0:
  print(f"Oops out of attempts!  The correct number was {computer_guess}")
