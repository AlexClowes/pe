from math import factorial


def comb(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def expected_colours(N, K, n):
    return K * (1 - comb(N - N / K, n) / comb(N, n))


def main():
    print(f"{expected_colours(70, 7, 20):.9f}")


if __name__ == "__main__":
    main()
