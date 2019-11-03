from utils import get_primes_up_to_n


def main():
    primes = get_primes_up_to_n(10 ** 6)
    for i, p in enumerate(primes, 1):
        if i % 2 == 1 and (2 * i * p) % (p * p) > 10 ** 10:
            print(i)
            break


if __name__ == "__main__":
    main()
