import json 

filename = "to_do_list.json"

def load_tasks():
  try:
    with open (filename, "r") as file:
      return json.load(file)
  except:
    return{"tasks": []}

def save_tasks(tasks):
  try:
    with open (filename, "w") as file:
      json.dump(tasks, file, indent=4)
  except:
    print("Failed to save")
    print()

def view_tasks(tasks):
  tasks_list = tasks["tasks"]
  if len(tasks_list) == 0:
    print("No tasks to display")
    return
  else:
    print("Your To-Do List")
    for idx, task in enumerate(tasks_list):
      status = "[Completed]" if task["Complete"] else "[Pending]"
      print(f"{idx + 1}. {task['Description']} | {status}")
      print()
    

def create_tasks(tasks):
  description = input("Enter tasks description ").strip()
  if description:
    tasks["tasks"].append({"Description": description, "Complete": False})
    save_tasks(tasks)
    print("Tasks added\n")
  else:
    print("Description cannot be empty")
    
    

def mark_tasks_complete(tasks):
  view_tasks(tasks)
  if len(tasks["tasks"]) == 0:
    return
  try:
    task_number = int(input("Enter number to the task to mark complete "))
    if 1 <= task_number <= len(tasks["tasks"]):
      tasks["tasks"][task_number - 1]["Complete"] = True
      save_tasks(tasks)
      print("Task marked complete\n")
    else:
      ("Invalid task number\n")
  except ValueError:
    print("Please enter a valid number\n")

def delete_tasks(tasks):
  view_tasks(tasks)
  if len(tasks["tasks"]) == 0:
    return
  try:
    task_number = int(input("Enter number of the task you want to delete "))
    if 1 <= task_number <= len(tasks["tasks"]):
      delete = tasks["tasks"].pop(task_number - 1)
      save_tasks(tasks)
      print(f"Deleted task: {delete['Description']}\n")
    else:
      print("Invalid task number\n")
  except ValueError:
    print("Enter a valid number\n")
  

def main():
  tasks = load_tasks()
  while True: 
    print("To-Do List Manager ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Tasks")
    print("4. Delete Tasks")
    print("5. Exit")
  
    choice = input("Enter a choice\n")
  
    if choice == "1":
      create_tasks(tasks)
    elif choice == "2":
      view_tasks(tasks)
    elif choice == "3":
      mark_tasks_complete(tasks)
    elif choice == "4":
      delete_tasks(tasks)
    elif choice == "5":
      print("Goodbye. Make sure you complete your Tasks")
      break
    else:
      print("Invalid number. Please enter a valid number ")
      
main()
