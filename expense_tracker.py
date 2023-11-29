def main_menu():
    while True:
        print('\n=== Expense Tracker ===')
        print('\n Please pick an option from the list below:')
        print('1. Add an expense')
        print('6. Exit')
        choice = input('Enter a corrisponding number, to make a choice: ')
        
        if choice == '1':
            print('This will be impelmented later')
        elif choice == '6':
            break
        else:
            print('Invalid choice. Please try again')


if __name__ == '__main__':
    main_menu()