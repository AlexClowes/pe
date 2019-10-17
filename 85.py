def rectangle_count(h, w):
    return h * (h + 1) * w * (w + 1) // 4


def main():
    smallest_diff = 2 * 10 ** 6
    for h in range(1, 2001):
        for w in range(1, 2001):
            diff = abs(rectangle_count(h, w) - 2 * 10 ** 6)
            if diff < smallest_diff:
                smallest_diff = diff
                best_area = h * w
    print(best_area)


if __name__ == "__main__":
    main()

