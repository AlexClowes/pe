from numba import njit


@njit
def ends_in_89(n):
    while n != 1 and n != 89:
        digit_square_sum = 0
        while n > 0:
            n, r = divmod(n, 10)
            digit_square_sum += r * r
        n = digit_square_sum
    return n == 89


@njit
def main():
    count = 0
    for n in range(1, 10 ** 7):
        count += ends_in_89(n)
    print(count)


if __name__ == "__main__":
    main()
