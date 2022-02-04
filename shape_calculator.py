# Polygon Area Calculator -- Scientific Computing with Python Project #4

## Rectangle class
class Rectangle:

    # Functions
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        n = self.height
        picture = ""
        while n > 0:
            line = self.width * "*"
            picture += line + "\n"
            n -= 1
        return picture

    def get_amount_inside(self, shape):
        selfarea = self.get_area()
        shapearea = shape.get_area()
        amountinside = int(selfarea / shapearea)
        return amountinside

    def __str__(self):
        rstr = f"Rectangle(width={self.width}, height={self.height})"
        return rstr

## Square class
class Square(Rectangle):

    # Functions
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        sstr = f"Square(side={self.width})"
        return sstr

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height
