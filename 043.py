from itertools import permutations


def get_substring_integers(n):
    for i in range(1, 8):
        yield 100 * n[i] + 10 * n[i + 1] + n[i + 2]


def main():
    pandigital_numbers = (perm for perm in permutations(range(10)) if perm[0] != 0)
    primes = [2, 3, 5, 7, 11, 13, 17]
    total = 0
    for n in pandigital_numbers:
        for s, p in zip(get_substring_integers(n), primes):
            if s % p != 0:
                break
        else:
            total += int("".join(map(str, n)))
    print(total)


if __name__ == "__main__":
    main()
