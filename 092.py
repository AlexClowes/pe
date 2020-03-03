from numba import njit


@njit
def ends_in_89(n):
    if n == 1:
        return False
    if n == 89:
        return True
    digit_square_sum = 0
    while n > 0:
        n, r = divmod(n, 10)
        digit_square_sum += r * r
    return ends_in_89(digit_square_sum)


def main():
    print(sum(ends_in_89(n) for n in range(1, 10**7)))


if __name__ == "__main__":
    main()
