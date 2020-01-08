from math import floor, sqrt

from utils import get_primes_up_to_n


def get_factors(n):
    # We know that n is always even
    n //= 2
    for i in range(3, floor(sqrt(n)) + 1):
        if n % i == 0:
            yield i
            yield 2 * i


def main():
    primes = set(get_primes_up_to_n(10 ** 8))
    total = 0
    for p in primes:
        if p % 4 != 1 and p % 9 != 1 and p % 25 != 1:
            candidate = p - 1
            factors = get_factors(candidate)
            if candidate // 2 + 2 in primes and all(f + candidate / f in primes for f in factors):
                total += candidate
    print(total)


if __name__ == "__main__":
    main()
