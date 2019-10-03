def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    prod = 2
    for i in range(3, 21):
        prod = lcm(prod, i)
    print(prod)


if __name__ == "__main__":
    main()
