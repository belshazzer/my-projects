print("Welcome to Python Trivia Game")

import random

python_questions = {
    "What is Python's main data structure?": "Dictionary",
    "What is the keyword for defining a function?": "Def",
    "What is the data type for true/false values?": "Boolean",
    "What is the operator for exponentiation?": "**",
    "What is the method for adding an item to a list?": "Append",
    "What is the data type for a sequence of characters?": "String",
    "What is the keyword for importing a module?": "Import",
    "What is the data type for a collection of unique items?": "Set",
    "What is the operator for integer division?": "//",
    "What is the method for removing an item from a list?": "Pop",
    "What is the data type for a collection of key-value pairs?": "Dictionary",
    "What is the keyword for creating a class?": "Class",
    "What is the data type for a sequence of items?": "List",
    "What is the operator for modulus?": "%",
    "What is the method for sorting a list?": "Sort"
}

def play_game():
  while True:
    asked_questions = list(python_questions.keys())
    total_questions = 8
    score = 0 

    selected_questions = random.sample(asked_questions, total_questions)

    for idx, python_question in enumerate(selected_questions):
      print(f"{idx + 1}. {python_question}")
      user_answer = input("Answer ").lower().strip()
  
      correct_answer = python_questions[python_question]
  
      if user_answer == correct_answer.lower():
        print("Correct ")
        score += 1
      else:
        print (f"Oops Wrong. The answer is {correct_answer}")
    
    print(f"Game over. You scored {score}/{total_questions}")
  
    should_continue = input("Do you want to play again?  (y/n)").lower()
    if should_continue == "n":
      break 
    
play_game()
  
