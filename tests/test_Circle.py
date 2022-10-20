from ..src.Circle import Circle
import math


def test_perimeter():
    circle1 = Circle('Circle_with_radius_4', 4)
    assert circle1.perimeter == 8*math.pi

def test_area():
    circle1 = Circle('Circle_with_radius_4', 4)
    assert circle1.area == 16*math.pi

def test_radius():
    try:
        circle1 = Circle('Circle_with_negative_radius', -1)
    except:
        assert True
    else:
        assert False
