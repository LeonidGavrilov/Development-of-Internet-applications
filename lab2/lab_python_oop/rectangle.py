from lab_python_oop.colour import Colour
from lab_python_oop.shape import Shape


class Rectangle(Shape):
    SHAPE_NAME = "Прямоугольник"

    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        self.colour = Colour()
        self.colour.colour = colour

    def __repr__(self):
        return "{}. Цвет: {}. Стороны: {} и {}. Площадь: {}.".format(
            Rectangle.get_shape_name(), self.colour, self.width, self.height, self.area())

    def area(self):
        return self.width * self.height

    @classmethod
    def get_shape_name(cls):
        return cls.SHAPE_NAME
