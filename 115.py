from functools import lru_cache


@lru_cache()
def F(m, n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return F(m, n - 1) + sum(F(m, k) for k in range(n - m)) + (n >= m)


def main():
    n = 1
    while F(50, n) <= 10 ** 6:
        n += 1
    print(n)


if __name__ == "__main__":
    main()
