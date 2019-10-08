from itertools import permutations

from utils import get_primes_up_to_n


def get_perms(n):
    return (int("".join(perm)) for perm in permutations(str(n)))


def main():
    primes = set(get_primes_up_to_n(10**4)) - set(get_primes_up_to_n(10**3))
    for p in primes:
        prime_perms = set(get_perms(p)) & primes
        primes = primes - prime_perms
        prime_perms = sorted(prime_perms)
        for i in range(len(prime_perms)):
            pi = prime_perms[i]
            for j in range(i + 1, len(prime_perms)):
                pj = prime_perms[j]
                if 2 * pj - pi in prime_perms:
                    print(pi, pj, 2 * pj - pi, sep="")


if __name__ == "__main__":
    main()
