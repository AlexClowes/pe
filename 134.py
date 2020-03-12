from utils import get_primes_up_to_n


def f(p1, p2):
    # Smallest power of 10 greater than p1
    pow10 = 10
    while pow10 < p1:
        pow10 *= 10

    # Extended Euclidean algorithm
    t1, t2 = 0, 1
    r1, r2 = pow10, p2
    while r2 != 1:
        q = r1 // r2
        r1, r2 = r2, r1 - q * r2
        t1, t2 = t2, t1 - q * t2
    return (t2 * p1 * p2) % (p2 * pow10)


def main():
    primes = list(get_primes_up_to_n(10 ** 6 + 3))
    print(sum(f(p1, p2) for p1, p2 in zip(primes[2:], primes[3:])))


if __name__ == "__main__":
    main()
