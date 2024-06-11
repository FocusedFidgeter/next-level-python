# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Exercise: Properties for classes
# Enhance the provided Python code by adding essential properties to the Circle class to ensure
# accurate functionality. Make sure to include suitable type annotations for clarity and correctness.
# The test code is designed to showcase the proper implementation of properties such as radius,
# diameter, area, and circumference within the Circle class. The tests are there too help you to see if
# the implementation is correct.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from dataclasses import dataclass
from math import pi


@dataclass
class Circle:
    _radius: float

    # TODO: Add the properties
    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if self._radius < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @property
    def diameter(self) -> float:
        return 2 * self._radius

    @property
    def area(self) -> float:
        return float(pi * self._radius**2)

    @property
    def circumference(self) -> float:
        return float(2 * pi * self._radius)

    def __repr__(self) -> str:
        return f"Circle(radius={self._radius}, diameter={self.diameter}, area={self.area}, circumference={self.circumference})"

    def __str__(self) -> str:
        return f"Circle(radius={self._radius})"


def create_circle(radius: float) -> Circle:
    return Circle(radius)


def main() -> None:
    circle = create_circle(5.0)

    # Test the properties
    circle.radius = 10
    print("Radius:", circle.radius)
    print("Diameter:", circle.diameter)
    print("Area:", circle.area)
    print("Circumference:", circle.circumference)

    print(circle)

    print(repr(circle))

    print(str(circle))


if __name__ == "__main__":
    main()
