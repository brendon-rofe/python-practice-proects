def display_menu():
  print("\nTo-Do List")
  print("------------")
  print("1. View tasks")
  print("2. Add task")
  print("3. Remove task")
  print("4. Exit")

  choice = input("Choose an option: ")
  return choice

tasks = []

def add_task():
  task = input("Enter the task you want to add: ")

  tasks.append(task)
  print(f"Task '{task}' added!")

if __name__ == "__main__":
  while True:
    user_choice = display_menu()

    if user_choice == "1":
      print(tasks)
    elif user_choice == "2":
      add_task()
    elif user_choice == "3":
      pass
    elif user_choice == "4":
      print("Exiting...")
      break
    else:
      print("Invalid option, please choose a number between 1 and 4.")