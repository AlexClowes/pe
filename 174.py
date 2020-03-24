from numba import njit


@njit
def L(t):
    n = t // 4
    count = 0
    k = 1
    while k * k < n:
        if n % k == 0:
            count += 1
        k += 1
    return count


@njit
def main():
    t_max = 10 ** 6
    total = 0
    for t in range(4, t_max + 4, 4):
        if 1 <= L(t) <= 10:
            total += 1
    print(total)


if __name__ == "__main__":
    main()
