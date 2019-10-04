def get_repetend_length(d):
    first_pos = {}
    x = 1
    pos = 0
    while x not in first_pos:
        first_pos[x] = pos
        pos += 1
        x = (x * 10) % d
    return pos - first_pos[x]


def main():
    best_d = -1
    best_repetend_length = 0
    for d in range(1, 1000):
        repetend_length = get_repetend_length(d)
        if repetend_length > best_repetend_length:
            best_repetend_length = repetend_length
            best_d = d
    print(best_d)


if __name__ == "__main__":
    main()
