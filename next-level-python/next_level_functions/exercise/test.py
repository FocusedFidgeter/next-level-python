import pytest
from solution import power, square, cube

def test_power():
    result = power(2, 3)
    assert pytest.approx(result, rel=1e-7) == 8.0

def test_square():
    result = square(5)
    assert pytest.approx(result, rel=1e-7) == 25.0

def test_cube():
    result = cube(3)
    assert pytest.approx(result, rel=1e-7) == 27.0
