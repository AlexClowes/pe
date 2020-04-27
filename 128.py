from itertools import count

from utils import is_prime


def main():
    target = 2000
    total = 2  # 1, 2 are special cases
    for n in count(2):
        if is_prime(6 * n - 1):
            if is_prime(6 * n + 1) and is_prime(12 * n + 5):
                total += 1
                if total == target:
                    print(3 * n * (n - 1) + 2)
                    break
            if is_prime(6 * n + 5) and is_prime(12 * n - 7):
                total += 1
                if total == target:
                    print(3 * n * (n + 1) + 1)
                    break


if __name__ == "__main__":
    main()
