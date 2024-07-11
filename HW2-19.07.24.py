import math

class Figure:
    def __init__(self):
        pass

    def area(self):
        pass

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f"Фигура: {type(self).__name__}, Площадь: {self.area()}"

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Прямоугольник, ширина: {self.width}, высота: {self.height}, Площадь: {self.area()}"

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Круг, радиус: {self.radius}, Площадь: {self.area()}"

class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Прямоугольный треугольник, основание: {self.base}, высота: {self.height}, Площадь: {self.area()}"

class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def __str__(self):
        return f"Трапеция, основание 1: {self.base1}, основание 2: {self.base2}, высота: {self.height}, Площадь: {self.area()}"


rectangle = Rectangle(5, 10)
print(rectangle)
print(int(rectangle))

circle = Circle(7)
print(circle)
print(int(circle))

triangle = RightTriangle(6, 8)
print(triangle)
print(int(triangle))

trapezoid = Trapezoid(4, 8, 6)
print(trapezoid)
print(int(trapezoid))
