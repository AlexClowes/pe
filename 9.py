import time


def main():
    start = time.time()
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print(a, b, c)
                print(a * b * c)
    print(time.time() - start)

    start = time.time()
    for b in range(1, 1000):
        q, r = divmod(500000 - 1000 * b, 1000 - b)
        if r == 0 and 0 < q < b:
            a = q
            c = 1000 - a - b
            print(a, b, c)
            print(a * b * c)
    print(time.time() - start)


if __name__ == "__main__":
    main()
