from numba import njit
import numpy as np


@njit
def s_arr():
    s = np.zeros(4 * 10 ** 6, dtype=np.int32)
    for k in range(1, 56):
        s[k - 1] = (100003 - 200003 * k + 300007 * k ** 3) % (10 ** 6) - 5 * 10 ** 5
    for k in range(56, 4 * 10 ** 6 + 1):
        s[k - 1] = (s[k - 25] + s[k - 56] + 10 ** 6) % (10 ** 6) - 5 * 10 ** 5
    return s.reshape(2000, 2000)


@njit
def max_subarray(arr):
    best_sum = 0
    current_sum = 0
    for x in arr:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum


def get_diags(arr):
    for offset in range(1 - arr.shape[0], arr.shape[1]):
        yield np.diag(arr, offset)


def max_subseq_sum(arr):
    # Horizontals
    best_sum = max(max_subarray(row) for row in arr)
    # Verticals
    best_sum = max(best_sum, max(max_subarray(col) for col in arr.T))
    # Diagonals
    best_sum = max(best_sum, max(max_subarray(diag) for diag in get_diags(arr)))
    # Anti-diagonals
    best_sum = max(best_sum, max(max_subarray(adiag) for adiag in get_diags(np.fliplr(arr))))
    return best_sum


def main():
    print(max_subseq_sum(s_arr()))


if __name__ == "__main__":
    main()
