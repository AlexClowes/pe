import time


def main():
    for b in range(1, 1000):
        q, r = divmod(500000 - 1000 * b, 1000 - b)
        if r == 0 and 0 < q < b:
            a = q
            c = 1000 - a - b
            print(a * b * c)


if __name__ == "__main__":
    main()
