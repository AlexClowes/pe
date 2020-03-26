from numba import njit

from utils import gcd


@njit
def main():
    max_perimeter = 10 ** 8
    count = 0
    for m in range(2, int((max_perimeter / 2) ** 0.5) + 1):
        for n in range(m - 1, 0, -2):
            if gcd(m, n) == 1:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                c = (m + n ) * (m + n) - b
                if c % abs(b - a) == 0:
                    count += max_perimeter // (a + b + c)
    print(count)


if __name__ == "__main__":
    main()
