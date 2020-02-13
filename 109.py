def score(*throws):
    return sum(a * b for a, b in throws)


def n_checkouts(n):
    count = 0
    legal_throws = (
        [(val, mul) for val in range(1, 21) for mul in range(1, 4)]
        + [(0, 0), (25, 1), (25, 2)]
    )
    for throw1 in legal_throws:
        if throw1[1] != 2 or throw1[0] * 2 > n:
            continue
        for i in range(len(legal_throws)):
            throw2 = legal_throws[i]
            for j in range(i, len(legal_throws)):
                throw3 = legal_throws[j]
                if score(throw1, throw2, throw3) < n:
                    count += 1
    return count


def main():
    print(n_checkouts(100))


if __name__ == "__main__":
    main()
