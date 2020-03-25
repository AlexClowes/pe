from functools import lru_cache


@lru_cache(maxsize=None)
def count_the_ways(n, a, b):
    if n == 1:
        return max(0, 10 - a - b)
    return sum(count_the_ways(n - 1, b, i) for i in range(10 - a - b))


def main():
    print(count_the_ways(20, 0, 0) - count_the_ways(19, 0, 0))


if __name__ == "__main__":
    main()
