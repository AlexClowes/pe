import itertools


def is_palindrome(n):
    str_rep = str(n)
    return str_rep == str_rep[::-1]


def get_prime_factors(n):
    prime_factors = []
    k = 2
    while k * k <= n:
        if n % k == 0:
            n = n // k
            prime_factors.append(k)
        else:
            k += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors


def get_first_n_primes(n):
    primes = [2]
    test_num = 3
    while len(primes) < n:
        for p in primes:
            if test_num % p == 0:
                break
        else:
            primes.append(test_num)
        test_num += 2
    return primes


def get_primes_up_to_n(n):
    # Sieve of eratosthenes
    candidates = range(2, n+1)
    is_prime = [True] * len(candidates)
    for pos, val in enumerate(candidates):
        # If val is prime, then all its multiples are not prime
        if is_prime[pos]:
            mult_pos = pos + val
            while mult_pos < len(candidates):
                is_prime[mult_pos] = False
                mult_pos += val
    return itertools.compress(candidates, is_prime)
