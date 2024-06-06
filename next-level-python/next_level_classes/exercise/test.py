from math import pi
from pytest import approx
import pytest
from exercise import Circle  # Replace with the actual import statement for your Circle class

@pytest.fixture
def circle():
    return Circle(5.0)

def test_radius(circle: Circle):
    assert circle.radius == 5.0

    # Test setting a new radius
    circle.radius = 10.0
    assert circle.radius == 10.0

    # Test setting a negative radius
    with pytest.raises(ValueError):
        circle.radius = -5.0

def test_diameter(circle: Circle):
    assert circle.diameter == 10.0

def test_area(circle: Circle):
    assert approx(circle.area, abs=1e-9) == pi * 25.0

def test_circumference(circle: Circle):
    assert approx(circle.circumference, abs=1e-9) == 2 * pi * 5.0
