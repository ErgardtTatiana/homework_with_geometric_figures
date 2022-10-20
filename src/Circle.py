from .Figure import Figure
import math


class Circle(Figure):
    @property
    def area(self):
        if self._area == None:
            self._area = math.pi * (self.radius ** 2)
        return self._area

    @property
    def perimeter(self):
        if self._perimeter == None:
            self._perimeter = 2 * math.pi * self.radius
        return self._perimeter

    def __init__(self, name, radius):
        super().__init__(name)
        self._area = None
        self._perimeter = None
        self.radius = radius
        if (radius <= 0):
            raise ValueError('Передана не геометрическая фигура')


