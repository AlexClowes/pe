from collections import deque

from utils import is_prime


def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def is_harshad(n):
    return n % sum_digits(n) == 0


def is_strong(n):
    return is_prime(n / sum_digits(n))


def gen_rt_harshads():
    h_queue = deque(range(1, 10))
    for n in iter(h_queue.popleft, None):
        yield n
        for candidate in range(10 * n, 10 * n + 10):
            if is_harshad(candidate):
                h_queue.append(candidate)


def strong_rt_harshad_primes():
    for h in filter(is_strong, gen_rt_harshads()):
        yield from filter(is_prime, range(10 * h + 1, 10 * h + 10, 2))


def main():
    total = 0
    for p in strong_rt_harshad_primes():
        if p > 10 ** 14:
            break
        total += p
    print(total)


if __name__ == "__main__":
    main()
