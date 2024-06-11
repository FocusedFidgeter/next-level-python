# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Exercise: Generate permutations and filter based on conditions
# Use itertools to generate all permutations of the data list. Filter the permutations
# to keep only those where the first element is prime. Use itertools to chain together the
# filtered permutations. The expected output of this program is 1080.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import itertools

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def calculate_chained_permutations(data: list[int]) -> list[int]:
    perms = itertools.permutations(data)
    filtered_perms = filter(lambda x: is_prime(x[0]), perms)
    chained_perms = itertools.chain.from_iterable(filtered_perms)
    return list(chained_perms)


def main() -> None:
    data = [1, 2, 3]

    # TODO: Use itertools to generate all permutations of the data list
    perms: list[list[int]] = list(itertools.permutations(data))
    # TODO: Filter the permutations to keep only those where the first element is prime
    filtered_perms: list[list[int]] = list(filter(lambda x: is_prime(x[0]), perms))
    # TODO: Use itertools to chain together the filtered permutations
    chained_perms: list[int] = list(itertools.chain.from_iterable(filtered_perms))
    # Use the calculate_chained_permutations function to get the result
    chained_permutations: list[int] = calculate_chained_permutations(data)

    print(chained_permutations)
    # Print the sum of the chained permutations
    print("Sum of chained permutations:", sum(chained_permutations))


if __name__ == "__main__":
    main()
