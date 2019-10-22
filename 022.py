def score_name(name, pos):
    score = 0
    for char in name:
        score += ord(char) - ord("A") + 1
    return score * pos


def main():
    with open("data/p022_names.txt") as f:
        data = f.read()
    data = data.split(",")
    data = [name[1:-1] for name in data]
    data.sort()

    total = sum(score_name(name, pos) for pos, name in enumerate(data, 1))
    print(total)


if __name__ == "__main__":
    main()
