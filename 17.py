from num2words import num2words


def num_world_len(n):
    word_rep = num2words(n)
    length = len(word_rep)
    n_space_or_hypens = sum(c in " -" for c in word_rep)
    return length - n_space_or_hypens


def main():
    print(sum(map(num_world_len, range(1, 1001))))


if __name__ == "__main__":
    main()
