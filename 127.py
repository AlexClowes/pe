from collections import defaultdict
from functools import lru_cache

from utils import gcd, get_primes_up_to_n


def main():
    N = 12 * 10 ** 4

    primes = list(get_primes_up_to_n(N))

    @lru_cache(maxsize=None)
    def rad(n):
        ret = 1
        for p in primes:
            if p > n:
                break
            if n % p == 0:
                ret *= p
                n //= p
        return ret

    # Possible optimisation - compute radicals and primes simultaneously
    rads = defaultdict(list)
    for n in range(1, N):
        rads[rad(n)].append(n)
    rads = sorted((rad, lst) for rad, lst in rads.items())

    total = 0
    for c in range(2, N):
        rad_c = rad(c)
        if 2 * rad_c >= c:
            continue
        for rad_a, a_vals in rads:
            if 2 * rad_a * rad_c >= c:
                break
            for a in a_vals:
                if 2 * a > c:
                    break
                if rad_a * rad(c - a) * rad_c < c and gcd(c - a, a) == 1:
                    total += c
    print(total)


if __name__ == "__main__":
    main()
