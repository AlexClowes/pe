from utils import get_primes_up_to_n


def main():
    upper_lim = 10 ** 8
    primes = list(get_primes_up_to_n(upper_lim // 2))
    count = 0
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            if primes[i] * primes[j] < upper_lim:
                count += 1
            else:
                break
    print(count)


if __name__ == "__main__":
    main()
