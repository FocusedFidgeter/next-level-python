# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Exercise: Calculate total prices and filter orders
# Use generator expressions to calculate the total prices for each sales order and filter
# orders with a total price greater than $100.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Order:
    product: str
    quantity: int
    price: Decimal


def calculate_total_price(quantity: int, price: Decimal) -> Decimal:
    return quantity * price


def main() -> None:
    # List of sales orders
    sales_orders = [
        Order(product="A", quantity=5, price=Decimal("60.00")),
        Order(product="B", quantity=3, price=Decimal("15.00")),
        Order(product="C", quantity=2, price=Decimal("20.00")),
        Order(product="D", quantity=4, price=Decimal("45.00")),
    ]

    # Use a generator expression to generate a sequence of total prices for each sales order
    total_prices = (
        calculate_total_price(order.quantity, order.price) for order in sales_orders
    )
    # I didn't realize that generators were consumed like a stack would be.
    # This was the source of a "bug" I was experiencing with the iterator exercises as well
    # print(list(total_prices))

    # use another generator to filter the total_prices iterator
    over_100 = (price for price in total_prices if price > 100)
    # my instinct here was to write `over_100 = [price for price in total_prices if price > 100]`
    # but I had to stop myself because that is just list comprehension, not a generator expression

    print(list(over_100))


if __name__ == "__main__":
    main()
