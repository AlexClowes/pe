from utils import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    prod = 2
    for i in range(3, 21):
        prod = lcm(prod, i)
    print(prod)


if __name__ == "__main__":
    main()
