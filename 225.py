from itertools import count
from numba import njit


@njit
def is_tribonacci_divisor(n):
    a, b, c = 1, 1, 1
    while True:
        a, b, c = b, c, (a + b + c) % n
        if c == 0:
            return True
        if a == b == c == 1:
            return False


def main():
    total = 0
    for n in count(1, 2):
        if not is_tribonacci_divisor(n):
            total += 1
            if total == 124:
                print(n)
                break


if __name__ == "__main__":
    main()
