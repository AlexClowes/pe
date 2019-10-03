import itertools


def main():
    tri_gen = (n * (n + 1) // 2 for n in itertools.count(1))
    pen_gen = (n * (3 * n - 1) // 2 for n in itertools.count(1))
    hex_gen = (n * (2 * n - 1) for n in itertools.count(1))

    t = next(tri_gen)
    p = next(pen_gen)
    h = next(hex_gen)
    while True:
        if t == p == h:
            print(t)
            h = next(hex_gen)
        while t < p:
            t = next(tri_gen)
        while p < h:
            p = next(pen_gen)
        while h < t:
            h = next(hex_gen)


if __name__ == "__main__":
    main()
