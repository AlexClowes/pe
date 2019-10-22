from utils import get_primes_up_to_n


def main():
    N = 10 ** 6
    primes = list(get_primes_up_to_n(N))
    def euler_totient(n):
        ret = n
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                ret *= (p - 1)
                ret //= p
                while n % p == 0:
                    n //= p
        if n > 1:
            ret *= (n - 1)
            ret //= n
        return ret

    print(sum(euler_totient(r) for r in range(1, N + 1)) - 1)


if __name__ == "__main__":
    main()
