from math import floor, sqrt

from numba import njit
import numpy as np

from utils import gcd


@njit
def is_square(n):
    return floor(sqrt(n)) ** 2 == n


@njit
def count_quadrilaterals(m):
    gcd_vals = np.zeros((m, m))
    for i in range(m):
        for j in range(m):
            gcd_vals[i, j] = gcd(i + 1, j + 1)

    count = 0
    for a in range(1, m + 1):
        for b in range(1, m + 1):
            for c in range(1, m + 1):
                for d in range(1, m + 1):
                    area_term = a * b + b * c + c * d + d * a
                    edge_term = (
                        gcd_vals[a - 1, b - 1]
                        + gcd_vals[b - 1, c - 1]
                        + gcd_vals[c - 1, d - 1]
                        + gcd_vals[d - 1, a - 1]
                    )
                    count += is_square((area_term - edge_term) // 2 + 1)
    return count


def main():
    print(count_quadrilaterals(100))


if __name__ == "__main__":
    main()
