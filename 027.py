from utils import is_prime


def main():
    most_successive_primes = 0
    for a in range(-999, 1000):
        for b in range(2, 1001):
            if not is_prime(b):
                continue
            quad = lambda x: x * x + a * x + b
            n = 0
            successive_primes = 0
            while is_prime(quad(n)):
                successive_primes += 1
                n += 1
            if most_successive_primes < successive_primes:
                most_successive_primes = successive_primes
                best_a = a
                best_b = b
    print(best_a * best_b)


if __name__ == "__main__":
    main()
