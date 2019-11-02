from math import floor, sqrt

from utils import is_palindrome


def main():
    N = 10 ** 8
    squares = [n * n for n in range(1, int(sqrt(N)))]

    palindromes = set()
    for i in range(len(squares) - 1):
        s = squares[i]
        for j in range(i + 1, len(squares)):
            s += squares[j]
            if s >= N:
                break
            if is_palindrome(s):
                palindromes.add(s)
    print(sum(palindromes))


if __name__ == "__main__":
    main()
