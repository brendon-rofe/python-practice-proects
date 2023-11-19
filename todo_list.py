tasks = []

def main_menu():
  while True:
    print('\n=== Todo List ===')
    print('1. Create task')
    print('5. Exit')

    choice = input('Enter a corrisponding number, to make a choice: ')

    if choice == '1':
      create_task()
    elif choice == '5':
      break
    else:
      print('Invalid choice. Please try again')

def create_task():
  task = input('Please type in your task: ')
  tasks.append(task)

print(tasks)

if __name__ == '__main__':
  main_menu()