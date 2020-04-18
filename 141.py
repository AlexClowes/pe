from math import floor, sqrt

from numba import njit

from utils import gcd


@njit
def is_square(n):
    return floor(sqrt(n)) ** 2 == n


@njit
def main():
    n_max = 10 ** 12
    total = 0
    for a in range(2, floor(n_max ** (1 / 3))):
        for b in range(1, a):
            if (
                (a % 2 == 1 or b % 2 == 1)
                and (a % 3 != 0 or b % 3 != 0)
                and gcd(a, b) == 1
            ):
                c = 1
                while True:
                    n = b * c * (a ** 3 * c + b)
                    if n > n_max:
                        break
                    if is_square(n):
                        total += n
                    c += 1
    print(total)


if __name__ == "__main__":
    main()
