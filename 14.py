import functools


@functools.lru_cache(maxsize=None)
def collatz_length(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return collatz_length(n // 2) + 1
    else:
        return collatz_length(3 * n + 1) + 1


def main():
    best_length = 0
    for i in range(1, 10**6):
        length = collatz_length(i)
        if best_length < length:
            best_length = length
            print(i, length)


if __name__ == "__main__":
    main()
