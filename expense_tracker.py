from enum import Enum

def main_menu():
	while True:
		print('\n=== Expense Tracker ===')
		print('\n Please pick an option from the list below:')
		print('1. Add an expense')
		print('2. List all expenses')
		print('3. Edit an expense')
		print('6. Exit')
		choice = input('Enter a corrisponding number, to make a choice: ')
		
		if choice == '1':
			add_expense()
		elif choice == '2':
			list_all_expenses()
		elif choice == '6':
			break
		else:
			print('Invalid choice. Please try again')

def add_expense():
	global expenses
	amount = input('Enter the amount of the expense: ')
	print('Please pick a category from the list below: ')
	print('1. Food')
	print('2. Entertainment')
	print('3. Transportation')
	print('4. Utilities')
	category = input('Enter the category of the expense: ')
	if category == '1':
		category = Category.FOOD
	elif category == '2':
		category = Category.ENTERTAINMENT
	elif category == '3':
		category = Category.TRANSPORTATION
	elif category == '4':
		category = Category.UTILITIES        
	else:
		print('Please choose a number between 1 and 4')
	description = input('Enter a description of the expense: ')
	date = input('Enter the date of the expense: ')
	new_expense = Expense(amount, category, description, date)
	expenses.append(new_expense)
def list_all_expenses():
	for expense in expenses:
		print('------------------')
		print('Expense Details:')
		print('------------------')
		print(f'ID: {expense.id}')
		print(f'Amount: {expense.amount}')
		print(f'Category: {expense.category.value}')
		print(f'Description: {expense.description}')
		print(f'Date: {expense.date}')
		print('------------------')

expenses = []

if __name__ == '__main__':
	main_menu()

def edit_expense():
	expense_id = input('Enter the ID of the expense you would like to modify: ')
	new_amount = input('Enter the new amount of the expense: ')
	expense_to_modify
	for expense in expenses:
		if expense.id == expense_id:
			expense_to_modify = expense
	expense_to_modify.amount = new_amount
	index_of_expense = expenses.index(expense_to_modify)
	expenses[index_of_expense] = expense_to_modify

class Expense:
	def __init__(self, amount, category, description, date):
		self.id = expenses.__len__() + 1
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