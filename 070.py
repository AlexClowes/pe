from utils import get_primes_up_to_n


#Commented out code is slow but much more readable

#def euler_totient(n):
#    unique_prime_factors = set(get_prime_factors(n))
#    ret = n
#    for p in unique_prime_factors:
#        ret *= (p - 1)
#        ret //= p
#    return ret
#
#
#primes = list(get_primes_up_to_n(10**7))
#def get_prime_factors(n):
#    prime_factors = set()
#    pos = 0
#    k = primes[pos]
#    while k * k <= n:
#        if n % k == 0:
#            n = n // k
#            prime_factors.add(k)
#        else:
#            pos += 1
#            k = primes[pos]
#    if n > 1:
#        prime_factors.add(n)
#    return prime_factors
#
#
#def main():
#    min_ratio = 10**7
#    for n in trange(2, 10**7):
#        et = euler_totient(n)
#        if sorted(str(et)) == sorted(str(n)):
#            if n / et < min_ratio:
#                min_ratio = n / et
#                best_n = n
#    print(best_n)


def main():
    primes = list(get_primes_up_to_n(10**7))
    primes_set = set(primes)
    min_ratio = 10 ** 7
    for n in range(2, 10**7):
        if n in primes_set:
            continue
        et = n
        n_copy = n
        early_exit = False
        for p in primes:
            if p * p > n_copy:
                break
            if n_copy % p == 0:
                et *= p - 1
                et //= p
                if n / et > min_ratio:
                    early_exit = True
                    break
                while n_copy % p == 0:
                    n_copy //= p
        if early_exit:
            continue
        if n_copy > 1:
            et *= n_copy - 1
            et //= n_copy
        if n / et < min_ratio and sorted(str(et)) == sorted(str(n)):
            min_ratio = n / et
            best_n = n
    print(best_n)


if __name__ == "__main__":
    main()
