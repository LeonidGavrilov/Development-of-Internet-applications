from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    SHAPE_NAME = "Квадрат"

    def __init__(self, side, colour):
        self.side = side
        super().__init__(self.side, self.side, colour)

    def __repr__(self):
        return "{}. Цвет: {}. Сторона: {}. Площадь: {}.".format(
            Square.get_shape_name(), self.colour, self.side, self.area())

    @classmethod
    def get_shape_name(cls):
        return cls.SHAPE_NAME
