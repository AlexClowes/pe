from functools import lru_cache


def f(*sheets):
    n_sheets = sum(sheets)
    if n_sheets == sheets[-1]:
        return 0
    ret = int(n_sheets == 1)
    for i, s in enumerate(sheets):
        if s > 0:
            new_sheets = *sheets[:i], s - 1, *(s + 1 for s in sheets[i+1:])
            ret += (s / n_sheets) * f(*new_sheets)
    return ret


def main():
    print(f"{f(1, 1, 1, 1):.6}")


if __name__ == "__main__":
    main()
