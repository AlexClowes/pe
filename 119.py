def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def main():
    max_n_digits = 15
    upper_bound = 10 ** max_n_digits
    sequence = []
    for d_sum in range(2, 9 * max_n_digits + 1):
        d_sum_power = d_sum
        while d_sum_power < upper_bound:
            if d_sum_power >= 10 and sum_digits(d_sum_power) == d_sum:
                sequence.append(d_sum_power)
            d_sum_power *= d_sum
    print(sorted(sequence)[29])


if __name__ == "__main__":
    main()
