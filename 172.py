from functools import lru_cache


@lru_cache(maxsize=None)
def f(n, *digits):
    if n == 0:
        return 1
    ret = 0
    for i, d in enumerate(digits):
        if d > 0:
            ret += f(n - 1, *digits[:i], d - 1, *digits[i + 1 :])
    return ret


def main():
    digits = (3,) * 10
    print(
        sum(
            f(17, *digits[:i], d - 1, *digits[i + 1 :])
            for i, d in enumerate(digits[:-1])
        )
    )


if __name__ == "__main__":
    main()
