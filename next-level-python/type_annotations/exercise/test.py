from typing import get_type_hints
from exercise import calculate_total_sales, calculate_average

def test_type_annotations():
    functions_to_test = [
        (calculate_average, {"numbers": list[int], "return": float}),
        (calculate_total_sales, {"sales": dict[str, int], "return": int}),
    ]

    for (func, wanted_types) in functions_to_test:
        res = get_type_hints(func)
        assert res == wanted_types
