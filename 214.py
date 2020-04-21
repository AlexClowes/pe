from numba import njit
import numpy as np

from utils import get_primes_up_to_n


@njit
def totient_sieve(n_max, primes):
    totients = np.arange(n_max + 1, dtype=np.int32)
    for p in primes:
        totients[p::p] //= p
        totients[p::p] *= p - 1
    return totients


def main():
    n_max = 4 * 10 ** 7
    target_length = 25

    primes = list(get_primes_up_to_n(n_max))
    totients = totient_sieve(n_max, np.array(primes))

    @njit
    def chain_length(n):
        if n == 1:
            return 1
        return 1 + chain_length(totients[n])

    print(sum(p for p in primes if chain_length(p) == target_length))


if __name__ == "__main__":
    main()
