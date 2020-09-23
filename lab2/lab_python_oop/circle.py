from math import pi

from lab_python_oop.colour import Colour
from lab_python_oop.shape import Shape


class Circle(Shape):
    SHAPE_NAME = "Круг"

    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = Colour()
        self.colour.colour = colour

    def __repr__(self):
        return "{}. Цвет: {}. Радиус: {}. Площадь: {}.".format(
            Circle.get_shape_name(), self.colour, self.radius, self.area())

    def area(self):
        return pi * self.radius ** 2

    @classmethod
    def get_shape_name(cls):
        return cls.SHAPE_NAME
