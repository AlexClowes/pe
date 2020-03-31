from numba import njit
import numpy as np

from utils import is_prime, get_primes_up_to_n


@njit
def consec_primes(n, primes):
    if n % 3 == 0 or n % 7 not in (3, 4):
        return False
    for p in primes:
        if p > n:
            if is_prime(n * n + 21):
                return False
            return True
        r = n % p
        for s in (1, 3, 7, 9, 13, 27):
            if (r * r + s) % p == 0:
                return False


def main():
    n_max = 15 * 10 ** 7
    primes = np.fromiter(get_primes_up_to_n(n_max + 27), dtype=np.int32)[4:]
    print(sum(n for n in range(10, n_max, 10) if consec_primes(n, primes)))


if __name__ == "__main__":
    main()
