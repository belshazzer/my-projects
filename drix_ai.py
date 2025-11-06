import time 
import random 

print("Hello I'm Drix, your personal chatbot")
name = input("What's your name?")
print(f"Welcome, {name}. Nice to meet you\n Type 'help' to see what i can do for you")

while True:
  command = input(f"{name}:  ").lower().strip()
  
  match command: 
    case "hello" | "hi" | "hey" | "what's up" :
      responses = [f"Hey {name}" , f"Hello {name}, How are you doing today?" , f"Yo {name}!, ready to chat?" , f"Hey there"]
      print("Drix:" , random.choice(responses))
      
    case "time" | "what's the time" | "current time" :
      print ("Drix: " , time.strftime ("It's %I:%M %p on %A, %d %B %Y"))
    case "weather" | "how's the weather":
      responses2 = ["It's a lovely day outside - perfect for learning python" , "Its another great day to learn python"]
      print("Drix: " , random.choice(responses2))
    
    case "help" | "menu" | "commands" :
      print ("Drix: \nhello, hi,  hey,  what's up \n time,  what's the time \n weather,  how's the weather\n joke,  tell me a joke\n help,  menu,  commands\n exit,  quit")
      

    case "joke" | "tell me a joke" :
      jokes = ["😂 Why did the programmer quit his job? Because he didn’t get arrays!", "🤣 I would tell you a UDP joke, but you might not get it." , "💻 There are only 10 kinds of people in the world: those who understand binary and those who don’t." , "🐍 Why do Python programmers prefer snakes? Because they don’t need braces!"] 
      print("Drix: " , random.choice(jokes))
        
    case "exit" | "quit" :
      print (f"Drix: Goodbye {name}  Have a great day")
      break 
      
    case _:
      print(f"Drix: Sorry {name} I did'nt understand that. Try 'help'" )
      
