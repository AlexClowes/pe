from math import gcd


def main():
    total = 0
    for d in range(1, 12001):
        for n in range(1, d + 1):
            if 2 * n < d < 3 * n and gcd(n, d) == 1:
                total += 1
    print(total)


if __name__ == "__main__":
    main()
