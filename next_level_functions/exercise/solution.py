from functools import partial


def power(base: float, exponent: float) -> float:
    return base**exponent


# Create a partial function 'square' using the 'power' function
square = partial(power, exponent=2)

# Create a partial function 'cube' using the 'power' function
cube = partial(power, exponent=3)


def main() -> None:
    print("Square of 5:", square(5))
    print("Cube of 3:", cube(3))


if __name__ == "__main__":
    main()
