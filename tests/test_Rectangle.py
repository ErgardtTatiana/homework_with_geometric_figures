from ..src.Rectangle import Rectangle
import math


def test_perimeter():
    rectangle1 = Rectangle('Triangle_4_8', 4, 8)
    assert triangle1.perimeter == 24


def test_area():
    rectangle1 = Rectangle('Triangle_4_8', 4, 8)
    assert rectangle1.area == 32


def test_sides_for_existance_of_figure():
    try:
        rectangle1 = Rectangle('Не существующий прямоугольник', 0, 4)
    except:
        assert True
    else:
        assert False
