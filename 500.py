import heapq

from utils import get_primes_up_to_n


MOD = 500500507


def smallest_with_2n_divisors(n):
    primes = get_primes_up_to_n(10 ** 7)
    prod = 1
    max_prime = next(primes)
    heap = [max_prime]
    for _ in range(n):
        next_term = heapq.heappop(heap)
        heapq.heappush(heap, next_term * next_term)
        if next_term == max_prime:
            max_prime = next(primes)
            heapq.heappush(heap, max_prime)
        prod *= next_term
        prod %= MOD
    return prod


def main():
    print(smallest_with_2n_divisors(500500))


if __name__ == "__main__":
    main()
