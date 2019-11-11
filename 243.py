from utils import get_prime_factors, prime_generator


def euler_totient(n):
    ret = n
    for p in set(get_prime_factors(n)):
        ret //= p
        ret *= p - 1
    return ret


def main():
    prod = 1
    a, b = 15499, 94744
    for p in prime_generator():
        prod *= p
        if b * euler_totient(prod) < a * (prod - 1):
            upper_bound = prod
            lower_bound = prod // p
            break
    for candidate in range(lower_bound, upper_bound + 1, lower_bound):
        if b * euler_totient(candidate) < a * (candidate - 1):
            print(candidate)
            break


if __name__ == "__main__":
    main()
