from utils import get_primes_up_to_n


def main():
    primes = list(get_primes_up_to_n(10**6))
    primes_set = set(primes)

    prime_sum = 0
    max_sum_len = 0
    while prime_sum < primes[-1]:
        prime_sum += primes[max_sum_len]
        max_sum_len += 1

    for sum_len in range(max_sum_len, 1, -1):
        prime_sum = sum(primes[:sum_len])
        pos = 0
        while pos < len(primes) - sum_len and prime_sum < primes[-1]:
            if prime_sum in primes_set:
                print(prime_sum)
                return
            prime_sum += primes[pos + sum_len] - primes[pos]
            pos += 1

if __name__ == "__main__":
    main()
