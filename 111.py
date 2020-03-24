from itertools import combinations, product

from utils import is_prime


def digits_to_int(digits):
    ret = 0
    for d in digits:
        ret *= 10
        ret += d
    return ret


def S(n, d):
    digits = [d] * n
    for non_reps in range(1, n):
        total = 0
        for positions, values in product(
            combinations(range(n), non_reps),
            product(range(10), repeat=non_reps),
        ):
            for p, v in zip(positions, values):
                digits[p] = v
            if digits[0] != 0 and is_prime(digits_to_int(digits)):
                total += digits_to_int(digits)
            for p in positions:
                digits[p] = d
        if total > 0:
            return total


def main():
    n = 10
    print(sum(S(n, d) for d in range(10)))


if __name__ == "__main__":
    main()
