def main():
    N, b = 4, 3
    while N <= 10 ** 12:
        N, b = 3 * N + 4 * b - 3, 2 * N + 3 * b - 2
    print(b)


if __name__ == "__main__":
    main()
