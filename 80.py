from fractions import Fraction
from math import floor, sqrt


def digit_sum(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n = n // 10
    return ret


def square_root_digit_sum(n):
    x = Fraction(floor(sqrt(n)))
    while x.denominator < 10**99:
        x = (x + n / x) / 2
    return digit_sum(floor(x * 10 ** 99))


def main():
    total = 0
    for n in range(2, 101):
        if floor(sqrt(n))**2 != n:
            total += square_root_digit_sum(n)
    print(total)


if __name__ == "__main__":
    main()
