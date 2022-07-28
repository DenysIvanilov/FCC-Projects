class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

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
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self):
        if self.height >= 50: return "Too big for picture."
        if self.width >= 50: return "Too big for picture."
        picture = ""
        lines = 1
        while lines <= self.height:
            picture += "*" * self.width + "\n"
            lines += 1
        return picture

    def get_amount_inside(self, shape):
        area = self.get_area()
        shape_area = shape.get_area()
        amount = area // shape_area
        return amount


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def __repr__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.set_height(side)
        self.set_width(side)

