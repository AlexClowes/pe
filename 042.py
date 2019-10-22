def word_value(word):
    return sum(ord(char) - ord("A") + 1 for char in word)


def main():
    with open("data/p042_words.txt") as f:
        words = f.read()
    words = [word[1:-1] for word in words.split(",")]

    triangle_numbers = {n * (n + 1) // 2 for n in range(1, 100)}

    print(sum(word_value(word) in triangle_numbers for word in words))


if __name__ == "__main__":
    main()
