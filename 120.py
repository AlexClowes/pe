def r_max(a):
    if a % 2 == 0:
        return a * (a - 2)
    else:
        return a * (a - 1)


def main():
    total = 0
    for a in range(3, 1001):
        total += r_max(a)
    print(total)


if __name__ == "__main__":
    main()
