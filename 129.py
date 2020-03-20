from itertools import count

from utils import gcd


def A(n):
    mod = 9 * n
    k = 1
    pow10 = 10 % mod
    while pow10 != 1:
        k += 1
        pow10 = (pow10 * 10) % mod
    return k


def main():
    N = 10 ** 6
    for n in count(N):
        if gcd(10, n) == 1 and A(n) > N:
            break
    print(n)


if __name__ == "__main__":
    main()
