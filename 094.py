def gen_pell_sols():
    # Solutions to Pell equation x^2 - 3y^2 = 1
    x, y = 2, 1
    while True:
        yield x, y
        x, y = 2 * x + 3 * y, x + 2 * y


def main():
    N = 10 ** 9
    perim_sum = 0
    for x, y in gen_pell_sols():
        a = x * x + y * y
        perim_pos = 3 * a + 1
        if perim_pos <= N:
            perim_sum += perim_pos
        a = (x + 2 * y) ** 2 + y * y
        perim_neg = 3 * a - 1
        if perim_neg <= N:
            perim_sum += perim_neg
        if perim_pos > N and perim_neg > N:
            break
    print(perim_sum)


if __name__ == "__main__":
    main()
