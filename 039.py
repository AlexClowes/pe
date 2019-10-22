def get_triple_count(p):
    count = 0
    for b in range(1, p // 2):
        a, r = divmod(p * (p - 2 * b), 2 * (p - b))
        if r == 0 and 0 < a < b:
            count += 1
    return count


def main():
    best_count = 0
    for p in range(1, 1001):
        count = get_triple_count(p)
        if count > best_count:
            best_count = count
            best_p = p
    print(best_p)


if __name__ == "__main__":
    main()
