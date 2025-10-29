print ("Welcome to Random Password Generator")

import string 
import random 

def generate_password():

  while True:
    try:
      length = int(input("Enter the desired length of the password  "))
      if length < 6:
        print("Password length should be greater than 6 for better security")
        continue
      break 
    except ValueError:
      print ("Enter a valid number")
      
  
  include_uppercase = input("Should contain uppercase? (y/n)  ").lower().strip()
  include_special = input("Should contain special characters? (y/n)  ").lower().strip()
  include_digits = input("Should contain digits? (y/n)  ").lower().strip()
  
  lowercase = string.ascii_lowercase 
  uppercase = string.ascii_uppercase if include_uppercase == "y" else ""
  special = string.punctuation if include_special == "y" else ""
  digits = string.digits if include_digits == "y" else ""
  all_characters = lowercase + uppercase + special + digits 
  
  required_characters = []
  if include_uppercase == "y": required_characters.append(random.choice(uppercase))
  if include_special == "y":
    required_characters.append(random.choice(special)) 
  if include_digits == "y":
    required_characters.append(random.choice(digits))
    
  remaining_characters = length - len(required_characters)
  password = required_characters
    
  for _ in range(remaining_characters):
    characters = random.choice(all_characters)
    password.append(characters)
  
  random.shuffle(password)
  
  str_password = "".join(password)
  return str_password
      
  
password = generate_password()
print (password)
