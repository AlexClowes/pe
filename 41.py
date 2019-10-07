from utils import is_prime


def is_pandigital(n):
    str_rep = str(n)
    return sorted(map(int, str_rep)) == list(range(1, len(str_rep) + 1))


def main():
    primes = (n for n in range(7654321, 0, -1) if is_prime(n))
    for p in primes:
        if is_pandigital(p):
            print(p)
            break


if __name__ == "__main__":
    main()
