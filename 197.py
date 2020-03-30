def f(x):
    return int(2 ** (30.403243784 - x * x)) * 1e-9


def main():
    u1, u2 = 0, -1
    last_sum = 0
    while u1 + u2 != last_sum:
        last_sum = u1 + u2
        u1, u2 = u2, f(u2)
    print(last_sum)


if __name__ == "__main__":
    main()
