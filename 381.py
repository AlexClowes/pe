from utils import get_primes_up_to_n


def S(p):
    inv_2 = pow(2, p - 2, p)
    inv_3 = pow(3, p - 2, p)
    return (-inv_2 + inv_2 * inv_3 - inv_2 ** 3 * inv_3) % p


def main():
    print(sum(S(p) for p in get_primes_up_to_n(10 ** 8) if p >= 5))


if __name__ == "__main__":
    main()
