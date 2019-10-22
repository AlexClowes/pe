from collections import defaultdict
from itertools import combinations

from utils import get_primes_up_to_n


def concat(a, b):
    return int(str(a) + str(b))


def main():
    # Guess biggest prime we want to check
    N = 10 ** 4
    primes = list(get_primes_up_to_n(N))

    # Build dict to know which pairs of primes work
    prime_checking_set = set(get_primes_up_to_n(N**2))
    prime_concat_dict = defaultdict(set)
    for p, q in combinations(primes, 2):
        if concat(p, q) in prime_checking_set and concat(q, p) in prime_checking_set:
            prime_concat_dict[p].add(q)
            prime_concat_dict[q].add(p)

    # Choose primes from dict and look for minimum sum
    min_sum = 4 * N
    for p1 in primes:
        i2 = prime_concat_dict[p1]
        for p2 in i2:
            i3 = i2 & prime_concat_dict[p2]
            for p3 in i3:
                i4 = i3 & prime_concat_dict[p3]
                for p4 in i4:
                    i5 = i4 & prime_concat_dict[p4]
                    for p5 in i5:
                        total = p1 + p2 + p3 + p4 + p5
                        if total < min_sum:
                            min_sum = total
    print(min_sum)


if __name__ == "__main__":
    main()
