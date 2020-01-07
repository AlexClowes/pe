from collections import Counter
from itertools import combinations, permutations
from math import floor, sqrt


def get_words():
    with open("data/p098_words.txt") as f:
        return [word.strip("\"") for word in f.read().split(",")]


def word_2_int(word, mapping):
    ret = 0
    for char in word:
        ret *= 10
        ret += mapping[char]
    return ret


def main():
    sorted_words = {word: sorted(word) for word in get_words()}
    anagram_pairs = [
        (w1, w2) for w1, w2 in combinations(sorted_words.keys(), 2)
        if sorted_words[w1] == sorted_words[w2]
    ]
    max_word_len = max(len(w1) for w1, w2 in anagram_pairs)
    squares = {n * n for n in range(10 ** (max_word_len // 2))}
    biggest_square = 0
    for w1, w2 in anagram_pairs:
        uniq_chars = set(w1)
        for digits in permutations(range(10), len(uniq_chars)):
            char_digit_mapping = dict(zip(uniq_chars, digits))
            # No leading zeros, last digit can't be 2, 3, 7, or 8
            if (
                char_digit_mapping[w1[0]] == 0
                or char_digit_mapping[w2[0]] == 0
                or char_digit_mapping[w1[-1]] in {2, 3, 7, 8}
                or char_digit_mapping[w2[-1]] in {2, 3, 7, 8}
            ):
                continue
            n1 = word_2_int(w1, char_digit_mapping)
            if n1 not in squares:
                continue
            n2 = word_2_int(w2, char_digit_mapping)
            if n2 in squares:
                biggest_square = max(n1, n2, biggest_square)
    print(biggest_square)


if __name__ == "__main__":
    main()
