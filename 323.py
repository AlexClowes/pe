from itertools import count


def main():
    last_EN, EN = 0, 1
    n = 1
    while EN - last_EN > 10 ** -11:
        last_EN = EN
        EN += 1 - (1 - 2 ** -n) ** 32
        n += 1
    print(f"{EN:.10f}")


if __name__ == "__main__":
    main()
