from fractions import Fraction
from itertools import count


def compose(f, g):
    return (f[0] * g[0], f[0] * g[1] + f[1])


def apply(f, n):
    return f[0] * n + f[1]


def get_inv_function(string):
    inverse = {
        "D": (3, 0),
        "U": (Fraction(3, 4), Fraction(-1, 2)),
        "d": (Fraction(3, 2), Fraction(1, 2)),
    }
    f = (1, 0)
    for func in reversed(string):
        f = compose(inverse[func], f)
    return f


def get_string(n):
    ret = ""
    while n > 1:
        if n % 3 == 0:
            n //= 3
            ret += "D"
        elif n % 3 == 1:
            n = (4 * n + 2) // 3
            ret += "U"
        else:
            n = (2 * n - 1) // 3
            ret += "d"
    return ret


def main():
    string = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
    N = 10 ** 15
    inv_func = get_inv_function(string)
    # Inverse function is of the form f(x) = (ax + b) / c
    a = inv_func[0]._numerator
    b = inv_func[1]._numerator
    c = inv_func[0]._denominator
    assert c == inv_func[1]._denominator

    # Lazy way to find first solution - could be sped up a lot
    for n in count(int((c * N - b) / a) + 1):
        if (a * n + b) % c == 0:
            print((a * n + b) // c)
            return


if __name__ == "__main__":
    main()
