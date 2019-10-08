def digit_sum(n):
    return sum(map(int, str(n)))


def main():
    best_sum = 0
    for a in range(100):
        for b in range(100):
            if digit_sum(a ** b) > best_sum:
                best_sum = digit_sum(a ** b)
    print(best_sum)


if __name__ == "__main__":
    main()
