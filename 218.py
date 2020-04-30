def brute_force():
    """Check all perfect triangles. Not actually necessary."""
    c_max = 10 ** 16
    total = 0
    for x in range(1, int(c_max ** 0.25)):
        y_max = min(x, int((c_max ** 0.5 - x * x) ** 0.5))
        for y in range(1, y_max):
            m = x * x - y * y
            n = 2 * x * y
            area = m * n * abs(m * m - n * n)
            if area % 84 != 0:
                total += 1
    print(total)


def main():
    # Verify that no solution exists
    for x in range(84):
        for y in range(84):
            m = x * x - y * y
            n = 2 * x * y
            area = m * n * abs(m * m - n * n)
            assert area % 84 == 0
    print(0)


if __name__ == "__main__":
    main()
