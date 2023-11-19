#Practice Problems

#1.

def devide(x, y):
  try:
    result = x / y
    print(result)
  except ZeroDivisionError:
    print('You cannot devide by 0!');

print(devide(4, 0));

#2.
def devideUsersNumbers():
  user_number_1 = int(input('Please input your first number: '))
  user_number_2 = int(input('Please input your second number: '))
  return devide(user_number_1, user_number_2)

devideUsersNumbers()