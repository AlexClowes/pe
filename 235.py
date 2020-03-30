def find_root(f, low, high, eps=1e-12):
    mid = (low + high) / 2
    fmid = f(mid)
    while high - low > eps:
        if fmid > 0:
            low = mid
        else:
            high = mid
        mid = (low + high) / 2
        fmid = f(mid)
    return mid


def s(r, n):
    return (
        900 * (1 - r ** n) / (1 - r)
        - 3 * (1 - (n + 1) * r ** n + n * r ** (n + 1)) / (1 - r) ** 2
    )


def main():
    root = find_root(lambda r: s(r, 5000) + 6 * 10 ** 11, 1, 1.003)
    print(f"{root:.12f}")


if __name__ == "__main__":
    main()
