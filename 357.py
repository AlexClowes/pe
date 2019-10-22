from math import floor, sqrt

from utils import get_primes_up_to_n


def get_factors(n):
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            yield i


def main():
    primes = set(get_primes_up_to_n(10 ** 8))
    total = 0
    for p in primes:
        candidate = p - 1
        factors = get_factors(candidate)
        if all(f + candidate / f in primes for f in factors):
            total += candidate
    print(total)


if __name__ == "__main__":
    main()
