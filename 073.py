from math import gcd


def main():
    total = 0
    for d in range(1, 12001):
        for n in range(d // 3 + 1, (d + 1) // 2):
            if gcd(n, d) == 1:
                total += 1
    print(total)


if __name__ == "__main__":
    main()
