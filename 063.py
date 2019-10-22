import math


def main():
    print(sum(10 - math.ceil(10 ** (1 - 1 / n)) for n in range(1, 22)))


if __name__ == "__main__":
    main()
