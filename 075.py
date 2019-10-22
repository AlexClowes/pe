from collections import defaultdict
from math import ceil, gcd, sqrt


def main():
    L_max = 1500000
    counter = defaultdict(int)
    for m in range(1, ceil(sqrt(L_max / 2))):
        for n in range(1, min(m, ceil(L_max / (2 * m)) - m)):
            if (m % 2 == n % 2) or gcd(m, n) != 1:
                continue
            primitive_length = 2 * m * (m + n)
            for L in range(primitive_length, L_max + 1, primitive_length):
                counter[L] += 1
    total = 0
    for L in counter:
        if counter[L] == 1:
            total += 1
    print(total)


if __name__ == "__main__":
    main()
