from .Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, name, side1):
        super().__init__(name, side1, side1)
