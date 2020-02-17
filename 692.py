from functools import lru_cache


@lru_cache()
def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


@lru_cache()
def Gfib(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    return fib(n - 1) + Gfib(n - 1) + Gfib(n - 2)


def main():
    print(Gfib(79))


if __name__ == "__main__":
    main()
