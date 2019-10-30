from itertools import combinations


# Replace 9s with 6s in set of square numbers
squares = {1, 4, 6, 16, 25, 36, 46, 64, 81}
def has_squares(d1, d2):
    concatenations = {c for n1 in d1 for n2 in d2 for c in (10 * n1 + n2, 10 * n2 + n1)}
    return squares <= concatenations


def main():
    dice = list(combinations((0, 1, 2, 3, 4, 5, 6, 7, 8, 6), 6))
    print(sum(has_squares(d1, d2) for d1 in dice for d2 in dice) // 2)


if __name__ == "__main__":
    main()
