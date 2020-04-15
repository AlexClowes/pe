from utils import get_primes_up_to_n


def fact_padic_val(n, p):
    div = p
    exp = 0
    while div <= n:
        exp += n // div
        div *= p
    return exp


def bin_padic_val(n, r, p):
    return fact_padic_val(n, p) - fact_padic_val(r, p) - fact_padic_val(n - r, p)


def bin_sum_primes(n, r):
    primes = get_primes_up_to_n(n)
    return sum(p * bin_padic_val(n, r, p) for p in primes)


def main():
    print(bin_sum_primes(2 * 10 ** 7, 15 * 10 ** 6))


if __name__ == "__main__":
    main()
