from utils import get_primes_up_to_n


def main():
    primes = list(get_primes_up_to_n(10**6))
    primes_set = set(primes)
    for sum_len in range(2, len(primes) + 1):
        prime_sum = sum(primes[:sum_len])
        pos = 0
        while pos < len(primes) - sum_len and prime_sum < primes[-1]:
            if prime_sum in primes_set:
                best_prime = prime_sum
                best_len = sum_len
                break
            prime_sum += primes[pos + sum_len] - primes[pos]
            pos += 1
    print(best_prime)


if __name__ == "__main__":
    main()



