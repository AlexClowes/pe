import numpy as np


def main():
    N = 10 ** 5
    rad = np.ones(N + 1)
    for n in range(2, N + 1):
        if rad[n] == 1:
            rad[n::n] *= n

    k = 10 ** 4
    e = sorted(range(N + 1), key=lambda n: (rad[n], n))
    print(e[k])


if __name__ == "__main__":
    main()
