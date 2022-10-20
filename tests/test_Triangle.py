from ..src.Triangle import Triangle
import math

def test_perimeter():
    triangle1 = Triangle('Triangle_4_4_4', 4, 4, 4)
    assert triangle1.perimeter == 12


def test_area():
    triangle1 = Triangle('Triangle_4_4_4', 4, 4, 4)
    assert triangle1.area == math.sqrt(48)

def test_sides_for_existance_of_figure():
    try:
        triangle1 = Triangle('Не существующий треугольник', 1,2,40)
    except:
        assert True
    else:
        assert False

