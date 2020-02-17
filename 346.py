from collections import defaultdict
from math import ceil, floor, log


def rep(n_digits, base):
    return (base ** n_digits - 1) // (base - 1)


def sum_strong_repunits(limit):
    repunit_counts = defaultdict(int)

    # 2 digit case
    repunit_counts = defaultdict(lambda: 1)
    max_base = ceil(limit ** 0.5)
    while rep(3, max_base) > limit:
        max_base -= 1

    # 3 digit case
    for base in range(2, max_base + 1):
        repunit_counts[rep(3, base)] += 1
    max_base = ceil(limit ** (1 / 3))
    while rep(4, max_base) > limit:
        max_base -= 1

    # 1 digit case - 1 is a strong repunit
    repunit_counts[1] += 9999

    for base in range(2, max_base + 1):
        max_digits = floor(log(limit * (base - 1) + 1) / log(base))
        for n_digits in range(4, max_digits + 1):
            repunit_counts[rep(n_digits, base)] += 1
    return sum(r for r, c in repunit_counts.items() if c >= 2)


def main():
    print(sum_strong_repunits(10 ** 12))


if __name__ == "__main__":
    main()
