from utils import get_primes_up_to_n


def M(p, q, N):
    prod = p * q
    p_exp = 1
    while prod * p <= N:
        prod *= p
        p_exp += 1

    best = prod
    while p_exp > 1:
        prod //= p
        p_exp -= 1
        while prod * q <= N:
            prod *= q
        best = max(best, prod)

    return best


def S(N):
    primes = list(get_primes_up_to_n(N // 2))
    total = 0
    for i in range(len(primes)):
        p = primes[i]
        if p * p > N:
            break
        for j in range(i + 1, len(primes)):
            q = primes[j]
            if p * q > N:
                break
            total += M(p, q, N)
    return total


def main():
    print(S(10 ** 7))


if __name__ == "__main__":
    main()
