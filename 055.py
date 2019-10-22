from utils import is_palindrome


def reverse_add(n):
    return n + int(str(n)[::-1])


def is_lychrel(n):
    counter = 0
    while counter < 50:
        n = reverse_add(n)
        if is_palindrome(n):
            return False
        counter += 1
    return True


def main():
    print(sum(map(is_lychrel, range(1, 10000))))


if __name__ == "__main__":
    main()
