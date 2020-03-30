from itertools import islice


def gen_sols():
    a, b = 2, 1
    while True:
        a, b = 9 * a + 20 * b, 4 * a + 9 * b
        if a % 5 in (2, 3):
            yield b


def main():
    print(sum(islice(gen_sols(), 12)))


if __name__ == "__main__":
    main()
