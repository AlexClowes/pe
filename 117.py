def count_the_ways(n_tiles):
    a, b, c, d = 1, 0, 0, 0
    for _ in range(n_tiles):
        a, b, c, d = a + b + c + d, a, b, c
    return a


def main():
    print(count_the_ways(50))


if __name__ == "__main__":
    main()
