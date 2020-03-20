from itertools import islice

from utils import get_primes_up_to_n


def main():
    k = 10 ** 9
    primes = get_primes_up_to_n(10 ** 6)
    prime_factors = (p for p in primes if p > 5 and pow(10, k % (p - 1), p) == 1)
    print(sum(islice(prime_factors, 40)))


if __name__ == "__main__":
    main()
