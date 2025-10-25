print("Welcome to Rock, Paper, Scissors game !!")

import random 

emojis = {"r": "🪨", "s": "✂️", "p": "📃"}
options = ["r", "p", "s"]

def get_player_choice():
  while True:
    player_choice = input("Rock, Paper, Scissors (r/p/s)").lower()
    if player_choice not in options:
      print("Invalid choice")
      continue
    else:
      return player_choice
      
def display_choices(player_choice, computer_choice):
  print (f"You chose {emojis[player_choice]}")
  print (f"Computer chose {emojis[computer_choice]}")
  
def check_winner(player_choice, computer_choice):
  if player_choice == computer_choice:
      print ("It's a tie!")
  elif (
      (player_choice == "r" and computer_choice == "s") or 
      (player_choice == "s" and computer_choice == "p") or 
      (player_choice == "p" and computer_choice == "r")):
      print ("You win!")
  else:
      print ("You lose")

def play_game():
  while True:
    player_choice = get_player_choice()
    
    computer_choice = random.choice(options)

    display_choices(player_choice,  computer_choice)
    
    check_winner(player_choice, computer_choice)
    
    should_contine = input("Continue? (y/n)").lower()
    if should_contine == "n":
      print ("Thanks for playing")
      break 
    
play_game()


