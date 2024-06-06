"""
Below is an example implementation of the properties for the Circle class.
Note that the radius property is implemented using a setter, which allows
us to validate the value before setting it.
"""

from dataclasses import dataclass
from math import pi


@dataclass
class Circle:
    _radius: float

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @property
    def diameter(self) -> float:
        return 2 * self._radius

    @property
    def area(self) -> float:
        return pi * self._radius**2

    @property
    def circumference(self) -> float:
        return 2 * pi * self._radius
    
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


if __name__ == "__main__":
    main()
