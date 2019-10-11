from collections import defaultdict
from math import ceil, floor


def n_digit_cubes(n):
    for i in range(ceil(10 ** ((n - 1) / 3)), floor(10 ** (n / 3)) + 1):
        yield i * i * i
    min_i = ceil(10 ** ((n - 1) / 3))
    max_i = floor(10 ** (n / 3))
    return [i * i * i for i in range(min_i, max_i + 1)]


def main():
    n = 0
    done = False
    while not done:
        n += 1
        cubes = n_digit_cubes(n)
        digit_cubes_map = defaultdict(list)
        for cube in cubes:
            digit_cubes_map["".join(sorted(str(cube)))].append(cube)
        smallest_cube = 10**n
        for k, v in digit_cubes_map.items():
            if len(v) == 5:
                if v[0] < smallest_cube:
                    smallest_cube = v[0]
                done = True
    print(smallest_cube)


if __name__ == "__main__":
    main()
