from utils import is_prime


def prime_count(n):
    """Get number of primes on nth layer"""
    numbers = [(2 * n + 1) ** 2 - 2 * n * i for i in range(1, 4)]
    return sum(map(is_prime, numbers))


def main():
    total_primes = 0
    layer = 1
    while True:
        total_primes += prime_count(layer)
        if total_primes / (4 * layer + 1) < 0.1:
            print(2 * layer + 1)
            break
        layer += 1


if __name__ == "__main__":
    main()
