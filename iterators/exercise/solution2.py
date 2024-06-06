import itertools


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_chained_permutations(data: list[int]) -> list[int]:
    # Use itertools to generate all permutations of the data list
    permutations = itertools.permutations(data)

    # Filter the permutations to keep only those where the first element is prime
    filtered_permutations = filter(lambda x: is_prime(x[0]), permutations)

    # Chain together the filtered permutations
    chained_permutations = itertools.chain.from_iterable(filtered_permutations)

    return list(chained_permutations)

def main() -> None:
    # Test data

    data = [1, 2, 3, 4, 5]
    
    chained_permutations: list[int] = calculate_chained_permutations(data)

    # Sum of chained_permutations
    print(sum(chained_permutations))


if __name__ == "__main__":
    main()
