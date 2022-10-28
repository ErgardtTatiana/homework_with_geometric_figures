from .Figure import Figure
import math


class Triangle(Figure):

    @property
    def perimeter(self):
        if self._perimeter == None:
            self._perimeter = self.side1 + self.side2 + self.side3
        return self._perimeter

    @property
    def area(self):
        if self._area == None:
            hp = self.perimeter / 2
            self._area = math.sqrt(hp * (hp - self.side1) * (hp - self.side2) * (hp - self.side3))
        return self._area

    def __init__(self, name, side1, side2, side3):
        super().__init__(name)
        self._area = None
        self._perimeter = None
        if ((side1 + side2) < side3) or ((side2 + side3) < side1) or ((side1 + side3) < side2):
            raise ValueError('Не выполнено основное правило существования треугольника')
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
