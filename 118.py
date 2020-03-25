from itertools import chain, permutations

from utils import is_prime


def concatenate(args):
    ret = 0
    for arg in args:
        ret *= 10
        ret += arg
    return ret


def count_sets(digits, prev_choice=0):
    if len(digits) == 0:
        return 1
    if len(digits) == 1:
        digit = digits.pop()
        return int(digit > prev_choice and is_prime(digit))
    total = 0
    for choice in chain.from_iterable(
        permutations(digits, r) for r in range(1, len(digits) + 1)
    ):
        choice_int = concatenate(choice)
        if choice_int > prev_choice and is_prime(choice_int):
            total += count_sets(digits - set(choice), choice_int)
    return total


def main():
    print(count_sets(set(range(1, 10))))


if __name__ == "__main__":
    main()
