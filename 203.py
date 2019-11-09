from itertools import islice


def pascal_gen():
    last_row = [1]
    yield from last_row
    while True:
        new_row = [1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row.append(1)
        yield from new_row
        last_row = new_row


def is_square_free(n):
    k = 2
    while k * k <= n:
        if n % k == 0:
            n = n // k
        if n % k == 0:
            return False
        k += 1
    return True


def main():
    n_rows = 51
    bin_coefs = set(islice(pascal_gen(), n_rows * (n_rows + 1) // 2))
    print(sum(n for n in bin_coefs if is_square_free(n)))


if __name__ == "__main__":
    main()
