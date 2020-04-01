from math import e, floor, log

from utils import gcd


def D(N):
    k = floor(N / e)
    if k * log(N / k) < (k + 1) * log(N / (k + 1)):
        k += 1
    k //= gcd(N, k)
    while k % 2 == 0:
        k //= 2
    while k % 5 == 0:
        k //= 5
    if k == 1:
        return -N
    return N


def main():
    print(sum(D(N) for N in range(5, 10 ** 4 + 1)))


if __name__ == "__main__":
    main()
