from functools import lru_cache


@lru_cache()
def count_the_ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return count_the_ways(n - 1) + sum(count_the_ways(k) for k in range(n - 3)) + (n > 2)


def main():
    print(count_the_ways(50))


if __name__ == "__main__":
    main()
