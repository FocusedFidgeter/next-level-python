"""
Below is an example of where to add type hints.
As you can see, I've added them to the function's parameters and return type.
Don't forget that main also has a return type (None).
You can also add type hints to variables, but that's not necessary since
Python is a dynamically typed language and you can easily infer the type from the value.
"""


def calculate_average(numbers: list[int]) -> float:
  length_of_numbers = len(numbers)
  if length_of_numbers > 0:
    return sum(numbers) / length_of_numbers
  return 0.0


def calculate_total_sales(sales: dict[str, int]) -> int:
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
