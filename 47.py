from utils import get_prime_factors


def main():
    target = 4
    candidate = 0
    consecutive_successes = 0
    while consecutive_successes < target:
        candidate += 1
        if len(set(get_prime_factors(candidate))) == target:
            consecutive_successes += 1
        else:
            consecutive_successes = 0
    print(*[candidate - i for i in range(target)][::-1])


if __name__ == "__main__":
    main()
