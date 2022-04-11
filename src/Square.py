from Figure import Figure

class Square(Figure):

    def __init__(self, name, side):
        super().__init__(name)
        self.name = name
        self.side = side
        Square.get_square(self)
        Square.get_perimetr(self)

    def get_square(self):
        self.area = self.side ** 2
        print('is area', self.name, self.area)

    def get_perimetr(self):
        self.perimetr = 4 * self.side
        print('is perimetr', self.name, self.perimetr)

square1 = Square('square1', 2)
square2 = Square('square2', 4)

square2.add_area(square1)
