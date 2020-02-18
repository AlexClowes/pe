import numpy as np
from numba import njit, vectorize

from utils import powmod


MOD = 10 ** 9 + 7


@vectorize
def inv(x, mod):
    return powmod(x, mod - 2, mod)


@njit
def get_primes_up_to_n(n):
    # Sieve of eratosthenes
    is_prime = np.ones(n + 1, dtype=np.int32)
    is_prime[:2] = False
    for val in range(2, n + 1):
        if val * val > n:
            break
        # If val is prime, then all its multiples are not prime
        if is_prime[val]:
            is_prime[val * val :: val] = False
    return np.extract(is_prime, np.arange(n + 1))


@njit
def get_prime_factors(n, primes):
    prime_factors = np.zeros((n, len(primes)), dtype=np.int32)
    for i in range(n):
        k = i + 1
        for j in range(len(primes)):
            if k == 1:
                break
            while k % primes[j] == 0:
                prime_factors[i, j] += 1
                k //= primes[j]
    return prime_factors


@njit
def cumsum_axis0(arr):
    ret = np.zeros_like(arr, dtype=arr.dtype)
    ret[0] = arr[0]
    for i in range(1, ret.shape[0]):
        ret[i] = ret[i - 1] + arr[i]
    return ret


@njit
def S(n):
    primes = get_primes_up_to_n(n)

    # Get prime factorisation of 1, 2, ..., n
    prime_factors = get_prime_factors(n, primes)

    # Numba doesn't support axis argument for np.cumsum()...
    prime_factor_sums = cumsum_axis0(prime_factors)

    # Calculate modular inverse of p - 1 for all primes p
    inverses = inv(primes - 1, MOD)

    # Iteratively get prime factorisation of B(1), B(2), ..., B(n), then use
    # this to compute and sum D(1), D(2), ..., D(n)
    total = 0
    bn_prime_factors = np.zeros_like(primes, dtype=np.int32)
    for m in range(n):
        bn_prime_factors += m * prime_factors[m]
        if m > 0:
            bn_prime_factors -= prime_factor_sums[m - 1]

        div_sum = 1
        for i in range(len(primes)):
            if bn_prime_factors[i] > 0:
                div_sum *= powmod(primes[i], bn_prime_factors[i] + 1, MOD) - 1
                div_sum %= MOD
                div_sum *= inverses[i]
                div_sum %= MOD
        total += div_sum
        total %= MOD

    return total


def main():
    print(S(20000))


if __name__ == "__main__":
    main()
