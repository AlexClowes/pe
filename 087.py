from utils import get_primes_up_to_n

from math import ceil, sqrt


def main():
    N = 50 * 10 ** 6
    primes = list(get_primes_up_to_n(ceil(sqrt(N))))
    prime_2 = [p ** 2 for p in primes]
    prime_3 = [p ** 3 for p in primes]
    prime_4 = [p ** 4 for p in primes]
    is_sum = [False] * N
    for a in prime_2:
        for b in prime_3:
            if a + b > N:
                break
            for c in prime_4:
                if a + b + c > N:
                    break
                is_sum[a + b + c - 1] = True
    print(sum(is_sum))


if __name__ == "__main__":
    main()


