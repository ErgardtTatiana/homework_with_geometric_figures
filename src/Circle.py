from Figure import Figure
import math

class Circle(Figure):

    def __init__(self, name, radius):
        super().__init__(name)
        self.name = name
        self.radius = radius
        Circle.get_square(self)
        Circle.get_perimetr(self)

    def get_square(self):
        self.area = math.pi * (self.radius ** 2)
        print('is area', self.name, self.area)

    def get_perimetr(self):
        self.perimetr = 2 * math.pi * self.radius
        print('is perimetr', self.name, self.perimetr)

circle1 = Circle('circle1', 10)
circle2 = Circle('circle2', 20)

circle1.add_area(circle2)
