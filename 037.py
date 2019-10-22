from utils import get_primes_up_to_n


def gen_truncations(n):
    str_rep = str(n)
    yield from (int(str_rep[i:]) for i in range(len(str_rep)))
    yield from (int(str_rep[:i]) for i in range(1, len(str_rep)))


def main():
    primes = set(get_primes_up_to_n(10**6))
    total = 0
    for p in primes:
        if p > 10 and all(t in primes for t in gen_truncations(p)):
            total += p
    print(total)


if __name__ == "__main__":
    main()
