def coords_reader():
    with open("data/p102_triangles.txt") as f:
        for line in f:
            coords = [int(n) for n in line.split(",")]
            yield (coords[0:2], coords[2:4], coords[4:6])


def contains_origin(x, y, z):
    y[0], y[1] = y[0] - x[0], y[1] - x[1]
    z[0], z[1] = z[0] - x[0], z[1] - x[1]
    den = y[0] * z[1] - y[1] * z[0]
    s = (y[1] * x[0] - y[0] * x[1]) / den
    t = (z[0] * x[1] - z[1] * x[0]) / den
    return 0 < s < 1 and 0 < t < 1 and s + t < 1


def main():
    print(sum(contains_origin(x, y, z) for x, y, z in coords_reader()))


if __name__ == "__main__":
    main()
