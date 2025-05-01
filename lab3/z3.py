from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c, height):
        self.a = a
        self.b = b
        self.c = c
        self.height = height

    def area(self):
        return 0.5 * self.a * self.height
    def perimeter(self):
        return self.a + self.b + self.c


def print_shape_info(shape):
    print(f"Тип фигуры: {type(shape).__name__}")
    print(f"Площадь: {shape.area():.2f}")
    print(f"Периметр: {shape.perimeter():.2f}")
    print()


shapes = [
    Rectangle(4, 5),
    Circle(5),
    Triangle(3, 4, 5, 4)
]

for shape in shapes:
    print_shape_info(shape)


