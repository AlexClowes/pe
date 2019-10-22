from utils import get_primes_up_to_n


def cycle_number_gen(n):
    digits = list(str(n))
    for i in range(len(digits)):
        yield int("".join(digits[i:]) + "".join(digits[:i]))


def main():
    primes = set(get_primes_up_to_n(10**6))
    count = 2 # Count 2 and 5, excluded by checks below
    for n in range(1, 10**6):
        if any((d % 2 == 0 or d == 5) for d in map(int, str(n))):
            continue
        if all(c in primes for c in cycle_number_gen(n)):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
