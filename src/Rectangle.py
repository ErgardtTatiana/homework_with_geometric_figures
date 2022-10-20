from .Figure import Figure


class Rectangle(Figure):

    @property
    def area(self):
        if self._area == None:
            self._area = self.side1 * self.side2
        return self._area


    @property
    def perimeter(self):
        if self._perimeter == None:
            self._perimeter = (self.side1 + self.side2) * 2
        return self._perimeter


    def __init__(self, name, side1, side2):
        super().__init__(name)
        self._area = None
        self._perimeter = None
        if (side2 <= 0) or (side1 <= 0):
            raise ValueError('Передана не геометрическая фигура')
        self.side1 = side1
        self.side2 = side2




