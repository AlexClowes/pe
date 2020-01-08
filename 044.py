def main():
    pent_list = [n * (3 * n - 1) // 2 for n in range(1, 10 ** 4)]
    pent_set = set(pent_list)
    for i, a in enumerate(pent_list):
        for b in pent_list[:i]:
            if a + b in pent_set and a - b in pent_set:
                print(a - b)
                return


if __name__ == "__main__":
    main()
