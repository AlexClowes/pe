from utils import get_primes_up_to_n


def main():
    N = 5 * 10 ** 7
    primes = list(get_primes_up_to_n(N))
    print(sum((p % 4 == 3) + (p * 4 < N) + (p * 16 < N) for p in primes))


if __name__ == "__main__":
    main()
