def main_menu():
  while True:
    print('\n=== Todo List ===')
    print('1. Create task')
    print('2. List all tasks')
    print('3. Update task by index')
    print('5. Exit')

    choice = input('Enter a corrisponding number, to make a choice: ')

    if choice == '1':
      create_task()
    elif choice == '2':
      list_tasks()
    elif choice == '3':
      update_task_by_index()
    elif choice == '5':
      break
    else:
      print('Invalid choice. Please try again')

def create_task():
  task = input('Please type in your task: ')
  tasks.append(task)

def list_tasks():
  print(tasks)

def update_task_by_index():
  index = int(input('Task at which index?: '))
  updatedTask = input('Update to apply: ')
  tasks[index] = updatedTask
  print(f'task at index {index} updated.')

tasks = []

if __name__ == '__main__':
  main_menu()