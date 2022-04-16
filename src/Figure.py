class Figure():
    area = None
    perimetr = None


    def __init__(self, name):
        self.name = name


    def add_area(self, figure):
            return print('is add_area:', self.area + figure.area)


