from collections import defaultdict
from itertools import product, starmap

from utils import gcd


def reduced(num, den):
    common_div = gcd(num, den)
    return num // common_div, den // common_div


def add(x, y):
    a, b = x
    c, d = y
    return reduced(a * d + b * c, b * d)


def D(n):
    capacitance_vals = defaultdict(set)
    capacitance_vals[1].add((1, 1))
    for i in range(2, n + 1):
        for j in range(1, i):
            for x, y in product(capacitance_vals[j], capacitance_vals[i - j]):
                for c1 in (x, x[::-1]):
                    for c2 in (y, y[::-1]):
                        c = add(c1, c2)
                        if c[0] > c[1]:
                            capacitance_vals[i].add(c)
                        else:
                            capacitance_vals[i].add(c[::-1])
        for j in range(1, i):
            capacitance_vals[i] -= capacitance_vals[j]
    return 2 * len(set().union(*capacitance_vals.values())) - 1


def main():
    print(D(18))


if __name__ == "__main__":
    main()
