from math import floor, sqrt

from numba import njit
import numpy as np

from utils import get_primes_up_to_n


@njit
def is_square(n):
    return floor(sqrt(n)) ** 2 == n


@njit
def sum_square_sigma(n_max, primes):
    sigma = [1] * n_max
    for p in primes:
        mult = [1] * (n_max // p)
        p_pow = p
        while p_pow < n_max:
            for i in range(p_pow // p - 1, n_max // p, p_pow // p):
                mult[i] += p_pow * p_pow
            p_pow *= p
        for i, m in enumerate(mult):
            sigma[p - 1 + i * p] *= m

    total = 0
    for i, s in enumerate(sigma):
        if is_square(s):
            total += i + 1
    return total


def main():
    n_max = 64 * 10 ** 6
    primes = np.fromiter(get_primes_up_to_n(n_max), dtype=np.int32)
    print(sum_square_sigma(n_max, primes))


if __name__ == "__main__":
    main()
