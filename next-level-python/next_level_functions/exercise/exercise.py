# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Exercise: Partial function application for Square, and Cube
# Use partial function application to define the square and cube functions based on the power
# function so that the statements in the main function work correctly.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def power(base: float, exponent: float) -> float:
    return base**exponent


# TODO: Define the square and cube functions using partial


def main() -> None:
    print("Square of 5:", square(5))
    print("Cube of 3:", cube(3))


if __name__ == "__main__":
    main()
