from utils import get_prime_factors


def euler_totient(n):
    prime_factors = set(get_prime_factors(n))
    prod = n
    for p in prime_factors:
        prod *= (p - 1)
        prod //= p
    return prod


def main():
    best_ratio = 0
    for n in range(2, 10**6 + 1):
        ratio = n / euler_totient(n)
        if ratio > best_ratio:
            best_ratio = ratio
            best_n = n
    print(best_n)


if __name__ == "__main__":
    main()
