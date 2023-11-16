# Practice Problems
import math

# 1.
class Shape:
  def __init__(self) -> None:
    pass

  def area(self):
    return 0
  
class Square(Shape):
  def __init__(self, side):
    self.side = side

  def area(self):
    return self.side ** 2
  
class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return math.pi *  (self.radius ** 2)
  
