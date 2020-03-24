from numba import njit

from utils import get_primes_up_to_n


@njit
def A(n):
    mod = 9 * n
    k = 1
    pow_10 = 10 % mod
    while pow_10 != 1:
        k += 1
        pow_10 = (pow_10 * 10) % mod
    return k


def main():
    primes = get_primes_up_to_n(10 ** 5)
    total = 10  # 2 + 3 + 5
    for p in primes:
        if p < 7:
            continue
        n = A(p)
        while n % 2 == 0:
            n //= 2
        while n % 5 == 0:
            n //= 5
        if n != 1:
            total += p
    print(total)


if __name__ == "__main__":
    main()
