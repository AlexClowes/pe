from functools import lru_cache


@lru_cache()
def count_the_ways(n_tiles, tile_size):
    if n_tiles < 0:
        return 0
    if n_tiles == 0:
        return 1
    return count_the_ways(n_tiles - 1, tile_size) + count_the_ways(n_tiles - tile_size, tile_size)


def main():
    print(sum(count_the_ways(50, size) - 1 for size in range(2, 5)))


if __name__ == "__main__":
    main()
