from Figure import Figure
import math


class Triangle(Figure):
    hp: None

    def __init__(self, name, side1, side2, side3):
        super().__init__(name)
        self.name = name
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if ((side1) == (side2)) and ((side2) == (side3)):
            print('Треугольник равносторонний')
        if ((side1 + side2) < side3) or ((side2 + side3) < side1) or ((side1 + side3) < side2):
            raise ValueError('Не выполнено основное правило существования треугольника')
        Triangle.get_square(self)
        Triangle.get_perimetr(self)

    def get_square(self):
        self.hp = (self.side1 + self.side2 + self.side3) / 2
        self.area = math.sqrt(self.hp * (self.hp - self.side1) * (self.hp - self.side2) * (self.hp - self.side3))
        print('is area', self.name, self.area)


    def get_perimetr(self):
        self.perimetr = self.side1 + self.side2 + self.side3
        print('is perimetr', self.name, self.perimetr)



triangle1 = Triangle('triangle1', 11, 12, 15)
triangle2 = Triangle('triangle2', 11, 22, 14)
triangle3 = Triangle('triangle3', 11, 11, 11)

# triangle1.add_area(triangle2)
# if ((side1) == (side2)) and ((side2) == (side3)):
#     print('Треугольник равносторонний')
# if ((side1 + side2) >= side3 or (side2 + side3) >= side1 or (side1 + side3) >= side2):
#     raise ValueError('Не выполнено основное правило существования треугольника')
