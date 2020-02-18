from numba import vectorize
import numpy as np

from utils import get_primes_up_to_n, powmod


@vectorize("int32(int32)", target="parallel")
def S(p):
    inv_2 = powmod(2, p - 2, p)
    inv_6 = powmod(6, p - 2, p)
    inv_24 = (inv_2 * inv_2 * inv_6) % p
    inv_24 = (((inv_2 * inv_2) % p) * inv_6) % p
    return (-inv_2 + inv_6 - inv_24) % p


def main():
    primes = np.fromiter(get_primes_up_to_n(10 ** 8), dtype=np.int32)[2:]
    print(np.sum(S(primes)))


if __name__ == "__main__":
    main()
