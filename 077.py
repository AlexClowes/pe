from utils import get_primes_up_to_n


def recurse(n, vals):
    if not vals:
        return int(n == 0)
    return sum(recurse(n - k, vals[:-1]) for k in range(0, n + 1, vals[-1]))


def main():
    primes = [2]
    for n in range(2, 100):
        if n > primes[-1]:
            primes = list(get_primes_up_to_n(n))
        if recurse(n, primes) > 5000:
            break
    print(n)


if __name__ == "__main__":
    main()
