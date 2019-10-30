def main():
    N = 10 ** 6
    factor_sums = [0] * N
    for i in range(1, N):
        for j in range(2 * i, N, i):
            factor_sums[j] += i

    def cycle_length(n):
        prev_seen = set()
        fs = factor_sums[n]
        cycle_len = 0
        while True:
            cycle_len += 1
            if fs == n:
                return cycle_len
            if fs > 10 ** 6 or fs in prev_seen:
                return -1
            prev_seen.add(fs)
            fs = factor_sums[fs]

    print(max(range(1, N), key=cycle_length))


if __name__ == "__main__":
    main()
