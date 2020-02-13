from functools import lru_cache


@lru_cache()
def count_the_ways(free, size):
    if size > free:
        return 0
    return sum(1 + count_the_ways(leftover, size) for leftover in range(free - size + 1))


def main():
    print(sum(count_the_ways(50, size) for size in range(2, 5)))


if __name__ == "__main__":
    main()
