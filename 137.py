def nugget(n):
    a, b = 1, 2
    for i in range(2 * n - 2):
        a, b = b, a + b
    return a * b


def main():
    print(nugget(15))


if __name__ == "__main__":
    main()
