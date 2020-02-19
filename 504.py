from itertools import product
from math import ceil


tri_memo = {}
def lattice_points_tri(a, b):
    if (a, b) not in tri_memo:
        tri_memo[a, b] = tri_memo[b, a] = sum(ceil(b - b * x / a - 1) for x in range(1, a))
    return tri_memo[a, b]


def lattice_points_quad(a, b, c, d):
    ret = -3 + a + b + c + d
    ret += lattice_points_tri(a, b)
    ret += lattice_points_tri(b, c)
    ret += lattice_points_tri(c, d)
    ret += lattice_points_tri(d, a)
    return ret


def count_quadrilaterals(m):
    squares = {n * n for n in range(2 * m)}
    count = 0
    for a, b, c, d in product(range(1, m + 1), repeat=4):
        count += lattice_points_quad(a, b, c, d) in squares
    return count


def main():
    print(count_quadrilaterals(100))


if __name__ == "__main__":
    main()
