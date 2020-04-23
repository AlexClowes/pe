def tri(n):
    return n * (n + 1) // 2


def f(n):
    if n <= 1:
        return n
    pow7 = 1
    while pow7 * 7 < n:
        pow7 *= 7
    q, r = divmod(n, pow7)
    return tri(q) * f(pow7) + (q + 1) * f(r)


def main():
    print(f(10 ** 9))


if __name__ == "__main__":
    main()
