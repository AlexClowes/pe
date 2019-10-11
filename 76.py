memo = {}
def p(k, n):
    if k > n:
        return 0
    if k == 0:
        return 0
    if k == n:
        return 1
    if (k, n) not in memo:
        memo[(k, n)] = p(k - 1, n - 1) + p(k, n - k)
    return memo[(k, n)]


def partitions(n):
    return sum(p(k, n) for k in range(1, n+1))


def main():
    print(partitions(100) - 1)


if __name__ == "__main__":
    main()
