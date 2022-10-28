from ..src.Square import Square
import math


def test_perimeter():
    square1 = Square('Triangle_4_8', 4)
    assert square1.perimeter == 16


def test_area():
    square1 = Square('Triangle_4_8', 4)
    assert square1.area == 16


def test_sides_for_existance_of_figure():
    try:
        square1 = Square('Не существующий квадрат', 0)
    except:
        assert True
    else:
        assert False
