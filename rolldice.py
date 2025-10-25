print("Welcome to Dice Rolling Game")

import random 

while True:
  
  user_input = input("Roll the dice? (y/n)").lower()
  
  if user_input == "y":
    try:
      user_input2 = (int(input("How many dice do you want to roll (1 - 5)?")))
    
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      die3 = random.randint(1, 6)
      die4 = random.randint(1, 6)
      die5 = random.randint(1, 6)
  
      if user_input2 == 1:
        print(die1)
      
      elif user_input2 == 2:
        print(die1 , die2)
      
      elif user_input2 == 3:
        print(f"{die1}, {die2}, {die3}")
      
      elif user_input2 == 4:
        print(f"{die1}, {die2}, {die3}, {die4}")
      
      elif user_input2 == 5:
        print(f"{die1}, {die2}, {die3}, {die4}, {die5}")
      
      else:
        print("Dices only from 1 - 5")
        
    except ValueError:
      print("Invalid input! Enter number from 1 - 5 ")
        
        
  elif user_input == "n":
    print("Thanks for playing")
    break
  else:
    print ("Invalid choice")
