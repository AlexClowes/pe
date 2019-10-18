from collections import defaultdict

from utils import get_factors


fs_memo = {}
def factor_sum(n):
    if n not in fs_memo:
        fs_memo[n] = sum(get_factors(n)) - n
    return fs_memo[n]


cl_memo = {}
def cycle_length(n):
    if n not in cl_memo:
        prev_seen = set()
        fs = factor_sum(n)
        cycle_len = 0
        while True:
            cycle_len += 1
            if fs == n:
                cl_memo[n] = cycle_len
                break
            elif fs > 10 ** 6 or fs in prev_seen:
                cl_memo[n] = -1
                break
            prev_seen.add(fs)
            fs = factor_sum(fs)
    return cl_memo[n]


def main():
    longest_chain = 0
    for n in range(1, 10 ** 6):
        cl = cycle_length(n)
        if cl > longest_chain:
            best_n, longest_chain = n, cl
    print(best_n)


if __name__ == "__main__":
    main()
