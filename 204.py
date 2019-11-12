from utils import get_primes_up_to_n


def main():
    N = 10 ** 9
    primes = list(get_primes_up_to_n(100))

    hamming_nos = {1}
    for p in primes:
        for x in set(hamming_nos):
            prod = x * p
            while prod <= N:
                hamming_nos.add(prod)
                prod *= p
    print(len(hamming_nos))


if __name__ == "__main__":
    main()
