from functools import lru_cache


@lru_cache(maxsize=None)
def f(n, m):
    if n == 0:
        return 1
    if n < 0 or 4 * m - 2 < n:
        return 0
    return f(n, m // 2) + f(n - m, m // 2) + f(n - 2 * m, m // 2)


def main():
    n = 10 ** 25
    m = 1
    while 2 * m < n:
        m *= 2
    print(f(n, m))


if __name__ == "__main__":
    main()
