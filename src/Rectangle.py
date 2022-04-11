from Figure import Figure

class Rectangle(Figure):

    def __init__(self, name, side1, side2):
        super().__init__(name)
        self.name = name
        self.side1 = side1
        self.side2 = side2
        Rectangle.get_square(self)
        Rectangle.get_perimetr(self)

    def get_square(self):
        self.area = self.side1 * self.side2
        print('is area', self.name, self.area)

    def get_perimetr(self):
        self.perimetr = (self.side1 + self.side2) ** 2
        print('is perimetr', self.name, self.perimetr)

rectangle1 = Rectangle('rectangle1', 2, 4)
rectangle2 = Rectangle('rectangle2', 4, 5)

rectangle1.add_area(rectangle2)
