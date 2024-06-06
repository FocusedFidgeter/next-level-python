# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Exercise: Generate combinations and calculate averages
# Use itertools to generate all possible combinations of length 2 from the data list.
# Calculate the average of each combination and store the results in a new list.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from typing import Collection


# Note: I'm using the Collection type hint here, which is a generic type hint
# for collections/iterables that support the len() function.
def calculate_average(numbers: Collection[int]) -> float:
    total = sum(numbers)
    return total / len(numbers)


def calculate_combination_averages(data: list) -> list[float]:
    # TODO: Use itertools to generate all possible combinations of length 2 from the data list
    # TODO: Calculate the average of each combination and store the results in a new list
    ...


def main() -> None:
    data = [1, 2, 3, 4, 5]

    averages: list[float] = calculate_combination_averages(data)

    # Print the average of each combination
    print("Averages of combinations:")
    for average in averages:
        print(average)


if __name__ == "__main__":
    main()
