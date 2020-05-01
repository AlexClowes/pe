from numba import njit
import numpy as np

from utils import get_primes_up_to_n, powmod


@njit
def tonelli_shanks(p, n):
    Q = p - 1
    S = 0
    while Q % 2 == 0:
        Q //= 2
        S += 1
    for z in range(3, p - 1):  # Assume p = +-1 (mod 8), so 2 is a quad residue
        if powmod(z, (p - 1) // 2, p) == p - 1:
            break
    M = S
    c = powmod(z, Q, p)
    t = powmod(n, Q, p)
    R = powmod(n, (Q + 1) // 2, p)
    while t != 1:  # Assume t != 0
        i = 0
        tsq = t
        while tsq != 1:
            i += 1
            tsq = (tsq * tsq) % p
        b = powmod(c, 2 ** (M - i - 1), p)
        M = i
        c = (b * b) % p
        t = (t * c) % p
        R = (R * b) % p
    return min(R, p - R)


def count_primes(n_max):
    tn_is_prime = np.ones(n_max + 1, dtype=np.bool)
    primes = [p for p in get_primes_up_to_n(int(2 ** 0.5 * n_max)) if p % 8 in (1, 7)]
    for p in primes:
        if p % 8 == 7:
            # In this case, square root is easy to find
            r = powmod((p - 1) // 2, (p + 1) // 4, p)
            r = min(r, p - r)
        else:
            r = tonelli_shanks(p, (p + 1) // 2)
        tn_is_prime[p - r :: p] = False
        tn_is_prime[p + r :: p] = False
    return np.sum(tn_is_prime[2:])


def main():
    print(count_primes(5 * 10 ** 7))


if __name__ == "__main__":
    main()
