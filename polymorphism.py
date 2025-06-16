import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 7)
]

for shape in shapes:
    print(f"{type(shape).__name__} area: {shape.area():.2f}")
