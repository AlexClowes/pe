def bin_coef(n, r):
    coef = 1
    for i in range(r):
        coef *= n - i
    for i in range(1, r + 1):
        coef //= i
    return coef


def main():
    n = 100
    print(bin_coef(n + 9, 9) + bin_coef(n + 10, 10) - 10 * n - 2)


if __name__ == "__main__":
    main()
