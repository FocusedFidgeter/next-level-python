import itertools
from typing import Collection


# This function calculates the average of a list of numbers
# Note: I'm using the Collection type hint here, which is a generic type hint
# for collections/iterables that support the len() function.
def calculate_average(numbers: Collection[int]) -> float:
    total = sum(numbers)
    return total / len(numbers)

def calculate_combination_averages(data: list[int]) -> list[float]:
    # Use itertools to generate all possible combinations of length 2 from the data list
    combinations = itertools.combinations(data, 2)

    # Calculate the average of each combination and store the results in a new list
    averages = [calculate_average(combination) for combination in combinations]

    return averages

def main() -> None:
    data = [1, 2, 3, 4, 5]

    averages: list[float] = calculate_combination_averages(data)

    # Print the average of each combination

    print(averages)


if __name__ == "__main__":
    main()
