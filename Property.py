class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    @property
    def width(self):
        pass

    @property
    def height(self):
        pass

rectangle = Rectangle(3,5)

print(rectangle._width)
print(rectangle._height)