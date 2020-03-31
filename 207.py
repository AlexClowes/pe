def main():
    k = 1
    while 12345 * k > 2 * (2 ** k - 1):
        k += 1
    r = 12345 * k - 2 ** k + 2
    n = 2 ** k + r
    m = n * (n - 1)
    print(m)


if __name__ == "__main__":
    main()
