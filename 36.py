from utils import is_palindrome


def is_binary_palindrome(n):
    str_rep = "{0:b}".format(n)
    return str_rep == str_rep[::-1]


def main():
    total = sum(n for n in range(10**6) if is_palindrome(n) and is_binary_palindrome(n))
    print(total)


if __name__ == "__main__":
    main()
