import time
from utils import get_factors


def main():
    abundant_numbers = [n for n in range(1, 28123) if n < sum(get_factors(n)) - n]
    sums = {a + b for a in abundant_numbers for b in abundant_numbers}
    total = sum(n for n in range(1, 28123) if n not in sums)
    print(total)


if __name__ == "__main__":
    main()
