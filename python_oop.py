# Practice Problems

# 1.
class Car:
  def __init__(self, make, year):
    self.make = make
    self.year = year
  
  def describe_car(self):
    return f"{self.make} {self.year}"

car = Car("Toyota", 2021)
print(car.make, car.year)

# 2.
print(car.describe_car())

# 3.
class Calculator:
  def __init__(self):
    pass

  def add(self, num1, num2):
    return num1 + num2

calculator = Calculator()

print(calculator.add(1, 2))