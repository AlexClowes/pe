memo = {}
def ends_in_89(n):
    if n == 1:
        return False
    if n == 89:
        return True
    if n not in memo:
        digit_square_sum = 0
        n_copy = n
        while n_copy > 0:
            r = n_copy % 10
            digit_square_sum += r * r
            n_copy //= 10
        memo[n] = ends_in_89(digit_square_sum)
    return memo[n]


def main():
    print(sum(ends_in_89(n) for n in range(1, 10**7)))


if __name__ == "__main__":
    main()
