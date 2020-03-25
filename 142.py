from itertools import count


def main():
    squares = set()
    for a in count(1):
        a2 = a * a
        squares.add(a2)
        for b in range(2 - a % 2, a, 2):
            b2 = b * b
            c_min = max(b + 1, int(((a2 + b2) / 2) ** 0.5) + 1)
            for c in range(c_min, a):
                c2 = c * c
                if c2 - b2 in squares and a2 - c2 in squares and a2 + b2 - c2 in squares:
                    x = (a2 + b2) // 2
                    y = (a2 - b2) // 2
                    z = c2 - (a2 + b2) // 2
                    print(x + y + z)
                    return


if __name__ == "__main__":
    main()
