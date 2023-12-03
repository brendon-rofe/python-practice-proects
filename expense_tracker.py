from enum import Enum

def main_menu():
    while True:
        print('\n=== Expense Tracker ===')
        print('\n Please pick an option from the list below:')
        print('1. Add an expense')
        print('6. Exit')
        choice = input('Enter a corrisponding number, to make a choice: ')
        
        if choice == '1':
            amount = input('Enter the amount of the expense: ')
            category = input('Enter the category of the expense: ')
            description = input('Enter a description of the expense: ')
            date = input('Enter the date of the expense: ')
            add_expense(amount, category, description, date)
        elif choice == '6':
            break
        else:
            print('Invalid choice. Please try again')

def add_expense(amount, category, description, date):
    new_expense = Expense(amount, category, description, date)
    expenses.append(new_expense)

class Expense:
    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

class Category(Enum):
    FOOD = 'food'
    ENTERTAINMENT = 'entertainment'
    TRANSPORTATION = 'transportation'
    UTILITIES = 'utilities'
    CLOTHING = 'clothing'

expenses = []

if __name__ == '__main__':
    main_menu()