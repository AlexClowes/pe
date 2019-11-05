import numpy as np


def f(x):
    return sum(x ** (2 * n) for n in range(6)) - sum(x ** (2 * n + 1) for n in range(5))


def main():
    deg = 10
    x = np.arange(1, deg + 2)
    y = f(x)

    total = 0
    for i in range(deg):
        total += np.polyval(np.polyfit(x[:i + 1], y[:i + 1], i), i + 2)
    print(int(round(total)))


if __name__ == "__main__":
    main()
