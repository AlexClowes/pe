import functools


@functools.lru_cache(maxsize=None)
def ends_in_89(n):
    if n == 1:
        return False
    if n == 89:
        return True
    ret = 0
    while n > 0:
        r = n % 10
        ret += r * r
        n //= 10
    return ends_in_89(ret)


def main():
    print(sum(ends_in_89(n) for n in range(1, 10**7)))


if __name__ == "__main__":
    main()
