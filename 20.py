def fact(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod


def sum_digits(n):
    return sum(map(int, str(n)))


def main():
    print(fact(100))
    print(sum_digits(fact(100)))


if __name__ == "__main__":
    main()
