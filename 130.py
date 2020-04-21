from itertools import count, islice

from utils import gcd, is_prime


def A(n):
    mod = 9 * n
    k = 1
    pow10 = 10 % mod
    while pow10 != 1:
        k += 1
        pow10 = (pow10 * 10) % mod
    return k


def main():
    composites = (
        n for n in count(2)
        if gcd(n, 10) == 1 and not is_prime(n) and (n - 1) % A(n) == 0
    )
    print(sum(islice(composites, 25)))


if __name__ == "__main__":
    main()
