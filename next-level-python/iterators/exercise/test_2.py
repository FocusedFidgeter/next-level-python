from solution2 import is_prime, calculate_chained_permutations

def test_is_prime():
    assert is_prime(2)
    assert is_prime(5)
    assert not is_prime(4)
    assert not is_prime(9)

def test_sum_of_calculate_chained_permutations():
    data = [1, 2, 3, 4, 5]

    result = calculate_chained_permutations(data)
    
    assert sum(result) == 1080
