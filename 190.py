def prod(iterable):
    p = 1
    for el in iterable:
        p *= el
    return p


def P(m):
    return int(prod((2 * n / (m + 1)) ** n for n in range(1, m + 1)))


def main():
    print(sum(P(m) for m in range(2, 16)))


if __name__ == "__main__":
    main()
