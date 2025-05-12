import math

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def area(self):
        return self.width * self.heigth


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


rectangle = Rectangle(5, 11)
circle = Circle(7)

print(f"Площадь прямоугольника: {rectangle.area()}\n"
      f"Площадь круга: {circle.area()}")