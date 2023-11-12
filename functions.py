# Practice Problems

# 1.
def add(x, y):
  return x + y

print(add(1, 2))

# 2.
def is_even(number):
  if(number % 2 == 0):
    return True
  return False

print(is_even(4))

# 3.
def largest(num1, num2, num3):
  return max(num1, num2, num3)

print(largest(1, 2, 3))

# 4.
def print_list(list):
  for item in list:
    print(item)
  
print_list(["apple", "bannana", "orange"])