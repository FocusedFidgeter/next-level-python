# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Exercise: Add type annotations
# Add appropriate type annotations to the functions to specify the types of the parameters
# and return values.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def calculate_average(
    numbers: list[int]
) -> float:
    """
    Calculate the average of a list of integers.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        float: The average of the numbers in the list. If the list is empty, 0.0 is returned.
    """

    length_of_numbers: int = len(numbers)
    if length_of_numbers > 0:
        return sum(numbers) / length_of_numbers
    return 0.0


def calculate_total_sales(
    sales: dict[any, int]
) -> int:
    """
    Calculate the total sales from a dictionary of product sales.

    Args:
        sales (dict[str, int]): A dictionary of product sales.

    Returns:
        int: The total sales.
    """

    return sum(sales.values())


def main() -> None:
    """
    Main function.
    """ 

    data: list[int] = [1, 2, 3, 4, 5]
    average: float = calculate_average(data)
    print("The average is: ", average)

    sales_data: dict[str, int] = {
        "product_a": 100,
        "product_b": 250,
        "product_c": 80,
        "product_d": 150
    }
    print("Sales data for product C: ", sales_data["product_c"])

    total_sales: int = calculate_total_sales(sales_data)
    print("Total sales: ", total_sales)


if __name__ == "__main__":
    main()
