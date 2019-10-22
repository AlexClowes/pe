from fractions import Fraction
from itertools import islice


def e_partial_values():
    yield 2
    yield 1
    n = 0
    while True:
        n += 2
        yield n
        yield 1
        yield 1


def nth_convergent(n, partial_values):
    values = list(islice(partial_values, n))
    ret = Fraction(0)
    for v in values[::-1]:
        ret = 1 / (ret + v)
    return 1 / ret


def main():
    num = nth_convergent(100, e_partial_values()).numerator
    print(sum(map(int, str(num))))


if __name__ == "__main__":
    main()
