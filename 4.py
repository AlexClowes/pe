from utils import is_palindrome


def main():
    best_result = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            prod = i * j
            if prod > best_result and is_palindrome(prod):
                best_result = prod
    print(best_result)


if __name__ == "__main__":
    main()
