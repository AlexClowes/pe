from utils import get_factors


def main():
    factor_sums = {n: sum(get_factors(n)) - n for n in range(1, 10000)}
    total = 0
    for n, s in factor_sums.items():
        if n != s and s in factor_sums and factor_sums[s] == n:
            total += n
    print(total)


if __name__ == "__main__":
    main()
