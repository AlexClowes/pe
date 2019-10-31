def gen_digits(n):
    while n > 0:
        yield n % 10
        n //= 10


def is_decreasing(n):
    digits = gen_digits(n)
    d_last = next(digits)
    for d in digits:
        if d < d_last:
            return False
        d_last = d
    return True


def is_increasing(n):
    digits = gen_digits(n)
    d_last = next(digits)
    for d in digits:
        if d > d_last:
            return False
        d_last = d
    return True


def is_bouncy(n):
    return not is_increasing(n) and not is_decreasing(n)


def main():
    bouncy_count = 0
    n = 1
    while True:
        bouncy_count += is_bouncy(n)
        if bouncy_count / n >= 0.99:
            break
        n += 1
    print(n)


if __name__ == "__main__":
    main()
