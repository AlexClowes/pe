from functools import lru_cache


MOD = 10 ** 9 + 7


@lru_cache()
def fib(n):
    return n if n <= 1 else fib(n - 1) + fib(n - 2)


def s(n):
    q, r = divmod(n, 9)
    return (r + 1) * pow(10, q, MOD) - 1


def S(k):
    q, r = divmod(k, 9)
    ret = 6 * pow(10, q, MOD) - 6 - 9 * q
    ret += sum(s(9 * q + i) for i in range(1, r + 1))
    return ret % MOD


def main():
    print(sum(S(fib(i)) for i in range(2, 91)) % MOD)


if __name__ == "__main__":
    main()
