from utils import get_factors


def is_pandigital(string):
    return sorted(list(string)) == list(map(str, range(1, 10)))


def main():
    total = 0
    for prod in range(1000, 9999):
        for f in get_factors(prod):
            if is_pandigital("{}{}{}".format(prod, f, prod // f)):
                total += prod
                break
    print(total)


if __name__ == "__main__":
    main()
