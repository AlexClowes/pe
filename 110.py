from math import ceil, log

from utils import get_first_n_primes


def prod(it):
    p = 1
    for el in it:
        p *= el
    return p


def main():
    N = 4 * 10 ** 6
    n_primes = ceil(log(2 * N - 1) / log(3))
    primes = get_first_n_primes(n_primes)
    upper_bound = prod(primes)

    incr = prod(primes[:-3])
    for n in range(incr, upper_bound + 1, incr):
        exponents = [0] * len(primes)
        for i, p in enumerate(primes):
            while n % p == 0:
                exponents[i] += 1
                n = n // p
        if n != 1:
            continue
        if prod(1 + 2 * e for e in exponents) > 2 * N - 1:
            print(prod(p ** e for p, e in zip(primes, exponents)))
            break


if __name__ == "__main__":
    main()
