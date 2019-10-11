from math import ceil
from fractions import Fraction

from utils import gcd


def main():
    min_dist = Fraction(3 / 7)
    for d in range(2, 10**6 + 1):
        n = ceil(d * 3 / 7) - 1
        if gcd(n, d) == 1:
            dist = Fraction(3, 7) - Fraction(n, d)
            if dist < min_dist:
                min_dist = dist
                closest_fraction = Fraction(n, d)
    print(closest_fraction.numerator)


if __name__ == "__main__":
    main()
