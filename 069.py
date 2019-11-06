from utils import prime_generator


def main():
    n = 1
    for p in prime_generator():
        next_n = n * p
        if next_n > 10 ** 6:
            break
        n = next_n
    print(n)


if __name__ == "__main__":
    main()
