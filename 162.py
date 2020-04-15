from functools import lru_cache


@lru_cache(maxsize=None)
def f(n, d):
    if n == 0:
        return d == 0
    return (16 - d) * f(n - 1, d) + d * f(n - 1, d - 1)


def count_strings(n_digits):
    return 13 * f(n_digits - 1, 3) + 2 * f(n_digits - 1, 2)


def main():
    result = hex(sum(count_strings(n) for n in range(3, 17)))
    print(result[2:].upper())


if __name__ == "__main__":
    main()
