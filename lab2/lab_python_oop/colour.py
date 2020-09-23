class Colour:
    def __init__(self):
        self._colour = None

    def get_colour(self):
        return self._colour

    def set_colour(self, colour):
        self._colour = colour

    def del_colour(self):
        del self._colour

    def __repr__(self):
        return str(self._colour)

    colour = property(get_colour, set_colour, del_colour, "This is the colour property.")
