from itertools import product
from math import floor, sqrt


def is_square(n):
    sn = floor(sqrt(n))
    return sn * sn == n


def main():
    string_pat = "1{}2{}3{}4{}5{}6{}7{}8{}900"
    digits = "0123456789"[::-1]
    candidates = (int(string_pat.format(*tup)) for tup in product(*((digits,) * 7), "048"))
    for n in candidates:
        if is_square(n):
            break
    print(floor(sqrt(n)))


if __name__ == "__main__":
    main()
