from math import factorial


def digits(n):
    while n > 0:
        n, r = divmod(n, 10)
        yield r


def digit_factorial_chain(n):
    while True:
        yield n
        n = sum(factorial(d) for d in digits(n))


def cycle_length(n):
    cycle_len = 0
    previously_seen = set()
    for n in digit_factorial_chain(n):
        if n not in previously_seen:
            cycle_len += 1
            previously_seen.add(n)
        else:
            return cycle_len


def main():
    count = 0
    cycle_lens = {}
    for n in range(1, 10**6):
        sorted_n = "".join(map(str, sorted(digits(n))))
        if sorted_n not in cycle_lens:
            cycle_lens[sorted_n] = cycle_length(n)
        if cycle_lens[sorted_n] == 60:
            count += 1
    print(count)


if __name__ == "__main__":
    main()

