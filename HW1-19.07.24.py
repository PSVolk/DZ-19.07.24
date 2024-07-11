import math

class Figure:
    def __init__(self):
        pass

    def area(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height


rectangle = Rectangle(5, 10)
print("Площадь прямоугольника:", rectangle.area())

circle = Circle(7)
print("Площадь круга:", circle.area())

triangle = RightTriangle(6, 8)
print("Площадь прямоугольного треугольника:", triangle.area())

trapezoid = Trapezoid(4, 8, 6)
print("Площадь трапеции:", trapezoid.area())
