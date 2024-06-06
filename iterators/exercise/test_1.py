from solution1 import calculate_combination_averages

def test_calculate_combination_averages():
    result: list[float] = calculate_combination_averages([1, 2, 3, 4, 5])
    assert result == [1.5, 2.0, 2.5, 3.0, 2.5, 3.0, 3.5, 3.5, 4.0, 4.5]

