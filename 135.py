def get_factors(n_max):
    factors = [[] for n in range(n_max)]
    for val in range(1, n_max):
        for f in factors[val::val]:
            f.append(val)
    return factors


def count_solutions(n, factors):
    count = 0
    for y in factors:
        if (n // y + y) % 4 == 0:
            d = (n // y + y) // 4
            if d < y:
                count += 1
    return count


def main():
    n_max = 10 ** 6

    factors = get_factors(n_max)

    count = 0
    for n in range(1, n_max):
        if n % 4 != 2 and count_solutions(n, factors[n]) == 10:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
