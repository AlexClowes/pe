def main():
    pent_nums = {n * (3 * n - 1) // 2 for n in range(1, 10**4)}
    for a in pent_nums:
        for b in pent_nums:
            if a + b in pent_nums and a - b in pent_nums:
                print(a - b)


if __name__ == "__main__":
    main()
