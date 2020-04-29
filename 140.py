def gen_n(k, m):
    while True:
        if k > 7 and k % 5 == 2:
            yield (k - 7) // 5
        k, m = 9 * k + 20 * m, 4 * k + 9 * m


def main():
    sols = set()
    for k, m in ((7, 1), (8, 2), (13, 5), (17, 7), (32, 14), (43, 19)):
        for n in gen_n(k, m):
            if len(sols) >= 30 and n > max(sols):
                break
            sols.add(n)
    print(sum(sorted(sols)[:30]))


if __name__ == "__main__":
    main()
