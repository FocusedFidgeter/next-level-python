from exercise import Order, calculate_total_price
from decimal import Decimal

def test_calculate_total_price():
    result = calculate_total_price(3, Decimal("25.00"))
    assert result == Decimal("75.00")

def test_order_creation():
    order = Order(product="A", quantity=5, price=Decimal("60.00"))
    assert order.product == "A"
    assert order.quantity == 5
    assert order.price == Decimal("60.00")
