class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (2*self.width) + (2*self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2)** 0.5
        return diagonal

    def get_picture(self):
        if (self.width>50 or self.height>50):
            return "Too big for picture."
        pic_string = (('*' * self.width)+ '\n') * self.height
        return pic_string

    def get_amount_inside(self, shape):
        amount_fit = int(self.get_area()/ shape.get_area())
        return amount_fit


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def __str__(self) -> str:
        return f"Square(side={self.width})"
    
    def set_side(self, side):
        self.width = side
        self.height = side

