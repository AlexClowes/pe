from collections import Counter
from itertools import count
from utils import get_prime_factors


def count_factors(n):
    prime_factors = Counter(get_prime_factors(n))
    total_factors = 1
    for prime, multiplicity in prime_factors.items():
        total_factors *= multiplicity + 1
    return total_factors


def main():
    triangle_numbers = (n * (n + 1) // 2 for n in count(1))
    for t in triangle_numbers:
        if count_factors(t) > 500:
            print(t)
            break


if __name__ == "__main__":
    main()
