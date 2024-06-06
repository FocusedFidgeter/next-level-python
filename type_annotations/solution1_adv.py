"""
Here's a more advanced example of type hints. This uses
more generic type annotations. If you look at calculate_average,
you'll see that it takes a collection of integers or floats. This is
more generic than a list of integers. A collection can be
any iterable, such as a list, tuple, set, or dictionary. Ideally,
we'd like to define it as a collection of things that are "summable".
However, there's currently no easy way to do that in Python. So, we
use a union of integers and floats.

Also, notice that the calculate_total_sales function takes
a dictionary of Any and integers. This is more generic
than a dictionary of strings and integers. The function doesn't 
need to know the type of the keys, so we can use Any.
"""


from typing import Any, Collection


def calculate_average(numbers: Collection[int | float]) -> float:
    total = sum(numbers)
    return total / len(numbers)


def calculate_total_sales(sales: dict[Any, int]) -> int:
    return sum(sales.values())


def main() -> None:
    data = [1, 2, 3, 4, 5]
    average = calculate_average(data)
    print("The average is:", average)

    sales_data = {"product_a": 100, "product_b": 250, "product_c": 80, "product_d": 150}
    print("Sales data for product C:", sales_data["product_c"])
    total_sales = calculate_total_sales(sales_data)
    print("Total sales:", total_sales)


if __name__ == "__main__":
    main()
